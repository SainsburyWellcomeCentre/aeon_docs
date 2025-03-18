import subprocess
from pathlib import Path

import yaml


def run_docfx_metadata(src_path: Path, output_format: str = "markdown"):
    """
    Run docfx metadata command to generate YAML files from source code.
    """
    subprocess.run(
        ["dotnet", "docfx", "metadata", "--outputFormat", f"{output_format}"],
        cwd=src_path,
    )


def rewrite_section(section: str):
    """
    Rewrite a single section of a namespace document as a list-table.
    """
    section_title, section_body = section.split("\n\n", 1)
    section_content = (
        f":::{{rubric}}{section_title}\n:::"
        "\n\n::: {list-table}\n:class: acquisition-api-table\n\n"
    )
    section_lines = section_body.split("\n\n")
    # Remove empty lines
    section_lines = [line for line in section_lines if line.strip()]
    # Check if description column is required
    has_description = any([not line.startswith(" [") for line in section_lines])
    for idx, section_line in enumerate(section_lines):
        is_description = not section_line.startswith(" [")
        if is_description:
            # Description column
            section_content += f"    - {section_line}\n"
        else:
            # Extract link text and URL
            link_text = section_line.split("[")[1].split("]")[0]
            link_path = section_line.split("(")[1].split(")")[0]
            # Reconstruct the link with backticks
            section_line = f"[`{link_text}`]({link_path})"
            section_content += f"*   - {section_line}\n"
        if not has_description:  # Single column table
            continue
        # Check if next line is a description line
        try:
            next_line = section_lines[idx + 1]
            if next_line.startswith(" [") and not is_description:
                # Account for empty description
                section_content += "    - \n"
        except IndexError:  # Last line
            if not is_description:
                section_content += "    - \n"
    section_content += ":::\n\n"
    return section_content


def process_namespace(namespace: dict, metadata_path: Path):
    """
    Process a single namespace from the toc file.

    Specifically, this function returns a table row and a toctree entry
    for the namespace on the main page.
    It also rewrites the namespace document and adds a toctree to it.
    """
    namespace_name = namespace["name"]
    namespace_href = namespace.get("href")
    namespace_items = namespace.get("items")
    if namespace_href is None or namespace_items is None:
        return None, None
    # Generate entry to table on main page that mimics aeon_mecha doc structure
    table_row = f"*   - [``{namespace_name}``](aeon_acquisition/{namespace_name})\n"
    # Generate toctree entry
    toctree_entry = f"    {namespace_name} <aeon_acquisition/{namespace_name}>\n"
    # Generate toctree for namespace document
    namespace_path = metadata_path.joinpath(namespace_href)
    with open(namespace_path, "r+", encoding="utf-8") as nsf:
        content = nsf.read()
        sections = content.split("###")
        content = sections[0]  # Page header
        for section in sections[1:]:
            content += rewrite_section(section)
        content += ":::{toctree}\n   :hidden:\n"
        # loop through all namespace items
        for item in namespace_items:
            item_name = item["name"]
            item_href = item.get("href")
            if item_href is None:  # item is category, skip for now
                continue
            # item is type, add toctree entry
            item_path = metadata_path.joinpath(item_href)
            item_filename = item_path.with_suffix("").name
            content += f"\n{item_name} <{item_filename}>"
        content += "\n:::"
        nsf.seek(0)
        nsf.write(content)
        nsf.truncate()
    return table_row, toctree_entry


def make_acquisition_doctree():
    """
    Create a doctree of all namespaces in aeon_acquisition.
    """
    # Generate .md API files from source code
    src_path = Path("src")
    run_docfx_metadata(src_path)
    # Path to main page (src/reference/api/aeon_acquisition.md)
    metadata_path = src_path.joinpath("reference", "api", "aeon_acquisition")
    # Get acquisition toc
    acquisition_toc = yaml.safe_load(metadata_path.joinpath("toc.yml").read_text())
    # Get the main page header
    api_head_path = Path("src") / "_templates" / "api_aeon_acquisition_head.md"
    api_head = api_head_path.read_text()
    # Initialise sections
    table_rows = ":::{list-table}\n:class: acquisition-api-table\n\n"
    toctree = ":::\n\n:::{toctree}\n    :glob:\n    :hidden:\n\n"
    # All namespaces are children of the root element
    for namespace in acquisition_toc:
        table_row, toctree_entry = process_namespace(namespace, metadata_path)
        table_rows += table_row
        toctree += toctree_entry
    toctree += "\n:::"
    with open(metadata_path.with_suffix(".md"), "w") as f:
        f.write(api_head + table_rows + toctree)


if __name__ == "__main__":
    make_acquisition_doctree()
