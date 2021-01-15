import discord
from discord.ext import commands
import random
from configparser import ConfigParser


class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        config = ConfigParser()

    @commands.Cog.listener()
    async def on_ready(self):
        guildnum = 0
        guilds = await self.bot.fetch_guilds(limit=150).flatten()
        for _ in guilds:
            guildnum = guildnum + 1
        print(f'Logged in as: {self.bot.user.name}\n ID: {self.bot.user.id}\n API Version: {discord.__version__}\n Bot Version: 1.0.0\n Ruining {guildnum} guilds')

        # Changes our bots Playing Status. type=1(streaming) for a standard game you could remove type and url.
        await self.bot.change_presence(status=discord.Status.dnd, activity=(discord.Game('with my dick')))
        print(f'Successfully logged in and booted...!')
        print(
            '============================================================\n     Nigger\n============================================================')

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
        msg = msg.casefold()
        cumzone = ['Welcome to the cum zone',
                   'Only cum inside anime girls',
                   'Quivering clit, double jointed pussy',
                   'Fresh balls, elegant ejaculation',
                   'First the kiss, then the cum',
                   'My dick is in love with pain',
                   'Co-op cock torture',
                   'Stuff my dick into a furnace',
                   'Stitch my cock shut',
                   'Pressure cook my greasy balls',
                   'Cumblast me and make it snappy',
                   'What\'s all the cummotion?',
                   'My dad fell into a cum shaft',
                   'My dad glazed my face with cum',
                   'Fertilize a baby with hunk spunk',
                   'Cum spunk in my trunk',
                   'Cum craving toddler',
                   'Cum drippin\' cunt',
                   'Cummy Rae Jepsen',
                   'Cum me maybe',
                   'Cummy bottom boy',
                   'Night of the living cum',
                   'Nefarious cum mastermind',
                   'Cum makes me fearless',
                   'Cum crammer, cock slammer',
                   'Cum slammed ya mum',
                   'Mail your mums pieces of my dick',
                   'Bazinga!',
                   'Chug the cum',
                   'fug ya mum',
                   'Fuck my asshole full of cum',
                   'Three little words',
                   'Get fucked, nerd',
                   'Cum stuffer, '
                   'jenkem huffer',
                   'Fuck my cum puddle',
                   'Bottom stuffer',
                   'semen huffer',
                   'Would love a gator to fuck me',
                   'Undercooked baby pig penises',
                   'Help my dogs get a huge boner',
                   'Water bong full of cat cum',
                   'Accidentally fucked my own ass',
                   'I barely had any dicks inside me',
                   'Who ate all my cum? A mystery',
                   'Cum detective hot on the trail',
                   'Bees make honey, I make cummy']
        try:
            print(message.author.name, "#", message.channel.name, " : ", msg, )

            if 'epic' in msg:
                await message.channel.send("fucking еpic")

            elif 'cum' in msg and message.author != self.bot:
                await message.channel.send(random.choice(cumzone))

        except AttributeError:
            print("Direct Message received!")
            print(message.author.name, "[#] Direct Channel: ", msg)


# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.


def setup(bot):
    bot.add_cog(MainCog(bot))
