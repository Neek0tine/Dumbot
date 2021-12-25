from saucenao_api import SauceNao
from responses import sauce_respo, errors
from discord.ext import commands
from random import choice
from os import getenv
import requests
import asyncio
import discord


class SauceCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sauce(self, ctx, arg=None):
        print('[+] Sauce command detected!')
        _sauce_api = ''
        _results = ''
        _img_url = ''
        _suffixes = ('.png', '.jpg', '.jpeg', '.jfif')

        if str(arg).endswith(_suffixes):
            try:
                _url_check = requests.get(arg)
                _img_url = arg
            except requests.ConnectionError as e:
                await ctx.channel.send('is that an url?')
                print(f'[!] Something went wrong, on acquiring argument {e}')

        elif len(str(arg).split(sep='?')) == 2:
            try:
                if str((str(arg).split(sep='?'))[0]).endswith(_suffixes):
                    _img_url = str((str(arg).split(sep='?'))[0])
                else:
                    await ctx.channel.send('Did you pasted an incomplete link?')

            except Exception as e:
                print('[!] Wtf did he sent?')
                await ctx.channel.send(f'wtf did you send? <@256713166149386240> {e}')

        else:
            try:
                _img_url = ctx.message.attachments[0].url
            except Exception as e:
                print(f'[!] Wrong image. {e}')
                await ctx.channel.send('pretty sure it isnt an image')
                return

        await ctx.channel.trigger_typing()
        await asyncio.sleep(7)
        await ctx.channel.send(choice(sauce_respo))

        await ctx.channel.trigger_typing()
        await asyncio.sleep(6)

        try:
            _sauce_api = SauceNao(getenv('sauce_api'))
            _results = _sauce_api.from_url(_img_url)
        except Exception as e:
            print(f'[!] Something went wrong, probably rate limited. Again {e}')
            await ctx.channel.send(f'{choice(errors)} <@256713166149386240> {e}')

        _best = _results[0]
        _title = _best.title
        _author = _best.author
        _thumbnail = _best.thumbnail
        _score = _best.similarity

        _url = _best.urls
        _url = [str(f'({str(url).replace(" ", "-")})') for url in _best.urls]
        _url = ", ".join(_url)

        _confidence = ''
        print(f'[+] Result:{_title}, {_author}, {_score}, {_url}, {_thumbnail}')

        if _score < 25:
            _confidence = "idk never seen it, prolly manga or something"
        elif _score < 50:
            _confidence = "its probably this, but dont quote me on that"
        elif _score < 75:
            _confidence = 'yo i think i seen this one'
        else:
            _confidence = 'oh i know this'

        _sauce = discord.Embed(title=_title, description=f'Sauce found with confidence level of {_score}%',
                               color=0x87CEEB)
        _sauce.set_thumbnail(url=_thumbnail)
        _sauce.add_field(name=f"Author", value=_author, inline=True)

        if len(_url) == 0:
            await ctx.channel.send(_confidence, embed=_sauce)
        else:
            _sauce.add_field(name=f"Link", value=_url, inline=True)
            await ctx.channel.send(_confidence, embed=_sauce)


def setup(bot):
    bot.add_cog(SauceCog(bot))
