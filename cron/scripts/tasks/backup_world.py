from task_base import TaskBase


class BackupWorld(TaskBase):
    def __init__(self):
        super().__init__()

    def get_name(self):
        return "backup_world"

    def _task_handler(self):
        self._log("test")


if __name__ == "__main__":
    task = BackupWorld()
    task.run()
