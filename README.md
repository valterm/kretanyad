# KrétAnyád
Simple telegram bot that generates insults using the Kréta leaks.

## Prepare
1. Create a telegram bot using @BotFather
2. Create the commands `/start`,`/help`, `/insult` and `/fuckyou`.
3. Edit `docker-compose.yml` to add your token

## Run
Run with the following command:
```bash
docker-compose up -d
```

Alternatively, you can make a local build of it using the Dockerfile, and edit `docker-compose.yml` to use your local tag.