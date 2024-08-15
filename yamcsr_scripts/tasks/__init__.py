from yamcsr_scripts.tasks.task_base import TaskBase

from yamcsr_scripts.tasks.backup_world import BackupWorld

tasks_register = {
    BackupWorld.get_name(): BackupWorld,
}
