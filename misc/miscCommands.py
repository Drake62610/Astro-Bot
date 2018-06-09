import asyncio
from main import bot
import recastai
import discord


@bot.event
async def on_message(message):
    await bot.process_commands(message)

    # RECAST
    if (str(message.channel) == "bot"):
        if not str(message.author) == "Astro Bot#9191" and not message.content[0] == "!":
            client = recastai.Client('9d1a465da0eeabc77ea479fe567c6202')
            response = client.request.converse_text(str(message.content))
            await bot.send_message(message.channel, response.reply)

    # OTHER
    if (message.content.startswith('Aurevoir Astro Bot') or message.content.startswith('Sayonara Astro Bot')):
        await bot.send_message(message.channel, "Aurevoir " + str(message.author).split('#')[0] + " !")

    if message.content.startswith('add joke'):
        file = open("blague.txt", "a")
        if (str(message.author) == "Σωιτε Λιτε#0138"):
            message.author = "Switelite#0138"
        file.write(str(message.content) + " @" + str(message.author).split('#')[0] + "\n")
        file.close
        await bot.send_message(message.channel,
                               "Ta blague a bien été ajoutée ! En attente de confirmation de l'admin pour l'implémenter dans mon répertoire")


# USELESS
@bot.command(pass_context=True)
async def help(ctx):
    await bot.send_message(await bot.start_private_message(ctx.message.author), "yo bitch")


@bot.command(pass_context=True)
async def joined_at(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author

    await bot.say('{0} joined at {0.joined_at}'.format(member))


@bot.command()
async def hello():
    print("coucou")
    await bot.say("Bip Boop (Hello World !)")


@bot.command(pass_context=True)
async def idchannel(ctx, arg):
    id = [channel for channel in bot.get_all_channels() if channel.name == arg][0]
    await bot.say("L\' id du channel " + arg + " est : " + id)


# AUTRES
@bot.command()
async def planninganime():
    with open('planning.png', 'rb') as f:
        await bot.send_file(bot.get_channel('178532977901305857'), f)
