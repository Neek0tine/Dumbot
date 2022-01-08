from collections import namedtuple
from urllib.parse import urljoin
from discord.ext import commands
from discord import Embed, Color, Button, ButtonStyle, Interaction
from enum import Enum, unique
from discord import Embed
from typing import List
from responses import errors
import nhentai
import requests
import discord
import asyncio
import random
import time


class NukegenCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nuke(self, ctx, arg=random.randint(0, 400000)):
        await ctx.trigger_typing()

        _random = ''
        _img = ''

        try:
            _random = nhentai.get_doujin(arg)
            _img = _random.cover
        except Exception as e:
            await ctx.channel.send(e)
            await asyncio.sleep(1)
            await ctx.channel.send(f'{choice(errors)} <@256713166149386240> {e}')
            await asyncio.sleep(2)
            await ctx.channel.send("Meanwhile, enjoy this")
            await ctx.channel.send(f"https://nhentai.net/g/{random.randint(0, 4000)}")

        print(f'[+] Nuke command launched! Gathered ID: {_random.id}')

        info = dict()
        for tags in enumerate(_random.tags):

            if tags[1].type in info:
                # append the new number to the existing array at this slot
                info[tags[1].type].append(tags[1].name)
            else:
                # create a new array in this slot
                info[tags[1].type] = [tags[1].name]

        _group = 'None'
        _language = ''
        _artist = ''
        _character = ''
        _tag = ''
        _parody = ''
        _category = ''

        try:
            _group = [group.title() for group in info['group']]
            _group = ", ".join(_group)
        except Exception:
            _group = 'None'

        try:
            _parody = str("".join(info['parody'])).title()
        except Exception:
            _parody = 'Original'

        try:
            _character = [character.title() for character in info['character']]
            _character = ", ".join(_character)
        except Exception:
            _character = 'Original'

        try:
            _artist = [artist.title() for artist in info['artist']]
            _artist = ", ".join(_artist)
        except Exception:
            _artist = 'Unknown'

        try:
            _language = [language.title() for language in info['language']]
            _language = ", ".join(_language)
        except Exception:
            _language = 'Unknown'

        try:
            _category = [category.title() for category in info['category']]
            _category = ", ".join(_category)
        except Exception:
            _category = 'Hentai'

        try:
            _tag = [str(f'[{tag.title()}](https://nhentai.net/tags/{str(tag).replace(" ", "-")})') for tag in info['tag']]
            _tag = ", ".join(_tag)
            _tag = (_tag[:1000] + '..') if len(_tag) > 1000 else _tag
        except Exception:
            _tag = 'None'

        _nhen = Embed(title=_random.titles['english'], description='Here you go, you degenerate', color=0x87CEEB)
        _nhen.set_thumbnail(url=_img)
        _nhen.add_field(name="Info", value=f"Parody : {_parody}\nArtist  : {_artist}\nGroup   : {_group}\nLanguage  : {_language}\nCharacters   : {_character}\nCategory    : {_category}")
        # _nhen.add_field(name="** **", value=f": {_parody}\n: {_artist}\n: {_group}\n: {_language}\n: {_character}\n: {_category}", inline=True)
        _nhen.add_field(name=f"Sauce", value=f'**{_random.id}**', inline=False)
        _nhen.add_field(name="Tags", value=_tag, inline=False)

        _invoke_view = [[Button(label='Source', url=f'https://nhentai.net/g/{_random.id}', style=ButtonStyle.url),
                        Button(label='Preview', custom_id='prev', style=ButtonStyle.green)]]

        _nukegen = await ctx.send(embed=_nhen, components=_invoke_view)

        def check_button(i: Interaction, button):
            return i.author == ctx.author and i.message == _nukegen

        while True:
            timeout = time.time() + 60*2  # 5 minutes from now
            interaction, button = await self.bot.wait_for('button_click', check=check_button)

            if time.time() > timeout:
                break
            else:
                await ctx.invoke(self.bot.get_command('preview'), arg=_random.id)
                break


def setup(bot):
    bot.add_cog(NukegenCog(bot))
