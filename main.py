# MATTE Florian

# DATE 18/10/17
# Version V1.0
# Astro Bot

# Library
# -------------------
import discord
from discord.ext import commands
from keys import *
from nyaa import nyaaCommands

# Connect
bot = commands.Bot(command_prefix='!', description='Astro Bot pour vous servir')
bot.remove_command("help")


@bot.event
async def on_ready():
    print('Logged in as')

    await bot.change_presence(game=discord.Game(name='Waifu Fight - Tentacle School Life Edition'))
    print(bot.user.name)


# Start
bot.loop.create_task(nyaaCommands.check_nya())
print(main_key)
bot.run(main_key)
print("done")
