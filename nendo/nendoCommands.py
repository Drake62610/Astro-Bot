import asyncio
from main import bot
from nendo import tumblrpy
import requests

@bot.command()
async def goodsmile():
    announce = tumblrpy.run()
    for nendo in announce:
        url = nendo[0]
        tmp = nendo[1] + ' ' + nendo[2]
        img_data = requests.get(url).content
        with open('cache.jpg', 'wb') as handler:
            handler.write(img_data)
    with open('cache.jpg', 'rb') as f:
        await bot.send_message(bot.get_channel('178532977901305857'), tmp)
        await bot.send_file(bot.get_channel('178532977901305857'), f)