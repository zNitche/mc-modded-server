import yarcon
from yamcsr_scripts.config import Config


def send_cmd(command: str):
    if Config.RCON_ENABLED:
        with yarcon.Connection(Config.SERVER_SERVICE_NAME, Config.RCON_PORT) as conn:
            logged_in = conn.login(Config.RCON_PASSWORD)

            if logged_in:
                conn.command(command)
