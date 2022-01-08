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

        async def _nuke(_arg):
            _random = ''
            _img = ''

            async def again(_arg):
                try:
                    _random = nhentai.get_doujin(_arg)
                    _img = _random.cover
                    return _random, _img
                except Exception as e:
                    # await ctx.channel.send(e)
                    # await asyncio.sleep(1)
                    # await ctx.channel.send(f'{random.choice(errors)} <@256713166149386240> {e}')
                    # await asyncio.sleep(2)
                    await again(random.randint(0, 400000))

            _random, _img = await again(_arg)

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
                _tag = [str(f'[{tag.title()}](https://nhentai.net/tags/{str(tag).replace(" ", "-")})') for tag in
                        info['tag']]
                _tag = ", ".join(_tag)
                _tag = (_tag[:1000] + '..') if len(_tag) > 1000 else _tag
            except Exception:
                _tag = 'None'

            _nhen = Embed(title=_random.titles['english'], description='Here you go, you degenerate', color=0x87CEEB)
            _nhen.set_thumbnail(url=_img)
            _nhen.add_field(name="Info",
                            value=f"Parody : {_parody}\nArtist  : {_artist}\nGroup   : {_group}\nLanguage  : "
                                  f"{_language}\nCharacters   : {_character}\nCategory    : {_category}")

            # _nhen.add_field(name="** **", value=f": {_parody}\n: {_artist}\n: {_group}\n: {_language}\n: {
            # _character}\n: {_category}", inline=True)

            _nhen.add_field(name=f"Sauce", value=f'**{_random.id}**', inline=False)
            _nhen.add_field(name="Tags", value=_tag, inline=False)

            return _nhen, _random.id

        #
        # _invoke_view = [[Button(label='Source', url=f'https://nhentai.net/g/{_random.id}', style=ButtonStyle.url),
        #                 Button(label='Preview', custom_id='prev', style=ButtonStyle.green),
        #                 Button(label='Randomize', custom_id='rand', style=ButtonStyle.blurple)]]

        # _nukegen = await ctx.send(embed=_nhen, components=_invoke_view)

        _link = ''
        _em, _link = await _nuke(arg)
        _nukegen = await ctx.send(embed=_em)
        await ctx.message.delete()

        _prev = '🔎'
        _rand = '🎲'
        _pin = '📌'
        _close = '❌'

        await _nukegen.add_reaction(_prev)
        await _nukegen.add_reaction(_rand)
        await _nukegen.add_reaction(_pin)
        await _nukegen.add_reaction(_close)

        _guide = await ctx.send("🔎 Read  |  🎲 Randomize  |  📌 Save")

        _valid_reactions = ['🔎', '🎲', '📌', '❌']
        timeout = time.time() + 60 * 2  # 5 minutes from now

        while True:

            if time.time() > timeout:
                await ctx.send('Ah i forgot the link, you took too long')
                break

            def check_react(reaction, user):
                return user == ctx.author and str(reaction.emoji) in _valid_reactions

            reaction, user = await self.bot.wait_for('reaction_add', check=check_react)

            timeout = time.time() + 60 * 2  # 5 minutes from now
            if str(reaction.emoji) == _prev:
                await _nukegen.remove_reaction(_prev, user)
                await _nukegen.delete()
                await _guide.delete()
                await ctx.invoke(self.bot.get_command('preview'), arg=_link)

            elif str(reaction.emoji) == _close:
                await _nukegen.delete()
                await _guide.delete()

            elif str(reaction.emoji) == _rand:
                await _nukegen.remove_reaction(_rand, user)
                while True:
                    try:
                        _em, _link = await _nuke(random.randint(0, 400000))
                        await _nukegen.edit(embed=_em)
                        break
                    except:
                        pass

            elif str(reaction.emoji) == _pin:
                async for user in reaction.users():
                    await _nukegen.remove_reaction(_pin, user)
                    await user.send(f'https://nhentai.net/g/{_link}')

            else:
                await ctx.send('How the fuck did you get here?')


def setup(bot):
    bot.add_cog(NukegenCog(bot))
