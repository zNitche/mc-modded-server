import os


class Config:
    MODULE_PATH = os.path.abspath(os.path.dirname(__file__))
    PROJECT_PATH = os.path.abspath(os.path.join(MODULE_PATH, os.pardir))

    LOGS_PATH = "/yamcsr_logs"
    TASKS_RUNNER_LOGS_PATH = os.path.join(LOGS_PATH, "tasks_runner")

    FILES_PATH = "/yamcsr_files"
    BACKUPS_PATH = os.path.join(FILES_PATH, "backups")
    
    WORLD_BACKUPS_PATH = os.path.join(BACKUPS_PATH, "world")

    # from docker-compose.yml
    SERVER_DATA_PATH = "/yamcsr_server_data"
    WORLD_PATH = os.path.join(SERVER_DATA_PATH, "world")
