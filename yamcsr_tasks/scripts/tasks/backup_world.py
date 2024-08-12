import os
from datetime import datetime
from common.task_base import TaskBase
from common.config import Config, LogType
from common import utils


class BackupWorld(TaskBase):
    def __init__(self):
        super().__init__()

    def get_name(self):
        return "backup_world"

    def __remove_old_backups(self):
        to_keep_count = int(os.getenv("WORLD_BACKUPS_TO_KEEP", 1))
        backup_files = []
        removed_files = []

        for file in os.listdir(Config.WORLD_BACKUPS_PATH):
            if file.endswith(".tar.gz"):
                backup_files.append(file)

        if len(backup_files) >= to_keep_count:
            files_by_age = sorted(backup_files, key=lambda fn : fn[:-6])
            files_diff = len(backup_files) - to_keep_count

            for file in files_by_age[:files_diff if files_diff > 0 else 1]:
                file_path = os.path.join(Config.WORLD_BACKUPS_PATH, file)

                if os.path.exists(file_path):
                    os.remove(file_path)
                    removed_files.append(file)

        self.log(f"removed {len(removed_files)} backups")
                

    def _task_handler(self):
        self.log("starting world backup")

        utils.check_dir_existance(Config.WORLD_BACKUPS_PATH)

        self.__remove_old_backups()

        timestamp = datetime.now().timestamp()
        output_path = os.path.join(Config.WORLD_BACKUPS_PATH, f"{timestamp}.tar.gz")

        try:
            utils.make_tarfile(Config.WORLD_PATH, output_path)
        except Exception as e:
            self.log(f"error while creating world backup: {str(e)}", LogType.ERROR)

        self.log(f"world backup completed, timestamp: {timestamp}")


if __name__ == "__main__":
    task = BackupWorld()
    task.run()
