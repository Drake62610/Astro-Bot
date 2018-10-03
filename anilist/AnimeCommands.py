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
    async def randomANL(self,*nums):
        link = ""
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
        title = response.json()['data']['Page']['media'][0]['title']['romaji']
        #Last query to get anime information
        media = searchANL(title)[0] #Get first result
        print(media)
        genre = media['genres']
        strGenre = ''
        for i in genre:
            strGenre = strGenre + ' ' + i
        tag = media['tags']
        strTag = ''
        for i in tag:
            strTag = strTag + ' ' + i['name']
        link = "https://anilist.co/anime/" + str(media['id'])
        # if("-a" in nums):
        #     pass
        # else:
        #     if("-l" in nums):
        #
        #     if("-i" in nums):
        #         pass
        await self.bot.say("Vous avez tiré : " +
                           "\n**__Titre :__** "     + title +
                           "\n**__Genre(s) :__** " + strGenre +
                           "\n**__Tag(s) :__** " + strTag +
                           "\n" + link
                          )

    @commands.command()
    async def searchANL(self,name,type="ANIME"):
        resp = searchANL(name,type)[0]
        title = resp['title']['romaji']
        link = "https://anilist.co/"+ type.lower() + "/" + str(resp['id'])
        print(resp)
        await self.bot.say(title + "\n" + link)

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

#Get 3 first anime of a search query in anilist
#Return tab of anime
def searchANL(name,type="ANIME"):
    query = '''
    query ($id: Int, $page: Int, $perPage: Int, $search: String, $type: MediaType) {
      Page(page: $page, perPage: $perPage) {
        pageInfo {
          total
          currentPage
          lastPage
          hasNextPage
          perPage
        }
        media(id: $id, search: $search, type:$type) {
          id
          title {
            romaji
          }
          type
          episodes
          coverImage {
            large
          }
          trailer {
            id
            site
          }
          genres
          averageScore
          tags {
            name
          }
        }
      }
    }
    '''
    variables = {
        'search': name,
        "type": type,
        'page': 1,
        'perPage': 3
    }
    url = 'https://graphql.anilist.co'
    response = requests.post(url, json={'query': query, 'variables': variables})
    return response.json()['data']['Page']['media']
