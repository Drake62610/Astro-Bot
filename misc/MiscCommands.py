import discord
from discord.ext import commands
import random
import logging
import requests
from vote import roll
from keys import ovwtxt

class MiscCommands():
    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger('AstroLog')

    # USELESS
    @commands.command(pass_context=True)
    async def help(self,ctx):
        await self.bot.send_message(await self.bot.start_private_message(ctx.message.author), "yo bitch")

    @commands.command(pass_context=True)
    async def roll(self,ctx, input):
        tmp = ''
        result = roll.lancer(input)
        for i in result:
            tmp += str(i) + ' '
        await self.bot.say(tmp)

    @commands.command(pass_context=True)
    async def joined_at(self,ctx, member: discord.Member = None):
        if member is None:
            member = ctx.message.author

        await self.bot.say('{0} joined at {0.joined_at}'.format(member))


    @commands.command()
    async def hello(self):
        self.logger.debug("coucou")
        await self.bot.say("Bip Boop (Hello World !)")


    @commands.command(pass_context=True)
    async def idchannel(self,ctx, arg):
        id = [channel for channel in self.bot.get_all_channels() if channel.name == arg][0]
        await self.bot.say("L\' id du channel " + arg + " est : " + id)


    # AUTRES
    @commands.command()
    async def planninganime(self):
        with open('misc/planning.png', 'rb') as f:
            await self.bot.send_file(self.bot.get_channel('178532977901305857'), f)

    @commands.command()
    async def addTheme(self, word):
        word = word.split(',')
        self.logger.debug(word)
        with open('misc/theme.db', 'a') as f:
            for i in word:
                f.write(i + '\n')
        await self.bot.say('Fichier mis a jour')

    @commands.command()
    async def theme(self):
        tmp = []
        with open('misc/theme.db', 'r') as f:
            for line in f:
                tmp.append(line)
        await self.bot.say('Le theme sera : ' + random.choice(tmp))

    @commands.command(pass_context=True)
    async def overwatchID(self,ctx):
        self.logger.info("overwatchID called by " + str(ctx.message.author))
        if "membres du crew" in [y.name.lower() for y in ctx.message.author.roles] or "employés netflix" in [y.name.lower() for y in ctx.message.author.roles]:
            await self.bot.say("Je vous envoie les identifiants par MP !")
            await self.bot.send_message(await self.bot.start_private_message(ctx.message.author), ovwtxt)
        else:
            drake = ctx.message.server.get_member_named("Drake62610")
            await self.bot.say("Vous n'êtes pas autorisé à acceder aux identifiants pour le moments, n'hésitez pas à contacter " + drake.mention + " si vous souhaitez les obtenirs.")
    @commands.command()
    async def overwatchCLST(self):
        pass

    #Communique avec l'API de la MEL pour donner la disponibilité des vélos autour d'une location enregistrée auparavant
    #Aucune gestion d'erreur ici...
    @commands.command(pass_context=True)
    async def vlille(self,ctx,lieu="ISEN"):
        self.logger.info("vlille function called by"+ str(ctx.message.author)+ " with "+lieu+" parameter")
        url = 'none'
        msg = ''
        etat = ''
        #Add places
        if lieu.lower()=="isen":
            lieu = "ISEN"
            url = 'https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=libelle%3D28+OR+libelle%3D03+OR+libelle%3D09+OR+libelle%3D02&lang=FR&facet=libelle&facet=nom&facet=commune&facet=etat&facet=type&facet=etatconnexion'
        elif lieu.lower()=="lille flandre" or lieu.lower()=="flandre" or lieu.lower()=="gare":
            lieu = "Lille Flandre"
            url = "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=libelle%3D24+OR+libelle%3D25+OR+libelle%3D12+OR+libelle%3D26&lang=FR&facet=libelle&facet=nom&facet=commune&facet=etat&facet=type&facet=etatconnexion"
        elif lieu.lower()=="ugc" or lieu.lower()=="repu":
            lieu = "Republique Beaux Art"
            url = "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=libelle%3D08+OR+libelle%3D06+OR+libelle%3D43+OR+libelle%3D66&lang=FR&facet=libelle&facet=nom&facet=commune&facet=etat&facet=type&facet=etatconnexion"
        #Let's do our request
        if url != 'none':
            self.logger.info("Request to MEL Api")
            response = requests.get(url)
            records = response.json()['records']
            msg = msg + ":bicyclist: **__Voilà les stations que j'ai trouvé autour de "+lieu+" :__** :bicyclist: \n"
            for i in records:
                fields = i['fields']
                msg = msg + "__"+fields['nom'] + " :__ "
                #Graphic interface wowo
                if fields['etat']=="EN SERVICE":
                    etat = ":white_check_mark:"
                else:
                    etat = ":no_entry_sign:"
                #Dispo
                msg = msg + etat + "\n  -nbvelosdispo : " + str(fields["nbvelosdispo"])
                if str(fields["nbvelosdispo"]) == "0":
                    msg = msg + " :no_bicycles:"
                msg = msg + "\n"
                #Capacité max
                msg = msg + "  -nbplacesdispo : " + str(fields["nbplacesdispo"])
                if fields["nbplacesdispo"] == 0:
                    msg = msg + " :no_bicycles:"
                msg = msg + "\n"
                self.logger.debug("Impression d'information sur " + fields['nom'])
        else :
            self.logger.info("Le lieu n'existe pas, fin de la fonction")
            msg = msg + ("Le lieu entré n'est pas géré")
        await self.bot.say(msg)

def setup(bot):
    bot.add_cog(MiscCommands(bot))
