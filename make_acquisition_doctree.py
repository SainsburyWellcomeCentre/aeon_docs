import yaml
import subprocess
from pathlib import Path


def make_acquisition_doctree():
    """
    Create a doctree of all namespaces in aeon_acquisition.
    """
    src_path = Path("./src")
    subprocess.run(["dotnet", "docfx", "metadata", "--outputFormat", "markdown"], cwd=src_path)
    metadata_path = src_path.joinpath("reference", "acquisition")

    # get the acquisition doc header
    with open(metadata_path.joinpath("toc.yml"), "r") as f:
        acquisition_toc = yaml.safe_load(f)

    # write file for acquisition doc with header + doctree
    with open(metadata_path.with_suffix(".rst"), "w") as f:
        f.write("..\n  This file is auto-generated.\n\n")
        f.write(".. _target-acquisition-reference:\n\n")
        f.write("Acquisition Reference\n")
        f.write("=====================\n\n")
        f.write(".. toctree::\n")
        f.write("    :glob:\n\n")

        # all namespaces are children of the root element
        for namespace in acquisition_toc:
            namespace_name = namespace["name"]
            namespace_href = namespace.get("href")
            namespace_items = namespace.get("items")
            if namespace_href is None or namespace_items is None:
                continue

            # add namespace toctree entry
            f.write(f"    {namespace_name} <acquisition/{namespace_name}>\n")

            # generate toctree for each namespace document
            namespace_path = metadata_path.joinpath(namespace_href)
            with open(namespace_path, "r+", encoding="utf-8") as nsf:
                content = nsf.read()
                content += "```{toctree}\n"

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

                content += "\n```"
                nsf.seek(0)
                nsf.write(content)
                nsf.truncate()


if __name__ == "__main__":
    make_acquisition_doctree()
