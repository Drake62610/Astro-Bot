import discord
from discord.ext import commands
import logging

class AdminCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger('AstroLog')


def setup(bot):
    bot.add_cog(AdminCommands(bot))
logger = logging.getLogger('AstroLog')

