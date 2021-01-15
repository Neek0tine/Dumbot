import asyncio
import random
from discord.ext import commands


class NukegenCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nuke(self, ctx):
        await ctx.trigger_typing()
        await asyncio.sleep(1)
        baselink = 'https://nhentai.net/g/'
        code = random.randint(1, 400000)
        code = str(code)
        url = baselink + code
        await ctx.channel.send(url)

# The setup function below is necessary. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.


def setup(bot):
    bot.add_cog(NukegenCog(bot))
