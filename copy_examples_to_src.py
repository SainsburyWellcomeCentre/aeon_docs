import os
import shutil


def copy_ipynb_files(src_dirs: str | list[str], dst_dir: str) -> None:
    """
    Copy all ``.ipynb`` files from ``src_dirs`` to ``dst_dir``.

    Args:
        src_dirs (str | list[str]): A list of directories or a single directory.
        dst_dir (str): The destination directory.
    """
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    if not isinstance(src_dirs, list):
        src_dirs = [src_dirs]

    for src_dir in src_dirs:
        for file_name in os.listdir(src_dir):
            if file_name.endswith(".ipynb"):
                name, extension = os.path.splitext(file_name)
                # Append "_copy" to the name
                new_file_name = f"{name}_copy{extension}"
                shutil.copy(
                    os.path.join(src_dir, file_name),
                    os.path.join(dst_dir, new_file_name),
                )


if __name__ == "__main__":
    src_dir = os.path.join("aeon_mecha", "docs", "examples")
    dst_dir = os.path.join("src", "user", "how_to")
    print(src_dir, dst_dir)
    copy_ipynb_files(src_dir, dst_dir)