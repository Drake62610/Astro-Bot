import discord
from discord.ext import commands
import random

class ScpCommands():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def scp(self,params):
        #DBOI 7
        DBoilist = ["Ne ramasser aucune carte", "Ne jamais courir", "Ne pas communiquer", "Jouer sans aucun son", "Ne parler qu'en disant D-Boi jusqu'a la mort", "Trouver le flingue avant d'upgrade les cartes", "Se faire capturer par des NTF et les faire chier le plus longtemps possible"]
        randd = int(random.randint(0, 6))
        Dboipd = str(DBoilist[randd])
        #SCP 7
        SCPlist = ["Jouer sans aucun son", "Ne pas communiquer", "Si SCP-049, ne ressuciter personne", "Si SCP-106, jouer sans portail", "Si SCP-106, se tp dans son portail à chaque kill","Si SCP-096, ne pas casser des portes", "Si SCP-173, attendre 15 secondes avant de sortir"]
        randscp = int(random.randint(0, 6))
        SCPpd = str(SCPlist[randscp])
        #NTF 5
        NTFlist = ["Ne pas communiquer", "Jouer sans aucun son", "Drop la radio au début de la partie", "Tuer toutes les classes D", "Ne fermer aucune gate"]
        randntf = int(random.randint(0, 4))
        NTFpd = str(NTFlist[randntf])
        #CHAOS 3
        Chaoslist = ["Jouer sans aucun son", "Tuer un mec en criant Allah Akbar", "Raconter une blague à l'intercom"]
        randchaos = int(random.randint(0, 2))
        Chaospd = str(Chaoslist[randchaos])
        #NERD 4
        Nerdlist = ["Ne jamais courir", "Jouer sans aucun son", "Ne faire que rabaisser les classes D", "Ne parler qu'en disant Yee jusqu'a la mort"]
        randnerd = int(random.randint(0, 3))
        Nerdpd = str(Nerdlist[randnerd])
        if params == "D-Boi":
            await self.bot.say("Ton défi : **" + Dboipd + "**")
        elif params == "SCP":
            await self.bot.say("Ton défi : **" + SCPpd + "**")
        elif params == "NTF":
            await self.bot.say("Ton défi : **" + NTFpd + "**")
        elif params == "Chaos":
            await self.bot.say("Ton défi : **" + Chaospd + "**")
        elif params == "Nerd":
            await self.bot.say("Ton défi : **" + Nerdpd + "**")
        else:
            await self.bot.say("```css"+"\n"+
            "[Roulette SCP]"+"\n"+"!scp <role>" + "\n" + "\n" +
            "Avec <Role> = D-Boi, SCP, NTF, Chaos ou Nerd" + "\n" +
            "Envoie un defi aleatoire selon le role sur SCP Secret Laboratory" + "```")


def setup(bot):
    bot.add_cog(ScpCommands(bot))
