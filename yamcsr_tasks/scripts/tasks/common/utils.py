import tarfile
import os


def check_dir_existance(path: str):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

def make_tarfile(source_path: str, output_path: str):
    with tarfile.open(output_path, "w:gz") as tar:
        tar.add(source_path, arcname=os.path.basename(source_path))
