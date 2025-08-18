import re

import pandas as pd
import chardet

def read_csv_safely(filepath):
    with open(filepath, "rb") as f:
        raw_data = f.read()
        detected = chardet.detect(raw_data)
        encoding = detected["encoding"]
    return pd.read_csv(filepath, encoding=encoding)


# Generate new csv block
def generate_csv_block(csv_file_path):
    df = read_csv_safely(csv_file_path)
    df_sorted = df.sort_values(by=["Last", "First"])
    df_sorted["Name"] = df_sorted["First"] + " " + df_sorted["Last"]
    df_sorted = df_sorted.drop(columns=["First", "Last"])
    col_names = ["Name", "Affiliations"]
    df_sorted = df_sorted[col_names]
    new_block = (
        "```{csv-table}\n"
        + ":header: >\n:    "
        + ", ".join([f'"{col}"' for col in col_names])
        + "\n\n"
    )
    for _, row in df_sorted.iterrows():
        new_block += f'"{row["Name"]}","{row["Affiliations"]}"\n'
    new_block += "```"
    return new_block


if __name__ == "__main__":
    new_block = generate_csv_block("src/about/people.csv")
    with open("src/about/people.md", "r", encoding="utf-8") as f:
        content = f.read()
    updated_content = re.sub(
        r"```{csv-table}.*?```", new_block, content, flags=re.DOTALL
    )
    if updated_content != content:
        with open("src/about/people.md", "w", encoding="utf-8") as f:
            f.write(updated_content)
