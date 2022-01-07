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
    async def preview(self, ctx, arg=259049):
        _page = 1
        _dojin = nhentai.get_doujin(arg)
        _tot_page = len(_dojin.pages)

        def get_img(_code, _page):
            return str(
                (BeautifulSoup(
                    (get(f'https://nhentai.net/g/{_code}/{_page}')).content, 'html.parser')
                ).find_all('img', src=True)[-1]['src'])

        _view = Embed(title=f'{_dojin.titles["english"]} page {_page}', color=0x87CEEB)
        _view.set_image(url=get_img(arg, _page))

        _view_comp =[[Button(label='Source', url=f'https://nhentai.net/g/{arg}', style=ButtonStyle.url),
                      Button(label='Previous', custom_id='prev', style=ButtonStyle.green),
                      Button(label='Next', custom_id='next', style=ButtonStyle.green)]]

        _interactive_buttons = await ctx.send(embed=_view, components=_view_comp)

        def check_button(i: Interaction, button):
            return i.author == ctx.author and i.message == _interactive_buttons

        while True:
            timeout = time.time() + 60*2  # 5 minutes from now
            interaction, button = await self.bot.wait_for('button_click', check=check_button)

            if time.time() > timeout:
                await ctx.send('Ah i forgot the link, you took too long')
                break

            elif _page == 1:
                if button.custom_id == 'next':
                    _page += 1
                    _view = Embed(title=f'{_dojin.titles["english"]} page {_page}', color=0x87CEEB)
                    _view.set_image(url=get_img(arg, _page))
                    await interaction.edit(embed=_view)

                else:
                    await ctx.send('there\'s no page 0')

            elif _page == _tot_page:
                if button.custom_id == 'next':
                     await ctx.send('what are you trying to read? the doujin\'s over.')

                else:
                    _page += 1
                    _view = Embed(title=f'{_dojin.titles["english"]} page {_page}', color=0x87CEEB)
                    _view.set_image(url=get_img(arg, _page))
                    await interaction.edit(embed=_view)

            else:
                if button.custom_id == 'next':
                    _page += 1
                    _view = Embed(title=f'{_dojin.titles["english"]} page {_page}', color=0x87CEEB)
                    _view.set_image(url=get_img(arg, _page))
                    await interaction.edit(embed=_view)

                else:
                    _page -= 1
                    _view = Embed(title=f'{_dojin.titles["english"]} page {_page}', color=0x87CEEB)
                    _view.set_image(url=get_img(arg, _page))
                    await interaction.edit(embed=_view)



def setup(bot):
    bot.add_cog(PreviewerCog(bot))
