## YAMCSR - Yet Another Minecraft Server Runner

### Server commands
1. Attach to server console

```
sudo docker attach yamcsr_server
```

2. Execute command (for example list players)
```
list
```

3. Exit
```
Ctrl + P then Ctrl + Q
```

note that `Ctrl + C` will stop server.


## Notes

```
python3 -m iscep.tokens_management --tokens-path tokens.json --add user_name
```

```
openssl req -x509 -newkey rsa:2048 -nodes -out cert.pem -keyout key.pem -days 365
```
