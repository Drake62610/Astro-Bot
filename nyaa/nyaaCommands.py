from nyaa import nyaaRSS
import asyncio
from main import bot


async def check_nya():
    await bot.wait_until_ready()
    channel = [channel for channel in bot.get_all_channels() if channel.name == 'bot'][0]
    while not bot.is_closed:
        announce = nyaaRSS.run()
        if announce:
            for post in announce:
                message = (
                    '@everyone\n Le torrent : \n```' + post.title + "``` vient de sortir ! Vous pouvez le télécharger ici : \n " +
                    post.description.split('<a href=\"')[1].split('\">')[0])
                await bot.send_message(channel, message)
        await asyncio.sleep(60)
