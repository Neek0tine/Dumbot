import math
import random
import configparser
import asyncio
from responses import cumzone
import discord
from boo import boo
from discord.ext import commands


class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        guildnum = 0
        guilds = await self.bot.fetch_guilds(limit=150).flatten()
        for _ in guilds:
            guildnum = guildnum + 1
        print(
            f'Logged in as: {self.bot.user.name}\n ID: {self.bot.user.id}\n API Version: {discord.__version__}\n Bot Version: 1.4.0\n Ruining {guildnum} guilds')

        # Changes our bots Playing Status. type=1(streaming) for a standard game you could remove type and url.
        await self.bot.change_presence(status=discord.Status.dnd, activity=(discord.Game('with my dick')))
        print(f'Successfully logged in and booted...!')
        print(
            '============================================================\n     Æughē\n============================================================')

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
        timer = random.randint(0, 6)

        try:
            print(message.author.name, "#", message.channel.name, " : ", msg, )  # Log all chat to stdout

            if 'epic' in msg and message.author.name != 'Dumbot':
                print(f'\r[+] Epic message detected! msg : <{msg}>, timer : <{timer}s> ', end="")
                await asyncio.sleep(timer)
                async with message.channel.typing():
                    await message.channel.send("fucking еpic")

            elif 'cum' in msg:
              print(f'[+] Cum message detected! msg : <{msg}>, timer : <{timer}s>')
              await asyncio.sleep(timer)
              async with message.channel.typing():
                await message.channel.send(random.choice(cumzone))
                      
            elif 'æughē' in msg and message.author.name != 'Dumbot':
              print(f'[+] [what] message detected! msg : <{msg}>, timer : <{timer}s> ')
              await asyncio.sleep(timer)
              async with message.channel.typing():
                await message.channel.send("Æughē")

            elif 'uganda' in msg and message.author.name != 'Dumbot':
                choice = random.choice(['black goes brrr', 'inflation', 'cummotion', 'haha lmao yeet'])
                print(f'[+] uganda invasion detected! msg : <{msg}>, timer : <{timer}s>, response : <{choice}> ')
                await asyncio.sleep(timer)
                async with message.channel.typing():
                    await message.channel.send(choice)

            elif 'fuck' in msg and message.author.name != 'Dumbot':
                choice = random.choice(boo)
                print(f'[+] fuck yeah message detected! msg : <{msg}>, timer : <{timer}s>, response : <{choice}> ')
                await asyncio.sleep(timer)
                async with message.channel.typing():
                    await message.channel.send(choice)
            elif 'cunt' in msg:
                choice = random.choice(boo)
                print(f'[+] fuck yeah message detected! msg : <{msg}>, timer : <{timer}s>, response : <{choice}> ')
                await asyncio.sleep(timer)
                async with message.channel.typing():
                    await message.channel.send(choice)
            elif 'bitch' in msg:
                choice = random.choice(boo)
                print(f'[+] fuck yeah message detected! msg : msg : <{msg}>, timer : <{timer}s>, response : <{choice}> ')
                await asyncio.sleep(timer)
                async with message.channel.typing():
                    await message.channel.send(choice)
            elif 'idiot' in msg:
                choice = random.choice(boo)
                print(f'[+] fuck yeah message detected! msg : msg : <{msg}>, timer : <{timer}s>, response : <{choice}> ')
                await asyncio.sleep(timer)
                async with message.channel.typing():
                    await message.channel.send(choice)
            elif 'dumbass' in msg:
                choice = random.choice(boo)
                print(f'[+] fuck yeah message detected! msg : msg : <{msg}>, timer : <{timer}s>, response : <{choice}> ')
                await asyncio.sleep(timer)
                async with message.channel.typing():
                    await message.channel.send(choice)

            elif '@!722109072295591968' in msg:
                shutdowns = ['bacot', 'kontol', 'memek', 'brisik', 'what', 'yes', 'uganda', 'Æughē', 'ngapain ping mek']
                await asyncio.sleep(random.randint(0, 4))
                decide = random.choice(['True', 'False'])
                async with message.channel.typing():
                    if decide == 'True':
                        await message.channel.send(
                            f'{random.choice(shutdowns)}  {message.author.mention}')
                    else:
                        await message.channel.send(random.choice(shutdowns))

            elif 'gu' or 'bu' or 'ga' in msg:
                if (message.author.bot) :
                    return
                else:
                    drop = int(math.floor(int(len(message.content))/2))
                    chance = []

                    for _ in range(drop):
                        roll = random.randint(1, 50)
                        chance.append(roll)

                    chance = min(chance)

                    if chance < 3:

                        def bogayongen():
                            _first_set = ['b', 'g']
                            _second_set = ['a', 'o', 'i', 'u']

                            _bogayon = []

                            while len(_bogayon) < random.randint(2, 6):
                                _complete_set = str(random.choice(_first_set) + random.choice(_second_set))
                                _bogayon.append(_complete_set)
                            _bogayon = str("".join(_bogayon)).capitalize()
                            print(f'[+] Bagogo mesage detected, generating {_bogayon}')
                            return _bogayon

                        await message.channel.send(bogayongen())

                    else:
                        return

        except AttributeError:
            print("Direct Message received!")
            print(message.author.name, "[#] Direct Channel: ", msg)


def setup(bot):
    bot.add_cog(MainCog(bot))
