import os
import typing
from yamcsr_scripts.common import rcon
from yamcsr_scripts.config import Config
from yamcsr_scripts.common.logger import Logger


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
            rcon.send_cmd(f"say {message}")

        except Exception:
            if self.logger is not None:
                self.logger.exception(f"Error while writing to server console")

    def write_to_console(self,
                         message: str,
                         logger: typing.Callable[[str], None] = None,
                         propagate_to_server: bool = False):

        logger = logger if logger is not None else self.logger.info
        logger(message)

        if propagate_to_server:
            self.write_to_server_console(message)

    def _task_handler(self):
        raise NotImplemented()

    def run(self):
        self._task_handler()
