import discord
import asyncio
from discord.ext import commands


class CommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['invite', 'add'])
    async def link(self, ctx):
        await ctx.channel.trigger_typing()
        await asyncio.sleep(2)
        await ctx.send('lmao theyre so fucked')
        await ctx.send(
            'https://discord.com/api/oauth2/authorize?client_id=726088466370396270&permissions=238153216&scope=bot')

    @commands.command(aliases=['abt', 'a', 'who', 'prefix'])
    async def about(self, ctx, arg='n'):
        print(f'[+] About command run with/without prefix : {arg}')
        about = discord.Embed(title='About me!',
                              description='Bababoeey, I drop rice unconditionally ',
                              colour=discord.Color.purple(),
                              url='https://discord.com/api/oauth2/authorize?client_id=726088466370396270&permissions=8&scope=bot')
        about.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        about.set_thumbnail(url='https://moeninjagirls.files.wordpress.com/2019/01/ev1016.jpg')
        about.add_field(name='Author', value='Nick "Neekotine" Calvin')
        about.add_field(name='Complain to this guy', value='https://github.com/indefinick')
        about.add_field(name='Where should I bagogo',
                        value='https://discord.com/api/oauth2/authorize?client_id=726088466370396270&permissions=8&scope=bot',
                        inline=False)
        detail = discord.Embed(title='Dumbot - Discord Bot',
                               description='https://github.com/indefinick',
                               colour=discord.Color.purple())
        detail.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        detail.set_thumbnail(
            url='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/PyCharm_Logo.svg/1200px-PyCharm_Logo.svg.png')
        detail.add_field(name='Running on Python 3.9.1', value='Windows / Linux')
        detail.add_field(name='Built using Pycharm 2020.2.1',
                         value='Commercial, Freemium (open source parts are under Apache License)')

        if arg == 'n':
            await ctx.send(content=None, embed=about)
        elif arg == '-v':
            await ctx.send(content=None, embed=about)
            await ctx.send(content=None, embed=detail)

    @commands.command(aliases=["h", "help"])
    async def command_list(self, ctx):
        embed = discord.Embed(title="It's futile", description="You're helpless.",
                              color=discord.Color.purple())
        await ctx.send(embed=embed)

    @commands.command(aliases=["nickrev", "nickfix", "attendance"])
    async def nicknamefix(self, ctx):
        print('[+] Starting nickname fix command!')
        await ctx.send('Yall fuckos better have your name set')
        for guild in ctx.message.author.guild:
            for member in guild.members:
                print(member)
                await ctx.channel.send(member)
                try:
                    await ctx.member.edit(nick=None)
                except discord.Forbidden:
                    print('[!] Unable to change users name (Missing Permission)')
                    pass
        print('[+] Nickname fix command finished!')


def setup(bot):
    bot.add_cog(CommandsCog(bot))
