from task_base import TaskBase


class ClearLogs(TaskBase):
    def __init__(self):
        super().__init__()

    def get_name(self):
        return "clear_logs"

    def _task_handler(self):
        self.log("starting world backup")


if __name__ == "__main__":
    task = ClearLogs()
    task.run()
