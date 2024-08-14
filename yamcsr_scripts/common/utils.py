import tarfile
import os


def check_dir_existance(path: str):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)


def make_tarfile(source_path: str, output_path: str):
    if os.path.exists(source_path):
        with tarfile.open(output_path, "w:gz") as tar:
            tar.add(source_path, arcname=os.path.basename(source_path))


def get_oldest_files_to_remove(dir: str, files_count: int, extension: str | None) -> list[str]:
    files = []
    oldest_files = []

    for file in os.listdir(dir):
        if extension is None or file.endswith(extension):
            files.append(os.path.join(dir, file))

    files_diff = len(files) - files_count

    if files_diff >= 0:
        files.sort(key=os.path.getmtime)
        files_to_process = files_diff + 1

        for ind in range(files_to_process):
            file = files[ind]

            if os.path.exists(file):
                oldest_files.append(file)

    return oldest_files
