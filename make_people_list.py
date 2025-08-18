from io import StringIO
from pathlib import Path

import pandas as pd


def generate_csv_block(csv_file_path: str) -> str:
    """
    Generate a markdown-friendly CSV block from the given people.csv file.

    The CSV must have columns: First, Last, Affiliations.
    Output format:
        "Full Name","Affiliations"
    """
    df = pd.read_csv(csv_file_path, encoding="utf-8-sig")
    df = df.sort_values(by=["Last", "First"]).copy()
    df["Name"] = df["First"] + " " + df["Last"]
    df = df[["Name", "Affiliations"]]
    buffer = StringIO()
    df.to_csv(
        buffer, index=False, header=False, quoting=1, lineterminator="\n"
    )  # Quote all fields
    rows = buffer.getvalue().strip()
    return f'```{{csv-table}}\n:header: >\n:    "Name", "Affiliations"\n\n{rows}\n```'


if __name__ == "__main__":
    csv_path = Path("src/about/people.csv")
    header_path = Path("src/_templates/people_head.md")
    output_path = Path("src/about/people.md")
    new_block = generate_csv_block(csv_path)
    header_text = header_path.read_text(encoding="utf-8")
    output_text = header_text + new_block
    output_path.write_text(output_text, encoding="utf-8")
