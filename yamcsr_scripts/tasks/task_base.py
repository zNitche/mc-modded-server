import os
from yamcsr_scripts.config import Config
from yamcsr_scripts.common.logger import Logger
import yarcon


class TaskBase:
    def __init__(self):
        self.logger = None

        if self.get_name():
            self.logger = Logger(os.path.join(Config.LOGS_PATH, self.get_name()), "log.log",
                                 logger_name=f"{self.get_name()}_logger")

    @staticmethod
    def get_name() -> str:
        return None

    def write_to_server_console(self, message: str):
        try:
            with yarcon.Connection(Config.SERVER_SERVICE_NAME, 25575) as conn:
                conn.command(f"say {message}")

        except Exception:
            if self.logger is not None:
                self.logger.exception(f"Error while writing to server console")

    def _task_handler(self):
        raise NotImplemented

    def run(self):
        self._task_handler()
