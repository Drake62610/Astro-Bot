# MATTE Florian

# DATE 18/10/17
# Version V1.0
# Astro Bot

# Library
# -------------------
import discord
from discord.ext import commands
from keys import *

startup_extensions = ['events.Events','nendo.NendoCommands','fgo.FgoCommands','misc.MiscCommands']

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
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    # Start
    from nyaa import nyaaCommands
    bot.loop.create_task(nyaaCommands.check_nya(bot))
    bot.run(main_key)
