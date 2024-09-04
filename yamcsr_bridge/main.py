import os
from iscep import Server
from tasks.backup_world import BackupWorldTask
from tasks.op_player import OpPlayer


def register_tasks(server: Server):
    server.register_task(BackupWorldTask())
    server.register_task(OpPlayer())


def create_server() -> Server:
    server = Server(port=8989,
                    logs_path="/yamcsr_logs/bridge",
                    auth_tokens_path="auth_data/tokens.json",
                    ssl_key_file="auth_data/key.pem",
                    ssl_cert_file="auth_data/cert.pem")

    return server


if __name__ == '__main__':
    module_enabled = int(os.getenv("BRIDGE_MODULE_ENABLED", 0))

    if module_enabled:
        server = create_server()
        register_tasks(server)

        server.run()
