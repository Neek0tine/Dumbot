import asyncio
import random
from collections import namedtuple
from enum import Enum, unique
from typing import List
from urllib.parse import urljoin
import requests
from discord.ext import commands
from discord import Embed


@unique
class Extension(Enum):
    JPG = 'j'
    PNG = 'p'
    GIF = 'g'


class Doujin:
    """
    Class representing a doujin.
    :ivar int id:			Doujin id.
    :ivar dict titles:		Doujin titles (language:title).
    :ivar Doujin.Tag tags:	Doujin tag list.
    :ivar str cover:		Doujin cover image url.
    :ivar str thumbnail:	Doujin thumbnail image url.
    """
    Tag = namedtuple("Tag", ["id", "type", "name", "url", "count"])
    Pages = namedtuple("Page", ["url", "width", "height"])

    def __init__(self, data):
        self.id = int(data["id"])
        self.media_id = int(data["media_id"])
        self.titles = data["title"]
        self.favorites = int(data["num_favorites"])
        self.url = f"https://nhentai.net/g/{self.id}"
        images = data["images"]

        self.pages = [Doujin.__makepage__(self.media_id, num, **_) for num, _ in enumerate(images["pages"], start=1)]
        self.tags = [Doujin.__maketag__(tag_data) for tag_data in data["tags"]]

        thumb_ext = Extension(images["thumbnail"]["t"]).name.lower()
        self.thumbnail = f"https://t.nhentai.net/galleries/{self.media_id}/thumb.{thumb_ext}"

        cover_ext = Extension(images["cover"]["t"]).name.lower()
        self.cover = f"https://t.nhentai.net/galleries/{self.media_id}/cover.{cover_ext}"

    def __getitem__(self, key: int):
        """
        Returns a page by index.
        :rtype: Doujin.Page
        """
        return self.pages[key]

    def __maketag__(tag_data: dict):
        return Doujin.Tag(
            id=int(tag_data['id']),
            type=tag_data['type'],
            name=tag_data['name'],
            url=tag_data['url'],
            count=int(tag_data['count'])
        )

    def __makepage__(media_id: int, num: int, t: str, w: int, h: int):
        return Doujin.Pages(
            f"https://i.nhentai.net/galleries/{media_id}/{num}.{Extension(t).name.lower()}",
            int(w),
            int(h)
        )


_SESSION = requests.Session()
proxies = {'http': 'http://118.127.99.93:53281'}
_SESSION.proxies.update(proxies)


def _get(endpoint, params={}) -> dict:
    return _SESSION.get(urljoin("https://nhentai.net/api/", endpoint), params=params, proxies=proxies).json()


def search(query: str, page: int = 1, sort_by: str = "date") -> List[Doujin]:
    """
    sSearch doujins by keyword.
    :param str query: Search term. (https://nhentai.net/info/)
    :param int page: Page number. Defaults to 1.
    :param str sort_by: Method to sort search results by (popular/date). Defaults to date.
    :returns list[Doujin]: Search results parsed into a list of nHentaiDoujin objects
    """
    galleries = _get('galleries/search', {"query": query, "page": page, "sort": sort_by})["result"]
    return [Doujin(search_result) for search_result in galleries]


def search_tagged(tag_id: int, page: int = 1, sort_by: str = "date") -> List[Doujin]:
    """
    Search doujins by tag id.
    :param int tag_id: Tag id to use.
    :param int page: Page number. Defaults to 1.
    :param str sort_by: Method to sort search results by (popular/date). Defaults to date.
    :returns list[Doujin]: Search results parsed into a list of nHentaiDoujin objects
    """
    try:
        galleries = _get('galleries/tagged', {"tag_id": tag_id, "page": page, "sort": sort_by})["result"]
    except KeyError:
        raise ValueError("There's no tag with the given tag_id.")

    return [Doujin(search_result) for search_result in galleries]


def get_homepage(page: int = 1) -> List[Doujin]:
    """
    Get recently uploaded doujins from the homepage.
    :param int page: Page number. Defaults to 1.
    :returns list[Doujin]: Search results parsed into a list of nHentaiDoujin objects
    """
    return [Doujin(recent) for recent in _get('galleries/all', {"page": page})["result"]]


def get_doujin(id: int) -> Doujin:
    """
    Get a doujin by its id.
    :param int id: A doujin's id.
    :rtype: Doujin
    """
    try:
        return Doujin(_get(f"gallery/{id}"))
    except KeyError:
        raise ValueError("A doujin with the given id wasn't found")


def get_random_id() -> int:
    """
    Get an id of a random doujin.
    :returns int: A random existing doujin id.
    """
    redirect = _SESSION.head("https://nhentai.net/random/").headers["Location"]
    return int(redirect[3:-1])


class NukegenCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nuke(self, ctx):
        await ctx.trigger_typing()

        _random = ''
        _img = ''

        try:
            _random = get_doujin(random.randint(0, 400000))
            _img = _random.cover
        except Exception as e:
            await ctx.channel.send(e)
            await asyncio.sleep(1)
            await ctx.channel.send("Lmao forward this to that fucking nerd.")
            await asyncio.sleep(2)
            await ctx.channel.send("Meanwhile, enjoy this")
            await ctx.channel.send(f"https://nhentai.net/g/{random.randint(0, 4000)}")

        await asyncio.sleep(1)

        _random = get_doujin(random.randint(0, 400000))
        _img = _random.cover

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
            _parody = str(info['parody']).title()
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
            _tag = [tag.title() for tag in info['tag']]
            _tag = ", ".join(_tag)
        except Exception:
            _tag = 'None'

        _nhen = Embed(title=_random.titles['english'], description='Here you go, you degenerate', color=0x87CEEB)
        _nhen.set_thumbnail(url=_img)
        _nhen.add_field(name="Info", value=f"Parody: {_parody}\n"
                                           f"Artist: {_artist}\n"
                                           f"Group: {_group}\n"
                                           f"Language: {_language}\n"
                                           f"Characters: {_character}\n"
                                           f"Category: {_category}")

        _nhen.add_field(name=f"Sauce: {_random.id}", value=_random.url)
        _nhen.add_field(name="Tags", value=_tag, inline=False)

        await ctx.channel.send(embed=_nhen)


def setup(bot):
    bot.add_cog(NukegenCog(bot))
