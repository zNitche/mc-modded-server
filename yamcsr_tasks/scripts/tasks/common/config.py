import os
from enum import Enum


class LogType(Enum):
    INFO = "INFO"
    ERROR = "ERROR"


class Config:
    TASKS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    SCRIPTS_PATH = os.path.abspath(os.path.join(TASKS_PATH, os.pardir))
    MODULE_PATH = os.path.abspath(os.path.join(SCRIPTS_PATH, os.pardir))

    LOGS_PATH = os.path.join(MODULE_PATH, "logs")
    TASKS_RUNNER_LOGS_PATH = os.path.join(LOGS_PATH, "tasks_runner.log")

    FILES_PATH = os.path.join(MODULE_PATH, "files")
    BACKUPS_PATH = os.path.join(FILES_PATH, "backups")
    
    WORLD_BACKUPS_PATH = os.path.join(BACKUPS_PATH, "world")

    # from docker-compose.yml
    SERVER_DATA_PATH = "/yamcsr_server_data"
    WORLD_PATH = os.path.join(SERVER_DATA_PATH, "world")
