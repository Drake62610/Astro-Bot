from nyaa import nyaaRSS
import asyncio
import logging
from main import bot

logger = logging.getLogger('AstroLog')

async def check_nya(bot):
    await bot.wait_until_ready()
    channel = [channel for channel in bot.get_all_channels() if channel.name == 'bot'][0]
    logger.info('Background task check_nya operative')
    while not bot.is_closed:
        announce = nyaaRSS.run()
        if announce:
            for post in announce:
                message = (
                    '@everyone\n Le torrent : \n```' + post.title + "``` vient de sortir ! Vous pouvez le télécharger ici : \n " +
                    post.description.split('<a href=\"')[1].split('\">')[0])
                await bot.send_message(channel, message)
        await asyncio.sleep(60)
