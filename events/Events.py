import asyncio
import discord
import logging
import recastai

from discord.ext import commands

class Events:
    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger('AstroLog')

    async def on_ready(self):
        await self.bot.change_presence(game=discord.Game(name='Waifu Fight - Tentacle School Life Edition'))
        self.logger.info('Logged in as ' + self.bot.user.name)

    async def on_message(self,message):

        # RECAST
        if (str(message.channel) == "bot"):
            if not str(message.author) == "Astro Bot#9191" and not message.content[0] == "!":
                client = recastai.Client('9d1a465da0eeabc77ea479fe567c6202')
                response = client.request.converse_text(str(message.content))
                await self.bot.send_message(message.channel, response.reply)

        # OTHER
        if (message.content.startswith('Aurevoir Astro Bot') or message.content.startswith('Sayonara Astro Bot')):
            await self.bot.send_message(message.channel, "Aurevoir " + str(message.author).split('#')[0] + " !")

        if message.content.startswith('add joke'):
            file = open("blague.txt", "a")
            if (str(message.author) == "Σωιτε Λιτε#0138"):
                message.author = "Switelite#0138"
            file.write(str(message.content) + " @" + str(message.author).split('#')[0] + "\n")
            file.close
            await self.bot.send_message(message.channel,
                                   "Ta blague a bien été ajoutée ! En attente de confirmation de l'admin pour l'implémenter dans mon répertoire")

def setup(bot):
    bot.add_cog(Events(bot))
