import os


MODULE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


def main():
    with open(os.path.join(MODULE_ROOT, "world_backup.txt"), "a") as file:
        file.write("test backup\n")


if __name__ == "__main__":
    main()
