import asyncio
from main import bot
from datetime import date


@bot.command()
async def event():
    """
        The bot will display all events
        :return:
    """
    # CURRENT EVENT
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

    # NEXTEVENT
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
    event = False  # Say if there is an event
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
            event = True  # Event found
    if not event:
        await bot.say("\nIl n'y a actuellement aucun évenement en cours")

    print("Operation done successfully")
    conn.close()


@bot.command()
async def nextevent():
    """
    The bot will display the future events
    :return:
    """
    # Get current time
    now = date.today()
    event = False

    conn = sqlite3.connect('database')  # Connection
    print("Opened database successfully")
    cursor = conn.execute("SELECT event_name,event_desc,start_date,end_date FROM Event")  # Querry

    await bot.say("Voici les évenements à venir !")  # Printing
    for row in cursor:
        start = date(2000 + int(row[2].split('/')[2]), int(row[2].split('/')[1]),
                     int(row[2].split('/')[0]))  # Get start date
        end = date(2000 + int(row[3].split('/')[2]), int(row[3].split('/')[1]),
                   int(row[3].split('/')[0]))  # Get end date
        if (start > now):
            await bot.say("\n-> " + row[0] + "\n"
                          + row[1] + "\n"
                                     "Il se déroulera du " + str(start) + " au " + str(end) + ".\n")
            event = True
    print("Operation done successfully")
    conn.close()

    if not event:
        await bot.say("\nIl n'y a actuellement aucun évenement à venir")


@bot.command()
async def recommendation():
    await bot.say("Voici la liste des recommendation de la session en cours:")


@bot.command()
async def completed(member, id_rec, id_obj):
    await bot.say("En cours d'implementation")
