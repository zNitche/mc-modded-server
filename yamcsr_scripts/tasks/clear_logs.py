from yamcsr_scripts.tasks import TaskBase


class ClearLogs(TaskBase):
    def __init__(self):
        super().__init__()

    @staticmethod
    def get_name():
        return "clear_logs"

    def _task_handler(self):
        self.log("starting logs wipe")
