import logging
import os
from logging.handlers import TimedRotatingFileHandler
from yamcsr_scripts.common import utils


class Logger:
    def __init__(self, logs_path: str, log_filename: str, logger_name: str | None = None):
        utils.check_dir_existance(logs_path)

        self.log_filename = os.path.join(logs_path, log_filename)
        self.__logger = logging.getLogger(__name__ if logger_name is None else logger_name)

        self.__setup_handlers()

    def __setup_handlers(self):
        self.__logger.setLevel("DEBUG")

        formatter = self.__get_formatter()

        console_logger = logging.StreamHandler()
        console_logger.setFormatter(formatter)

        console_logger.setLevel("DEBUG")
        self.__logger.addHandler(console_logger)

        file_handler = TimedRotatingFileHandler(filename=self.log_filename,
                                                when="M",
                                                encoding="utf-8",
                                                backupCount=10)
        file_handler.setFormatter(formatter)
        file_handler.setLevel("INFO")

        self.__logger.addHandler(file_handler)

    def __get_formatter(self) -> logging.Formatter:
        formatter = logging.Formatter(
            "{asctime} - {levelname} - {message}",
            style="{",
            datefmt="%Y-%m-%d %H:%M",
        )

        return formatter

    def exception(self, message: str):
        self.__logger.exception(message)

    def error(self, message: str):
        self.__logger.error(message)

    def info(self, message: str):
        self.__logger.info(message)

    def debug(self, message: str):
        self.__logger.debug(message)
