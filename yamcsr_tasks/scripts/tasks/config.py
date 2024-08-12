import os
from enum import Enum


class LogType(Enum):
    INFO = "INFO"
    ERROR = "ERROR"


class Config:
    TASKS_PATH = os.path.abspath(os.path.dirname(__file__))
    SCRIPTS_PATH = os.path.abspath(os.path.join(TASKS_PATH, os.pardir))
    MODULE_PATH = os.path.abspath(os.path.join(SCRIPTS_PATH, os.pardir))

    LOGS_PATH = os.path.join(MODULE_PATH, "logs")
    TASKS_RUNNER_LOGS_PATH = os.path.join(LOGS_PATH, "tasks_runner.log")
