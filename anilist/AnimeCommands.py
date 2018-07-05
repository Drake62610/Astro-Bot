import discord
from discord.ext import commands
import logging

from random import randint
from urllib.request import urlopen
from bs4 import BeautifulSoup

MIN_ID=1
MAX_ID=11000

class AnimeCommands():
    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger('AstroLog')

    @commands.command()
    async def randomMAL(self):
        tmp=''
        animeId = getRandomId()
        url = "http://www.animenewsnetwork.com/encyclopedia/anime.php?id=%s" % str(animeId)
        html = urlopen(url)
        html = html.read()
        soup = BeautifulSoup(html, "html.parser")
        title =  soup.find("div", {"id": "page-title"}).find("h1", {"id": "page_header"}).contents[0]
        tmp += '__**' + str(title) + '**__\n\n'
        self.logger.debug(tmp)
        ratingText =  soup.find("div", {"id": "ratingbox"})
        if ratingText is None:
            tmp += 'No evalutation here'
        else:
            ratingText = ratingText.find_all('span')
            for i in ratingText:
                i = str(i)
                if 'vote' in i:
                    i = i.split('<span>')[1][1::]
                    tmp += i + '\n'
        await self.bot.say(tmp)

def setup(bot):
    bot.add_cog(AnimeCommands(bot))

def getRandomId():
  return randint(MIN_ID, MAX_ID)

# def isManga(self):
#     return "manga" in self.title
#
#   def isOneshot(self):
#     return bool(re.findall(b'(OAV)|(movie)|(special)', self.title))
#
#   def isPopular(self, threshold):
#     if not self.arithmeticMean or not self.weightedMean:
#       return False
#     return self.arithmeticMean >= threshold and self.weightedMean >= threshold
