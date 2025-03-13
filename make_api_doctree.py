import os
from pathlib import Path

# modules to ignore in the api doc
ignore_modules = []


def make_api_doctree():
    """
    Create a doctree of all modules in aeon_api/swc/aeon.
    """
    doctree = ""
    api_path = Path("aeon_api") / "swc" / "aeon"
    for path in sorted(api_path.rglob("*.py")):
        if path.name.startswith("_"):
            continue
        # Convert file path to module name
        full = str(path.with_suffix("")).replace(os.sep, ".")
        full = ".".join(full.split(".")[1:])
        if not any(full.startswith(ignore_module) for ignore_module in ignore_modules):
            doctree += f"   {full}\n"
    # Get the main page header
    api_head_path = Path("src") / "_templates" / "api_aeon_api_head.rst"
    api_head = api_head_path.read_text()
    # Write main page with header and doc tree
    output_dir = Path("src") / "reference" / "api"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "aeon_api.rst"
    with output_file.open("w") as f:
        f.write(api_head)
        f.write(doctree)


if __name__ == "__main__":
    make_api_doctree()
