import sys
from yamcsr_scripts.tasks import tasks_register


def main(target: str):
    task = tasks_register.get(target)

    if task:
        task().run()


if __name__ == '__main__':
    main(sys.argv[1])
