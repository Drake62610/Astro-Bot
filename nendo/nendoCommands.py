import discord
from discord.ext import commands

import asyncio
from nendo import tumblrpy
import requests

class NendoCommands():

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def goodsmile(self):
        announce = tumblrpy.run()
        print(announce)
        for nendo in announce:
            url = nendo[0]
            tmp = nendo[1] + ' ' + nendo[2]
            img_data = requests.get(url).content
            with open('nendo/cache.jpg', 'wb') as handler:
                handler.write(img_data)
        with open('nendo/cache.jpg', 'rb') as f:
            await self.bot.send_message(self.bot.get_channel('178532977901305857'), tmp)
            await self.bot.send_file(self.bot.get_channel('178532977901305857'), f)

    @commands.command()
    async def loop(self):
        print('started')
        self.bot.loop.create_task(check_nya(bot))

def setup(bot):
    bot.add_cog(NendoCommands(bot))
