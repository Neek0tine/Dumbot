# Dumbot; Discord.py [rewrite] 1.7.3
from discord.ext import commands
from threading import Thread
from flask import Flask, render_template
import os
import datetime
import time
import psutil
import os
import sqlite3


print("Getting token ...")
BOT_TOKEN = os.environ["dumbot_token"]
print('Bot token get!')


app = Flask('')


@app.route('/')
def main():
    usage = psutil.virtual_memory().percent
    avail = round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)
    return render_template('page.html', usage=usage, avail=avail)


def run():
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 33507)), debug=False)


def keep_alive():
    server = Thread(target=run)
    server.start()
    # run()


keep_alive()


def get_prefix(bot, message):
    prefixes = ['d ', 'dumbot ', 'D ', 'd  ', 'D  ']
    if not message.guild:
        return 'd '
    return commands.when_mentioned_or(*prefixes)(bot, message)


client = commands.Bot(command_prefix=get_prefix)
client.remove_command('help')

if __name__ == '__main__':

    db = sqlite3.connect("dumbot.db")
    print("SQLite database version:", sqlite3.version)

    selector = db.cursor()
    selector.execute("DROP TABLE IF EXISTS PREVIEWER")
    selector.execute("DROP TABLE IF EXISTS RANDOMIZER")
    previewer  = """ CREATE TABLE PREVIEWER (
    ID INTEGER(6) PRIMARY KEY NOT NULL,
    NID INTEGER(6),
    URL VARCHAR(29),
    PAGE INTEGER(4),
    
    CONSTRAINT fk_column
    FOREIGN KEY (ID)
    REFERENCES RANDOMIZER(ID)
    )"""
    selector.execute(previewer)

    randomizer = """ CREATE TABLE RANDOMIZER(
    ID INTEGER(6) PRIMARY KEY NOT NULL,
    NID INTEGER(6)
    )"""

    if os.path.exists("cogs/weather forecast.csv"):
        os.remove("cogs/weather forecast.csv")

    else:
        pass

    selector.execute(randomizer)
    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            client.load_extension(f'cogs.{file[:-3]}')
            print(f'Cog loaded : {file}')

client.run(BOT_TOKEN, bot=True, reconnect=True)
