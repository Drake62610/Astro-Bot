#MATTE Florian

#DATE 18/10/17
#Version V1.0
#Astro Bot

#Library
#-------------------
import discord
import asyncio
import aiohttp
import os
import recastai
import nyaaRSS
import tumblrpy
import requests
import fgoroll
from discord.ext import commands
from datetime import date
from keys import *

#Connect
bot = commands.Bot(command_prefix='!', description='Astro Bot pour vous servir')
bot.remove_command("help")
#event
#-------------------
@bot.event
async def on_ready():
    print('Logged in as')

    await bot.change_presence(game=discord.Game(name='Waifu Fight - Tentacle School Life Edition'))
    print(bot.user.name)

@bot.event
async def on_message(message):
    await bot.process_commands(message)

    #RECAST
    if (str(message.channel) == "bot"):
        if not str(message.author)=="Astro Bot#9191" and not message.content[0]=="!" :
            client = recastai.Client('9d1a465da0eeabc77ea479fe567c6202')
            response = client.request.converse_text(str(message.content))
            await bot.send_message(message.channel, response.reply)

    #OTHER
    if (message.content.startswith('Aurevoir Astro Bot') or message.content.startswith('Sayonara Astro Bot')) :
        await bot.send_message(message.channel, "Aurevoir " + str(message.author).split('#')[0] + " !")

    if message.content.startswith('add joke'):
        file = open("blague.txt", "a")
        if (str(message.author) == "Σωιτε Λιτε#0138"):
            message.author = "Switelite#0138"
        file.write(str(message.content) +" @"+str(message.author).split('#')[0]+"\n")
        file.close
        await bot.send_message(message.channel, "Ta blague a bien été ajoutée ! En attente de confirmation de l'admin pour l'implémenter dans mon répertoire")

#function
#
async def check_nya():
    await bot.wait_until_ready()
    channel = [channel for channel in bot.get_all_channels() if channel.name == 'bot'][0]
    while not bot.is_closed:
            announce = nyaaRSS.run()
            if announce:
                for post in announce:
                    message = ('@everyone\n Le torrent : \n```' + post.title + "``` vient de sortir ! Vous pouvez le télécharger ici : \n " + post.description.split('<a href=\"')[1].split('\">')[0])
                    await bot.send_message(channel, message)
            await asyncio.sleep(60)

#command
#

#USELESS
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


#EVENEMENTIEL
@bot.command()
async def event():
    """
        The bot will display all events
        :return:
    """
    #CURRENT EVENT
    event = False
    conn = sqlite3.connect('database')  # Connection
    print("Opened database successfully")
    cursor = conn.execute("SELECT event_name,event_desc,start_date,end_date FROM Event")  # Querry
    message = ("Voici les évenements en cours !")  # Printing
    for row in cursor:
        now = date.today()  # Get current time
        start = date(2000 + int(row[2].split('/')[2]), int(row[2].split('/')[1]),
                     int(row[2].split('/')[0]))  # Get start date
        end = date(2000 + int(row[3].split('/')[2]), int(row[3].split('/')[1]),
                   int(row[3].split('/')[0]))  # Get end date
        if (now >= start and now <= end):
            message += ("\n-> " + row[0] + "\n"
                          + row[1] + "\n"
                                     "Il se déroulera du " + str(start) + " au " + str(end) + ".\n")
            event = True
    if not event:
        message += ("\nIl n'y a actuellement aucun évenement en cours")
    print("\n")
    event = False

    #NEXTEVENT
    message += ("\nVoici les évenements à venir !")  # Printing
    for row in cursor:
        if (start > now):
            message += ("\n-> " + row[0] + "\n"
                          + row[1] + "\n"
                                     "Il se déroulera du " + str(start) + " au " + str(end) + ".\n")
            event = True
    print("Operation done successfully")
    if not event:
        message += "\nIl n'y a actuellement aucun évenement à venir"

    await bot.say(message)
    print("Operation done successfully")
    conn.close()

@bot.command()
async def currentevent():
    """
    The bot will display the future events
    :return:
    """
    event = False #Say if there is an event
    conn = sqlite3.connect('database')  # Connection
    print("Opened database successfully")
    cursor = conn.execute("SELECT event_name,event_desc,start_date,end_date FROM Event")  # Querry
    message = ("Voici les évenements en cours !")#Printing
    for row in cursor:
        now = date.today()  # Get current time
        start = date(2000+int(row[2].split('/')[2]),int(row[2].split('/')[1]),int(row[2].split('/')[0]))#Get start date
        end = date(2000+int(row[3].split('/')[2]),int(row[3].split('/')[1]),int(row[3].split('/')[0]))#Get end date
        if (now>=start and now<=end):
            message +=("\n-> " + row[0] + "\n"
                          + row[1] + "\n"
                                     "Il se déroulera du " + str(start) + " au " + str(end) + ".\n")
            event = True #Event found
    if not event:
        await bot.say("\nIl n'y a actuellement aucun évenement en cours")

    print("Operation done successfully")
    conn.close()

@bot.command(pass_context=True)
async def idchannel(ctx, arg):
    id = [channel for channel in bot.get_all_channels() if channel.name == arg][0]
    await bot.say("L\' id du channel " + arg + " est : " + id)

@bot.command()
async def roll(number, mode, is_ticket):
    # TODO: Faire en sorte que fgodb et gacha soient initialisable au lancement du bot, et pas à chaque roll
    fgodb = fgoroll.Fgodb()
    gacha = fgoroll.Gacha(fgodb)


    images=""

    if gacha.check_mode(mode):
        gacha.change_mode(mode)
        result = gacha.simulate(number, is_ticket)

        for pulled in result:
            msg=""
            images=""
            if isinstance(pulled, fgoroll.Servant):
                msg = msg + str(pulled.name) + "   (" + str(pulled.sclass) + ")   " + str(pulled.stars) + "⭐\n"
                images = images + " " + str(pulled.image_url)
            else:
                msg = msg + str(pulled.name) + "   " + str(pulled.stars) + "⭐\n"
                images = images + " " + str(pulled.image_url)
            await bot.say(msg+"\n"+images)
            await asyncio.sleep(5)
    else:
        msg = "Mode inexistant"
        await bot.say(msg+"\n"+images)

@bot.command()
async def nextevent():
    """
    The bot will display the future events
    :return:
    """
    #Get current time
    now = date.today()
    event = False

    conn = sqlite3.connect('database')#Connection
    print("Opened database successfully")
    cursor = conn.execute("SELECT event_name,event_desc,start_date,end_date FROM Event")#Querry

    await bot.say("Voici les évenements à venir !")#Printing
    for row in cursor:
        start = date(2000+int(row[2].split('/')[2]),int(row[2].split('/')[1]),int(row[2].split('/')[0]))#Get start date
        end = date(2000+int(row[3].split('/')[2]),int(row[3].split('/')[1]),int(row[3].split('/')[0]))#Get end date
        if (start>now):
            await bot.say("\n-> "+row[0]+"\n"
                          +row[1]+"\n"
                          "Il se déroulera du "+ str(start)+ " au "+ str(end) + ".\n")
            event = True
    print("Operation done successfully")
    conn.close()

    if not event:
        await bot.say("\nIl n'y a actuellement aucun évenement à venir")

@bot.command()
async def recommendation():
    await bot.say("Voici la liste des recommendation de la session en cours:")

@bot.command()
async def completed(member,id_rec,id_obj):
    await bot.say("En cours d'implementation")

#AUTRES
@bot.command()
async def planninganime():
    with open('planning.png', 'rb') as f:
        await bot.send_file(bot.get_channel('178532977901305857'), f)

bot.loop.create_task(check_nya())
bot.run(main_key)
print("done")
