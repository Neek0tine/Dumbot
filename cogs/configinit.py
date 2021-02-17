from configparser import ConfigParser
import asyncio
import random
import discord
from discord.ext import commands


class ConfigInit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def anti_cum(self, ctx, state, member: discord.Member.id = None):
        if not member:
            member = ctx.author
            print(member)

        config = ConfigParser()
        config.read('config.ini')
        state = state.casefold()
        data = config['BOT_CFG']
        if state == "":
            await ctx.channel.send(f'Anti Cum State : {data["anti_cum"]}')
        elif state == "false" or "true" and member.id == 256713166149386240:
            if state == 'false':
                data["anti_cum"] = 'False'
            elif state == 'true':
                data['anti_cum'] = 'True'
            await ctx.channel.send(f'Changing Anti Cum state to {state}')
            with open('config.ini', 'w') as conf:
                config.write(conf)
        else:
            await ctx.channel.send('cum')

# The setup function below is necessary. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.


def setup(bot):
    bot.add_cog(ConfigInit(bot))
