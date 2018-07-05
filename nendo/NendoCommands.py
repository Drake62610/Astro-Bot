import discord
from discord.ext import commands

import asyncio
from nendo import tumblrpy
import requests
import logging

class NendoCommands():

    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger('AstroLog')

    @commands.command()
    async def nendo(self):
        announce = tumblrpy.run()
        for nendo in announce:
            url = nendo[0]
            tmp = nendo[1] + ' ' + nendo[2]
            img_data = requests.get(url).content
            with open('nendo/cache.jpg', 'wb') as handler:
                handler.write(img_data)
            with open('nendo/cache.jpg', 'rb') as f:
                self.logger.debug(tmp)
                await self.bot.send_message(self.bot.get_channel('178652769891123200'), tmp)
                await self.bot.send_file(self.bot.get_channel('178652769891123200'), f)

def setup(bot):
    bot.add_cog(NendoCommands(bot))

logger = logging.getLogger('AstroLog')

#Method used for background task
async def check_nendo(bot):
    await bot.wait_until_ready()
    logger.info('Background task check_nendo operative')
    while not bot.is_closed:
        self.logger.info('Executing check_nendo')
        announce = tumblrpy.run()
        for nendo in announce:
            url = nendo[0]
            tmp = nendo[1] + ' ' + nendo[2]
            img_data = requests.get(url).content
            with open('nendo/cache.jpg', 'wb') as handler:
                handler.write(img_data)
            with open('nendo/cache.jpg', 'rb') as f:
                await bot.send_message(bot.get_channel('178532977901305857'), tmp)
                await bot.send_file(bot.get_channel('178532977901305857'), f)
        await asyncio.sleep(60*60) #wait one minute
