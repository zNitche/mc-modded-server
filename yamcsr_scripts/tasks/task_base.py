import os
from yamcsr_scripts.config import Config
from yamcsr_scripts.common.logger import Logger


class TaskBase:
    def __init__(self):
        self.__logger = Logger(Config.TASKS_RUNNER_LOGS_PATH, "tasks_runner.log",
                               logger_name="task_runner_logger")

        if self.get_name():
            self.logger = Logger(os.path.join(Config.LOGS_PATH, self.get_name()), "log.log",
                                 logger_name=f"{self.get_name()}_logger")

    @staticmethod
    def get_name() -> str:
        return None

    def _task_handler(self):
        raise NotImplemented

    def run(self):
        try:
            self._task_handler()

        except Exception:
            self.__logger.exception(f"Error while running: {self.get_name()}")
