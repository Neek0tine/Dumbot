# Dumbot; Discord.py [rewrite] 1.3.4
from discord.ext import commands
import os

BOT_TOKEN = 'NzIyMTA5MDcyMjk1NTkxOTY4.XueSeg.PDh_CPeRCRKS9fKSYO8xlw8vTI4'
BOT_INVITE = 'https://discord.com/api/oauth2/authorize?client_id=722109072295591968&permissions=1543761142&scope=bot'


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
