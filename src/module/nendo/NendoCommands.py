import discord
from discord.ext import commands

import asyncio
from src.module.nendo import tumblrpy
import requests
import logging

class NendoCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger('AstroLog')

    @commands.command()
    async def nendo(self, ctx):
        announce = tumblrpy.run()
        for nendo in announce:
            url = nendo[0]
            tmp = nendo[1] + ' ' + nendo[2]
            img_data = requests.get(url).content
            with open('nendo/cache.jpg', 'wb') as handler:
                handler.write(img_data)
            with open('nendo/cache.jpg', 'rb') as f:
                self.logger.debug(tmp)
                ch = self.bot.get_channel(571792395428036608)
                await ch.send(tmp, file=discord.File('nendo/cache.jpg'))

def setup(bot):
    bot.add_cog(NendoCommands(bot))
logger = logging.getLogger('AstroLog')

#Method used for background task
async def check_nendo(bot):
    await bot.wait_until_ready()
    logger.info('Background task check_nendo operative')
    while not bot.is_closed():
        logger.info('Executing check_nendo')
        announce = tumblrpy.run()
        for nendo in announce:
            url = nendo[0]
            tmp = nendo[1] + ' ' + nendo[2]
            img_data = requests.get(url).content
            with open('nendo/cache.jpg', 'wb') as handler:
                handler.write(img_data)
            with open('nendo/cache.jpg', 'rb') as f:
                ch = client.get_channel(571792395428036608)
                await ch.send(tmp, file=discord.File(f))
        await asyncio.sleep(60*60) #wait one minute
