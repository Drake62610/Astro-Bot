import discord
from discord.ext import commands
import random
import logging
import requests
from src.trashy.vote import roll

class MiscCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger('AstroLog')

    # USELESS
    @commands.command()
    async def help(self,ctx):
        await ctx.send(await self.bot.start_private_message(ctx.message.author), "yo bitch")

    @commands.command()
    async def roll(self,ctx, input):
        tmp = ''
        result = roll.lancer(input)
        for i in result:
            tmp += str(i) + ' '
        await ctx.send(tmp)

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Bip Boop (Hello World !)")

##TO DO
    # @commands.command()
    # async def idchannel(self, ctx, arg):
    #     id = [channel for channel in self.bot.get_all_channels() if channel.name == arg][0]
    #     await ctx.send("L\' id du channel " + arg + " est : " + id)

    # AUTRES
    @commands.command()
    async def planninganime(self, ctx):
        with open('misc/planning.png', 'rb') as f:
            ch = ctx.channel
            await ctx.send(file=discord.File('misc/planning.png'))

    @commands.command()
    async def addTheme(self, ctx, word):
        word = word.split(',')
        with open('misc/theme.db', 'a') as f:
            for i in word:
                f.write(i + '\n')
        await ctx.send('Fichier mis a jour')

    @commands.command()
    async def theme(self, ctx):
        tmp = []
        with open('misc/theme.db', 'r') as f:
            for line in f:
                tmp.append(line)
        await ctx.send('Le theme sera : ' + random.choice(tmp))

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
        await ctx.send(msg)

def setup(bot):
    bot.add_cog(MiscCommands(bot))
