# Dumbot; Discord.py [rewrite] 1.7.3
from discord.ext import commands
from threading import Thread
from flask import Flask
import psutil
import os


print("Getting token ...")
BOT_TOKEN = os.environ["dumbot_token"]
print('Bot token get!')


app = Flask('')


@app.route('/')
def main():
    stats = f"TSDBot; Discord.py [rewrite] 1.7.3 -- Status : Up -- Ram Usage: {psutil.virtual_memory().percent} % -- " \
            f"Available Memory: {round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)} %"
    return stats


def run():
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 33507)))

def keep_alive():
    server = Thread(target=run)
    server.start()


keep_alive()


def get_prefix(bot, message):
    prefixes = ['d ', 'dumbot ', 'D']
    if not message.guild:
        return 'd '
    return commands.when_mentioned_or(*prefixes)(bot, message)


client = commands.Bot(command_prefix=get_prefix)

if __name__ == '__main__':
    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            client.load_extension(f'cogs.{file[:-3]}')
            print(f'Cog loaded : {file}')

client.run(BOT_TOKEN, bot=True, reconnect=True)
