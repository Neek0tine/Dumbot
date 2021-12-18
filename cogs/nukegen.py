import asyncio
import random
from NHentai import NHentai
from discord.ext import commands
from discord import Embed


class NukegenCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nuke(self, ctx):
        await ctx.trigger_typing()
        await asyncio.sleep(1)
        _hen = NHentai()
        _random = _hen.get_random()
        _img = _random.cover.src
        _parody = []
        _artists = ''
        try:
            _parody = str((list(_random.parodies)[0]).name).title()
            _artists = str((list(_random.artists)[0]).name).title()

        except IndexError:
            _parody = "Original"
            _artists = "None (Probably in title)"

        _nametags = []
        try:
            _tags = _random.tags
            for index, tag in enumerate(_tags):
                n = str(_tags[index].name)
                n = n.title()
                _nametags.append(n)
        except IndexError:
            _nametags = "None"
        _nametags = ', '.join(_nametags)

        _nhen = Embed(title=_random.title.english, color=0x87CEEB)
        _nhen.set_thumbnail(url=_img)
        _nhen.add_field(name="Info", value=f"Parodies: {_parody}\nArtist: {_artists}\n Pages: {_random.total_pages} ")
        _nhen.add_field(name=f"Sauce: {_random.id}", value=_random.url)
        _nhen.add_field(name="Tags", value=_nametags, inline=False)

        await ctx.channel.send(embed=_nhen)

# The setup function below is necessary. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.


def setup(bot):
    bot.add_cog(NukegenCog(bot))
