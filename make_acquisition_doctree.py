import subprocess
from pathlib import Path

import yaml


def make_acquisition_doctree():
    """
    Create a doctree of all namespaces in aeon_acquisition.
    """
    src_path = Path("src")
    subprocess.run(
        ["dotnet", "docfx", "metadata", "--outputFormat", "markdown"], cwd=src_path
    )
    metadata_path = src_path.joinpath("reference", "api", "acquisition")
    # Get acquisition toc
    with open(metadata_path.joinpath("toc.yml"), "r") as f:
        acquisition_toc = yaml.safe_load(f)
    # Initialise content for main page
    api_head = (
        "<!-- This file is auto-generated. -->\n\n"
        "(target-acquisition-reference)="
        "\n# ``aeon_acquisition``\n\n"
    )
    table_rows = ":::{list-table}\n:class: acquisition-api-table\n\n"
    toctree = ":::\n\n:::{toctree}\n    :glob:\n    :hidden:\n\n"
    # All namespaces are children of the root element
    for namespace in acquisition_toc:
        namespace_name = namespace["name"]
        namespace_href = namespace.get("href")
        namespace_items = namespace.get("items")
        if namespace_href is None or namespace_items is None:
            continue
        # Add toc entry to table on main page to mimic aeon_mecha doc structure
        table_rows += f"*   - [``{namespace_name}``](acquisition/{namespace_name})\n"
        # Add namespace toctree entry
        toctree += f"    {namespace_name} <acquisition/{namespace_name}>\n"
        # Generate toctree for each namespace document
        namespace_path = metadata_path.joinpath(namespace_href)
        with open(namespace_path, "r+", encoding="utf-8") as nsf:
            content = nsf.read()
            sections = content.split("###")
            content = sections[0]
            for section in sections[1:]:
                section_title, section_body = section.split("\n\n", 1)
                section_content = f":::{{rubric}}{section_title}\n:::\n\n::: {{list-table}}\n:class: acquisition-api-table\n\n"
                section_lines = section_body.split("\n\n")
                # Remove empty lines
                section_lines = [line for line in section_lines if line.strip()]
                # Check if description column is required
                has_description = any(
                    [not line.startswith(" [") for line in section_lines]
                )
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
                content += section_content
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
    toctree += "\n:::"
    with open(metadata_path.with_suffix(".md"), "w") as f:
        f.write(api_head + table_rows + toctree)


if __name__ == "__main__":
    make_acquisition_doctree()
