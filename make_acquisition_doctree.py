import subprocess
from pathlib import Path

from jinja2 import FileSystemLoader
from jinja2.sandbox import SandboxedEnvironment
from lxml import etree as ET


def determine_namespace(name, namespaces):
    """Determine the parent namespace of an element by its name."""
    # Tokenise the name by "::"
    tokens = name.split("::")
    # Prioritise lower-level namespaces
    sorted_namespaces = sorted(
        namespaces, key=lambda ns: len(ns.split("::")), reverse=True
    )
    for ns in sorted_namespaces:
        ns_tokens = ns.split("::")
        if ns_tokens == tokens[: len(ns_tokens)]:
            return ns
    return None


def get_aeon_namespaces(root):
    """Get all Aeon namespaces except for Tests."""
    return root.xpath(
        ".//compound[@kind='namespace' and starts-with(name, 'Aeon::') and not (starts-with(name, 'Aeon::Tests'))]"
    )


def generate_section(root, namespace, data_type):
    """Generate the section for enum, class, or struct."""
    ns_names = [ns.findtext("name") for ns in get_aeon_namespaces(root)]
    ns_name = namespace.findtext("name")
    ns_kind = namespace.get("kind")
    ns_refid = namespace.get("refid")
    if data_type == "enum":
        elements = namespace.findall(f".//member[@kind='{data_type}']")
    else:
        elements = root.xpath(
            f".//compound[@kind='{data_type}' and contains(@refid, '{ns_refid.replace(ns_kind, '')}')]"
        )
        elements = [
            elem
            for elem in elements
            if determine_namespace(elem.findtext("name"), ns_names) == ns_name
        ]
    if not elements:
        return None
    return generate_section_content(elements, data_type, ns_name)


def generate_section_content(elements, data_type, namespace_name):
    """Generate the section content for enum, class, or struct."""
    content = ""
    for elem in elements:
        name = elem.findtext("name")
        name_formatted = name.replace(f"{namespace_name}::", "").replace("::", ".")
        content += f"""
{name_formatted}
{"^" * len(name_formatted)}

.. doxygen{data_type}:: {name}
"""
        if data_type != "enum":
            content += """   :members:
   :undoc-members:
   :allow-dot-graphs:
"""
    return content


def make_acquisition_doctree():
    """Create a doctree of all namespaces in aeon_acquisition."""

    # Generate xml docs using doxygen
    subprocess.run(["doxygen"])
    src_root = Path("src")
    acquisition_path = src_root / "reference" / "api" / "aeon_acquisition"
    templates_path = src_root / "_templates"
    # Create directory for acquisition docs
    acquisition_path.mkdir(parents=True, exist_ok=True)
    # Parse the doxygen-generated index.xml file
    index = ET.parse(src_root / "xml" / "index.xml")
    root = index.getroot()
    # Get the main page header
    api_head_path = templates_path / "api_aeon_acquisition_head.rst"
    api_file_content = api_head_path.read_text()
    # Get the namespace template
    env = SandboxedEnvironment(loader=FileSystemLoader(templates_path))
    ns_template = env.get_template("api_aeon_acquisition_namespace.rst")
    # For each namespace, add a toc entry to the main page,
    # and create a page for the namespace
    with acquisition_path.with_suffix(".rst").open("w") as api_file:
        for ns in get_aeon_namespaces(root):
            ns_name = ns.findtext("name")
            ns_name_formatted = ns_name.replace("::", ".")
            # Add toc entry to table on main page to mimic aeon_mecha doc structure
            api_file_content += f"   * - :cs:namespace:`{ns_name_formatted}`\n"
            with (acquisition_path / f"{ns_name_formatted}.rst").open("w") as ns_file:
                ns_file.write(
                    ns_template.render(
                        name_formatted=ns_name_formatted,
                        underline="=" * len(ns_name_formatted),
                        name=ns_name,
                        enums=generate_section(root, ns, "enum"),
                        classes=generate_section(root, ns, "class"),
                        structs=generate_section(root, ns, "struct"),
                    )
                )
        api_file.write(api_file_content)


if __name__ == "__main__":
    make_acquisition_doctree()
