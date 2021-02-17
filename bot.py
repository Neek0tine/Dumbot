# Dumbot; Discord.py [rewrite] 1.3.4
from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')

from discord.ext import commands
import os

data = config['BOT_CFG']
BOT_TOKEN = data['TOKEN']
BOT_INVITE = data['INVITE']


def get_prefix(bot, message):
    prefixes = ['d ', 'dumbot ']
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
