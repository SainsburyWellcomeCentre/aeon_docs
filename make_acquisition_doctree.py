import subprocess
from pathlib import Path

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


def make_acquisition_doctree():
    """Create a doctree of all namespaces in aeon_acquisition."""

    # Generate xml docs using doxygen
    subprocess.run(["doxygen"])
    src_path = Path("src") / "reference" / "api" / "acquisition"
    # Create directory for acquisition docs
    src_path.mkdir(parents=True, exist_ok=True)
    # Write file for acquisition main page with header + toctree
    with open(src_path.with_suffix(".rst"), "w") as f:
        f.write("""..
   This file is auto-generated.

.. _target-acquisition-reference:

``aeon_acquisition``
=====================

.. toctree::
   :maxdepth: 1
   :glob:

   acquisition/*
""")

    # Parse the doxygen-generated index.xml file
    index = ET.parse(Path("src") / "xml" / "index.xml")
    root = index.getroot()
    aeon_namespaces = root.xpath(
        ".//compound[@kind='namespace' and starts-with(name, 'Aeon::') and not (starts-with(name, 'Aeon::Tests'))]"
    )
    ns_names = [ns.findtext("name") for ns in aeon_namespaces]
    for ns in aeon_namespaces:
        ns_name = ns.findtext("name")
        ns_name_formatted = ns_name.replace("::", ".")
        ns_kind = ns.get("kind")
        ns_refid = ns.get("refid")
        file_content = f"""..
   This file is auto-generated.

{ns_name_formatted}
{'=' * len(ns_name_formatted)}

.. doxygennamespace:: {ns_name}
    :desc-only:
"""
        # Find all enums in the namespace
        enums = ns.findall(".//member[@kind='enum']")
        if enums:
            file_content += """
Enums
-----
"""
        for enum in enums:
            enum_name = enum.findtext("name")
            file_content += f"""
{enum_name}
{'^' * len(enum_name)}

.. doxygenenum:: {enum_name}
"""
        # Find all classes in the namespace
        classes = root.xpath(
            f".//compound[@kind='class' and contains(@refid, '{ns_refid.replace(ns_kind, '')}')]"
        )
        if classes:
            file_content += """
Classes
-------
"""
        for class_ in classes:
            class_name = class_.findtext("name")
            if determine_namespace(class_name, ns_names) != ns_name:
                continue
            class_name_formatted = class_name.replace(f"{ns_name}::", "").replace(
                "::", "."
            )
            file_content += f"""

{class_name_formatted}
{'^' * len(class_name_formatted)}

.. doxygenclass:: {class_name}
   :members: 
   :undoc-members:
   :protected-members:
   :allow-dot-graphs:
"""
        # Find all structs in the namespace
        structs = root.xpath(
            f".//compound[@kind='struct' and contains(@refid, '{ns_refid.replace(ns_kind, '')}')]"
        )
        if structs:
            file_content += """
Structs
-------
"""
        for struct in structs:
            struct_name = struct.findtext("name")
            struct_name_formatted = struct_name.replace(f"{ns_name}::", "").replace(
                "::", "."
            )
            file_content += f"""

{struct_name_formatted}
{'^' * len(struct_name_formatted)}

.. doxygenstruct:: {struct_name}
   :members: 
   :undoc-members:
   :protected-members:
   :allow-dot-graphs:
"""
        with open(src_path / f"{ns_name_formatted}.rst", "w") as file:
            file.write(file_content)


if __name__ == "__main__":
    make_acquisition_doctree()
