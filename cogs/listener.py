import math
import random
import asyncio
import discord
from realtype import realtype
from responses import boo, shutdowns, cumzone
from discord.ext import commands


class ListenerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        msg = message.content
        msg = msg.casefold()
        drop = random.randint(0, 100)
        timer = 1.3

        if 'cum' in msg:
            print(f'[+] Cum message detected! msg : <{msg}>, timer : <{timer}s>')
            _cum = random.choice(cumzone)
            _time = realtype(_cum)
            await asyncio.sleep(_time)
            async with message.channel.typing():
                await message.channel.send(_cum)

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

        elif 'epic' in msg and message.author.name != 'Dumbot':
            print(f'\r[+] Epic message detected! msg : <{msg}>, timer : <{timer}s> ', end="")
            await asyncio.sleep(timer)
            async with message.channel.typing():
                await message.channel.send("fucking еpic")

        elif drop < 25:
            print('[+] Drop chance passed')
            if 'fuck' in msg and message.author.name != 'Dumbot':
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

            elif 'retard' in msg:
                choice = random.choice(boo)
                print(f'[+] fuck yeah message detected! msg : <{msg}>, timer : <{timer}s>, response : <{choice}> ')
                await asyncio.sleep(timer)
                async with message.channel.typing():
                    await message.channel.send(choice)

            elif 'bitch' in msg:
                choice = random.choice(boo)
                print(
                    f'[+] fuck yeah message detected! msg : msg : <{msg}>, timer : <{timer}s>, response : <{choice}> ')
                await asyncio.sleep(timer)
                async with message.channel.typing():
                    await message.channel.send(choice)

            elif 'idiot' in msg:
                choice = random.choice(boo)
                print(
                    f'[+] fuck yeah message detected! msg : msg : <{msg}>, timer : <{timer}s>, response : <{choice}> ')
                await asyncio.sleep(timer)
                async with message.channel.typing():
                    await message.channel.send(choice)

            elif 'dumbass' in msg:
                choice = random.choice(boo)
                print(
                    f'[+] fuck yeah message detected! msg : msg : <{msg}>, timer : <{timer}s>, response : <{choice}> ')
                await asyncio.sleep(timer)
                async with message.channel.typing():
                    await message.channel.send(choice)

            elif '@!722109072295591968' in msg:

                await asyncio.sleep(random.randint(0, 4))
                decide = random.choice([True, False])
                async with message.channel.typing():
                    if decide:
                        _shutdown = random.choice(shutdowns)
                        await asyncio.wait(realtype(_shutdown))
                        await message.channel.send(f'{_shutdown}  {message.author.mention}')
                    else:
                        _shutdown = random.choice(shutdowns)
                        await asyncio.wait(realtype(_shutdown))
                        await message.channel.send(random.choice(_shutdown))

            elif 'ba' or 'bu' or 'gu' or 'go' or 'bo' in msg:
                bagogo_counter = 0
                for index in range(0, len(msg)):
                    _set = [msg[index: index + 2]]
                    msg = "".join(_set)
                    if 'ba' in msg:
                        bagogo_counter += 1
                    elif 'bu' in msg:
                        bagogo_counter += 1
                    elif 'gu' in msg:
                        bagogo_counter += 1
                    elif 'go' in msg:
                        bagogo_counter += 1
                    elif 'bo' in msg:
                        bagogo_counter += 1

                if bagogo_counter == 0:
                    return
                else:
                    print('[+] Bogayon message detected!', msg)
                    print(f'[+] Bogayon trigger count: {bagogo_counter}')

                try:
                    chance = min([random.randint(1, 50) for _ in range(bagogo_counter)])
                    print(f'[+] Bogayon minimal roll: {chance}')
                except:
                    return

                if chance < 15:

                    _first_set = ['b', 'g']
                    _second_set = ['a', 'o', 'i', 'u']
                    _bogayon = []

                    while len(_bogayon) < random.randint(2, 6):
                        _complete_set = str(random.choice(_first_set) + random.choice(_second_set))
                        _bogayon.append(_complete_set)
                    _bogayon = str("".join(_bogayon)).capitalize()
                    print(f'[+] Gacha passed, generating {_bogayon}')

                    await message.channel.send(_bogayon)

                else:
                    return
            else:
                print(f'[+] Trigger message detected with drop: {drop}')


def setup(bot):
    bot.add_cog(ListenerCog(bot))
