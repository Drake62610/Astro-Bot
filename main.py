# MATTE Florian

# DATE 18/10/17
# Version V1.0
# Astro Bot

# Library
# -------------------
import discord
import logging
from logging.handlers import RotatingFileHandler
from discord.ext import commands
from keys import *

startup_extensions = ['events.Events',
                      'nendo.NendoCommands',
#                      'fgo.FgoCommands',
                      'misc.MiscCommands',
                      'anilist.AnimeCommands',
                      'SCP807.ScpCommands']

# Logger
logger = logging.getLogger('AstroLog')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')

file_handler = RotatingFileHandler('activity.log', 'a', 1000000, 1)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

steam_handler = logging.StreamHandler()
steam_handler.setLevel(logging.DEBUG)
logger.addHandler(steam_handler)

# Connect
bot = commands.Bot(command_prefix='!', description='Astro Bot pour vous servir')
bot.remove_command("help")

#Main Commands
@bot.command()
async def load(extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))

@bot.command()
async def unload(extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name))


if __name__ == "__main__":
    logger.info('Starting Astro Bot ...')
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
            logger.info('Extension ' + extension + ' has been loaded.')
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            logger.warning('Failed to load extension {}\n{}'.format(extension, exc))

    # Background task
    from nyaa import nyaaCommands
    bot.loop.create_task(nyaaCommands.check_nya(bot))
    from nendo import NendoCommands
    #bot.loop.create_task(NendoCommands.check_nendo(bot))
    # Start
    bot.run(main_key)
