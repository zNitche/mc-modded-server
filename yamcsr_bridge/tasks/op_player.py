from iscep import Task
from yamcsr_scripts.common import rcon


class OpPlayer(Task):
    def __init__(self):
        super().__init__("op_player")

    def module(self, player_name: str, set_to_op: bool):
        cmd = f"op {player_name}" if set_to_op else f"deop {player_name}"
        rcon.send_cmd(cmd)
