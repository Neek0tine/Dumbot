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
            'https://discord.com/api/oauth2/authorize?client_id=722109072295591968&permissions=140328299584&scope=bot')

    @commands.command(aliases=['abt', 'a', 'who', 'prefix'])
    async def about(self, ctx, arg='n'):
        print(f'[+] About command run with/without prefix : {arg}')
        about = discord.Embed(title='who the fuck am I',
                              description='Bababoeey, I drop rice unconditionally. Basically a porn bot',
                              colour=discord.Color.purple(),
                              url='https://discord.com/api/oauth2/authorize?client_id=726088466370396270&permissions=8&scope=bot')
        about.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        about.set_thumbnail(url='https://raw.githubusercontent.com/Neek0tine/Dumbot/master/va.png')
        about.add_field(name='Author', value='- Tonald "Dumpy" Drump\n- Nick "Neek0tine" Calvin')
        about.add_field(name='Complain to this guy', value='https://github.com/Neek0tine')
        about.add_field(name='Where should I bagogo',
                        value='https://discord.com/api/oauth2/authorize?client_id=722109072295591968&permissions=140328299584&scope=bot',
                        inline=False)
        detail = discord.Embed(title='Dumbot - Discord Bot',
                               description='https://github.com/Neek0tine/dumbot',
                               colour=discord.Color.purple())
        detail.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        detail.set_thumbnail(
            url='https://pbs.twimg.com/profile_images/689189555765784576/3wgIDj3j_400x400.png')
        detail.add_field(name='Running on Python 3.9.x', value='Windows / Linux')
        detail.add_field(name='Built using Pycharm 2020.2.1', value='Commercial, Freemium (open source parts are under Apache License)')
        detail.add_field(name='Hosted on Heroku', value='US-EAST-1 Server; United States, North Virginia.')

        if arg == 'n':
            await ctx.send(content=None, embed=about)
        elif arg == '-v':
            await ctx.send(content=None, embed=about)
            await ctx.send(content=None, embed=detail)

    @commands.command(aliases=["h", "help"])
    async def command_list(self, ctx):
        embed = discord.Embed(title="fuccin **r e a d**", description="im basically a hentai bot ngl. ",
                              color=discord.Color.purple())
        embed.add_field(name='`invite`', value='My invitation link', inline=False)
        embed.add_field(name='`about`', value='Self explanatory. use -v arg for full info', inline=False)
        embed.add_field(name='`nickfix`', value='Change everyone\'s nick to their default', inline=False)
        embed.add_field(name='`nuke <optional: 6-digit>`', value='Fetch info about doujin, but r a n d o m (or not)', inline=False)
        embed.add_field(name='`sauce <img attachment/img url>`', value='Guessing the sauce of attached image', inline=False)
        embed.add_field(name='`preview <6-digit>`', value='Literally nhentai viewer',
                        inline=False)

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
