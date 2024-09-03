from iscep import Task
from yamcsr_scripts.tasks import BackupWorld as BackupWorldScript


class BackupWorldTask(Task):
    def __init__(self):
        super().__init__("backup_world")

    def module(self):
        task = BackupWorldScript()
        task.run()
