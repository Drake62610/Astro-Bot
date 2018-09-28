import discord
from discord.ext import commands
import logging
import requests

from random import randint
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://graphql.anilist.co'

class AnimeCommands():
    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger('AstroLog')

    @commands.command()
    async def randomANL(self):
         #First Query to obtain number of pages
        query = '''
        {
          Page(page:1,perPage:1){
            media(type:ANIME){
              id
            }
            pageInfo{
              lastPage
            }
          }
        }
        '''
        variables = {}
        response = requests.post(url, json={'query': query, 'variables' : variables})
        pages = response.json()['data']['Page']['pageInfo']['lastPage']

        #Get a random page
        random = randint(0, pages)

        #Second query to obtain random anime
        query = '''
        query($random:Int){
         Page(page:$random, perPage:1){
          media(type:ANIME){
            title{
              romaji
            }
          }
        }
        }
        '''
        variables = {'random' : random}
        response = requests.post(url, json={'query': query, 'variables': variables})
        await self.bot.say(response.json()['data']['Page']['media'][0]['title']['romaji'])

def setup(bot):
    bot.add_cog(AnimeCommands(bot))

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
