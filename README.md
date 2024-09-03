## yamcsr - yet another Minecraft server runner

### Description

While preparing for my next Minecraft gaming session, I had to find a way to host modded server locally.
I did such a thing in the past [here](https://github.com/zNitche/PiMinecraftServer), but this 2 years old solution is quite primitive.

My main goal was to have containerized server, with auto world backups + easy and secure access to server console.

And here we are after roughly month of work and 2 extra projects
([iscep](https://github.com/zNitche/iscep) and [yarcon](https://github.com/zNitche/yarcon)),
here we are having core functionalities and nice and expandable framework to build upon.

### Features
- containerized environment for running `Minecraft` servers.
- rcon ([yarcon](https://github.com/zNitche/yarcon)) integration.
- safe way to execute tasks / cron commands using [iscep](https://github.com/zNitche/iscep).
- cron based periodic tasks.

### Modules breakdown

#### core / server
Docker service running current server instance.

#### scripts
Core project scripts used by other modules.

#### tasks
Periodic tasks (handled via `cron`). This module run predefined tasks from `yamcsr_scripts` module.

Currently following tasks are supported:

- `BackupWorld` - creates world backup in `tar` archive, if 
modpack uses mods to perform backups (like `Simple Backups`), this task, or specified mod should
be disabled to prevent duplicated data.

#### bridge
bridge module is powered via [iscep](https://github.com/zNitche/iscep), and acts as a middleware between
3rd party apps and `yamcsr` tasks.

Currently following commands are supported:
- `BackupWorld` - create world backup (part of `yamcsr_scripts`)
- `OpPlayer` - change player operator status (executes rcon `op`/`deop` depending on passed parameter)

Do you want to integrate your service with this module ? Check [this](https://github.com/zNitche/iscep/blob/master/examples/client.py).

### How to use it

#### core setup
1. Create `.env` file

```
cp .env.template .env
```

2. Set the values that suit your needs (example 'Server Setup' section for Valhelsia modpack)

```
# Server Setup
SERVER_FILES_URL=https://www.curseforge.com/api/v1/mods/878495/files/5529449/download
SERVER_START_SCRIPT=ServerStart.sh
```

3. Build and start

```
docker compose build 
docker compose up -d
```

4. Attach to server container

```
docker container exec -it yamcsr_server bash
```

5. Edit `server.properties`

```
nano server.properties
```

6. Restart server to apply config changes

```
docker compose restart
```

#### tasks setup
Tasks are controlled via env variables (`Tasks` section of `.env`).

#### bridge setup
Settings can be changed in `Bridge` section of `.env` file.

Additional steps to consider:

- generate auth tokens (if `tokens.json` is not present in `yamcsr_bridge/auth_data`,
auth will be disabled, and all incoming packets will be processed)

```
python3 -m iscep.tokens_management --tokens-path tokens.json --add user_name
```

- generate SSL certificate to enable traffic encryption.
Like in previous case, all `*.pem` files have to be placed in `yamcsr_bridge/auth_data`

```
openssl req -x509 -newkey rsa:2048 -nodes -out cert.pem -keyout key.pem -days 365
```

### Extras
Server commands can be executed directly via console, to do it

1. Attach to server console

```
docker attach yamcsr_server
```

2. Execute command (for example list players)
```
list
```

3. Exit
```
Ctrl + P then Ctrl + Q
```

! note that `Ctrl + C` will stop the server !
