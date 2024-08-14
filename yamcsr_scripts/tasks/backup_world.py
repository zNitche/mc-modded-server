import os
from datetime import datetime
from yamcsr_scripts.tasks import TaskBase
from yamcsr_scripts.config import Config, LogType
from yamcsr_scripts.common import utils


class BackupWorld(TaskBase):
    def __init__(self):
        super().__init__()

    @staticmethod
    def get_name():
        return "backup_world"

    def __remove_old_backups(self):
        to_keep_count = int(os.getenv("WORLD_BACKUPS_TO_KEEP", 1))

        files_to_remove = utils.get_oldest_files_to_remove(Config.WORLD_BACKUPS_PATH,
                                                           to_keep_count, ".tar.gz")
        removed_files = []

        for file in files_to_remove:
            os.remove(file)
            removed_files.append(file)

        self.log(f"removed {len(removed_files)} old backup/s")

    def should_create_backup(self) -> bool:
        if os.path.exists(Config.WORLD_PATH) and len(os.listdir(Config.WORLD_PATH)) > 0:
            return True

        return False

    def _task_handler(self):
        self.log("starting world backup")

        utils.check_dir_existance(Config.WORLD_BACKUPS_PATH)

        if self.should_create_backup():
            self.__remove_old_backups()

            timestamp = datetime.now().timestamp()
            output_path = os.path.join(Config.WORLD_BACKUPS_PATH, f"{timestamp}.tar.gz")

            try:
                utils.make_tarfile(Config.WORLD_PATH, output_path)
            except Exception as e:
                self.log(f"error while creating world backup: {str(e)}", LogType.ERROR)

            self.log(f"world backup completed, timestamp: {timestamp}")

        else:
            self.log(f"skipping world backup world dir is empty")
