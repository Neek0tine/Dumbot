import discord
from discord.ext import commands


class StartupCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        guildnum = 0
        guilds = await self.bot.fetch_guilds(limit=150).flatten()
        for _ in guilds:
            guildnum = guildnum + 1
        print(
            f'Logged in as: {self.bot.user.name}\n ID: {self.bot.user.id}\n API Version: {discord.__version__}\n Bot '
            f'Version: 1.4.0\n Ruining {guildnum} guilds')

        # Changes our bots Playing Status. type=1(streaming) for a standard game you could remove type and url.
        await self.bot.change_presence(status=discord.Status.dnd, activity=(discord.Game('with my dick')))
        print(f'Successfully logged in and booted...!')
        print(
            '============================================================\n     '
            'Æughē\n============================================================')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('cum {0.mention}.'.format(member))

    @commands.Cog.listener()
    async def on_member_leave(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('cum {0.mention}.'.format(member))

    @commands.Cog.listener()
    async def on_message(self, message):
        msg = message.content
        if not message.guild:
            print(message.author.name, "#", "Direct Message : ", msg)  # Log all chat to stdout
        else:
            print(message.author.name, "#", message.channel.name, " : ", msg)  # Log all chat to stdout


def setup(bot):
    bot.add_cog(StartupCog(bot))
