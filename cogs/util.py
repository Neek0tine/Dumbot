import random
import configparser
import asyncio
from responses import cumzone
import discord
from boo import boo
from discord.ext import commands
import pickle

class UtilCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if 'gu' or 'bu' or 'ga' in msg:
            if (message.author.bot):

def setup(bot):
    bot.add_cog(UtilCog(bot))
