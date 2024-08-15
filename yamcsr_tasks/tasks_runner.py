import sys
from yamcsr_scripts.tasks import tasks_register
from yamcsr_scripts.common.logger import Logger
from yamcsr_scripts.config import Config


class TasksRunner:
    def __init__(self):
        self.__logger = Logger(Config.TASKS_RUNNER_LOGS_PATH, "tasks_runner.log",
                               logger_name="tasks_runner_logger")

    def run(self, module_name: str):
        task = tasks_register.get(module_name)

        if task:
            try:
                task().run()
            except Exception:
                self.__logger.exception(f"Error while running {module_name}")

        else:
            self.__logger.error(f"Module {module_name} not found")


if __name__ == '__main__':
    runner = TasksRunner()
    runner.run(sys.argv[1])
