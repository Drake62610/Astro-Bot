import discord
from discord.ext import commands

class AnimeCommands():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    def getAnime(animeId):
        


def setup(bot):
    bot.add_cog(AnimeCommands(bot))
