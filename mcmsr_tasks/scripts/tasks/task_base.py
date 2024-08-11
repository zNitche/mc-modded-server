import os
from datetime import datetime
from config import Config, LogType


class TaskBase:
    def __init__(self):
        pass

    def get_name(self) -> str:
        raise NotImplemented
    
    def log(self, message: str, type: LogType = LogType.INFO):
        filename = f"{self.get_name()}_logs.log"
        mess = f"[{type.value}] - [{datetime.now().isoformat()}] - {message}"

        self.__log_message(mess, os.path.join(Config.LOGS_PATH, filename))

    def __log_runner(self, message: str, type: LogType = LogType.INFO):
        mess = f"[{type.value}] - [{datetime.now().isoformat()}] - [{self.get_name()}] - {message}"
        self.__log_message(mess, Config.TASKS_RUNNER_LOGS_PATH)

    def __log_message(self, message: str, path: str):
        with open(path, "a") as file:
            file.write(f"{message}\n")

    def _task_handler(self):
        raise NotImplemented

    def run(self):
        try:
            self._task_handler()
        except Exception as e:
            self.__log_runner(str(e), LogType.ERROR)
