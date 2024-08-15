import os
from yamcsr_scripts.config import Config
from yamcsr_scripts.common.logger import Logger


class TaskBase:
    def __init__(self):
        if self.get_name():
            self.logger = Logger(os.path.join(Config.LOGS_PATH, self.get_name()), "log.log",
                                 logger_name=f"{self.get_name()}_logger")

    @staticmethod
    def get_name() -> str:
        return None

    def _task_handler(self):
        raise NotImplemented

    def run(self):
        self._task_handler()
