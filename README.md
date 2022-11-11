# KrétAnyád
Simple telegram bot that generates insults using the Kréta leaks.

## Install
1. Create a telegram bot using @BotFather
2. Create the commands `/start`,`/help`, and `/insult`.
3. Edit `Dockerfile` to add yout token
4. Run:
```bash
docker build -t valterm/kretanyad .
```

## Run
Run with the following command:
```bash
docker run -d name:tag
```