FROM python:latest
FROM gorialis/discord.py

RUN mkdir -p /usr/src/bot
WORKDIR /usr/src/bot

COPY . .

EXPOSE 5000

CMD [ "python", "./bilbot.py" ]
