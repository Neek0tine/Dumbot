import discord.errors
import requests
import nhentai
import asyncio
import time
from requests import get
from bs4 import BeautifulSoup
from discord.ext import commands
from discord import Embed, Color, Button, ButtonStyle, Interaction


class PreviewerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def preview(self, ctx, arg='259049', req_page=1):
        authorid = ctx.message.author.id

        _page = ''
        _dojin = ''
        _tot_page = ''

        if str(arg).startswith('http'):
            _sparg = str(arg).split(sep='/')
            print(_sparg)

            if len(_sparg) == 5:
                if _sparg[-1] == '':
                    print('[!] Are you sure it\'s the id is correct?')
                    await ctx.send('is the id correct?')
                elif _sparg[-1] != '':
                    arg = int(_sparg[-1])
                    _page = 1
                    _link = str("/".join(_sparg)) + '/' + str(_page)
                    print(arg, _link, _page)

            elif len(_sparg) == 6:
                if _sparg[-1] == '':
                    _page = 1
                    _link = str("/".join(_sparg)) + str(_page)
                else:
                    arg = int(_sparg[-2])
                    _page = _sparg[-1]
                    _link = str("/".join(_sparg))
                    print(arg, _link, _page)

            elif len(_sparg) < 5 or len(_sparg) > 7:
                print('[!] Are you sure it\'s the correct link?')

            arg = int(arg)
            _page = int(_page)
            _dojin = nhentai.get_doujin(arg)
            _tot_page = len(_dojin.pages)

        else:
            _page = req_page
            _dojin = nhentai.get_doujin(arg)
            _tot_page = len(_dojin.pages)

        def get_img(_code, _page, _url=None):
            if _url is not None:
                return str(
                    (BeautifulSoup(
                        (get(f'{_url}')).content, 'html.parser')
                    ).find_all('img', src=True)[-1]['src'])
            else:
                return str(
                    (BeautifulSoup(
                        (get(f'https://nhentai.net/g/{_code}/{_page}')).content, 'html.parser')
                    ).find_all('img', src=True)[-1]['src'])

        _view = Embed(title=f'[{arg}]{_dojin.titles["english"]} page {_page}', color=0x87CEEB)
        _view.set_image(url=get_img(arg, _page))
        try:
            await ctx.message.delete()
        except discord.errors.NotFound:
            pass

        _interactive_buttons = await ctx.send(embed=_view)

        _next_re = '▶'
        _prev_re = '◀'
        _pin = '📌'
        _close = '❌'
        _valid_reactions = ['▶', '◀', '📌', '❌']

        _guide = await ctx.send(" ◀ Previous  |  ▶ Next  |  📌 save")
        await _interactive_buttons.add_reaction('◀')
        await _interactive_buttons.add_reaction('▶')
        await _interactive_buttons.add_reaction('📌')
        await _interactive_buttons.add_reaction('❌')
        timeout = time.time() + 30  # 5 minutes from now

        # TODO: 2. Remove reaction after timeout
        # TODO: 3. Disable command if reaction still active

        while True:

            if time.time() > timeout:
                await _interactive_buttons.clear_reaction()
                break

            done_tasks = None
            check_react = lambda reaction, user: user == ctx.author and str(reaction.emoji) in _valid_reactions and user.id == authorid
            check_button = lambda interaction, button: interaction.author == ctx.author and interaction.message == _interactive_buttons

            pending_tasks = [self.bot.wait_for('button_click', check=check_button),
                             self.bot.wait_for('reaction_add', check=check_react)]

            done_tasks, pending_tasks = await asyncio.wait(pending_tasks, return_when=asyncio.FIRST_COMPLETED)

            for task in pending_tasks:
                task.cancel()

            timeout = time.time() + 60 * 2  # 5 minutes from now
            for task in done_tasks:
                reaction, user = await task
                interaction, button = await task

                if reaction and user:
                    if time.time() > timeout:
                        await ctx.send('Ah i forgot the link, you took too long')
                        break

                    elif str(reaction.emoji) == _pin:
                        await _interactive_buttons.remove_reaction('📌', user)
                        await user.send(f'https://nhentai.net/g/{arg}/{_page}')

                    elif str(reaction.emoji) == _close:
                        await _interactive_buttons.delete()
                        await _guide.delete()

                    elif _page == 1:
                        if str(reaction.emoji) == _next_re:
                            await _interactive_buttons.remove_reaction('▶', user)
                            _page += 1
                            _view = Embed(title=f'[{arg}]{_dojin.titles["english"]} page {_page}', color=0x87CEEB)
                            _view.set_image(url=get_img(arg, _page))
                            await _interactive_buttons.edit(embed=_view)

                        else:
                            await _interactive_buttons.remove_reaction('◀', user)

                    elif _page == _tot_page:
                        if str(reaction.emoji) == _prev_re:
                            await _interactive_buttons.remove_reaction('◀', user)
                            _page -= 1
                            _view = Embed(title=f'[{arg}]{_dojin.titles["english"]} page {_page}', color=0x87CEEB)
                            _view.set_image(url=get_img(arg, _page))
                            await _interactive_buttons.edit(embed=_view)

                        else:
                            await _interactive_buttons.remove_reaction('◀', user)

                    else:
                        if str(reaction.emoji) == _prev_re:
                            await _interactive_buttons.remove_reaction('◀', user)
                            _page -= 1
                            _view = Embed(title=f'[{arg}]{_dojin.titles["english"]} page {_page}', color=0x87CEEB)
                            _view.set_image(url=get_img(arg, _page))
                            await _interactive_buttons.edit(embed=_view)

                        elif str(reaction.emoji) == _next_re:
                            await _interactive_buttons.remove_reaction('▶', user)
                            _page += 1
                            _view = Embed(title=f'[{arg}]{_dojin.titles["english"]} page {_page}', color=0x87CEEB)
                            _view.set_image(url=get_img(arg, _page))
                            await _interactive_buttons.edit(embed=_view)
                else:
                    ctx.send('How did you get here?')


def setup(bot):
    bot.add_cog(PreviewerCog(bot))
