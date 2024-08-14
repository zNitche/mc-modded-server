import os
from datetime import datetime
from yamcsr_scripts.config import Config, LogType
from yamcsr_scripts.common import logging


class TaskBase:
    @staticmethod
    def get_name() -> str:
        raise NotImplemented

    def log(self, message: str, type: LogType = LogType.INFO):
        filename = f"{self.get_name()}.log"
        mess = f"[{type.value}] - [{datetime.now().isoformat()}] - {message}"

        file_path = os.path.join(Config.LOGS_PATH, filename)
        logging.log_to_file(file_path, mess)

    def __log_runner(self, message: str, type: LogType = LogType.INFO):
        mess = f"[{type.value}] - [{datetime.now().isoformat()}] - [{self.get_name()}] - {message}"
        logging.log_to_file(Config.TASKS_RUNNER_LOGS_PATH, mess)

    def _task_handler(self):
        raise NotImplemented

    def run(self):
        try:
            self._task_handler()
        except Exception as e:
            self.__log_runner(str(e), LogType.ERROR)
