def log_to_file(file_path: str, message: str):
    with open(file_path, "a") as file:
        file.write(f"{message}\n")
