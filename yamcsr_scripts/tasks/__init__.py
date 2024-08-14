from yamcsr_scripts.tasks.task_base import TaskBase

from yamcsr_scripts.tasks.backup_world import BackupWorld
from yamcsr_scripts.tasks.clear_logs import ClearLogs

tasks_register = {
    BackupWorld.get_name(): BackupWorld,
    ClearLogs.get_name(): ClearLogs
}
