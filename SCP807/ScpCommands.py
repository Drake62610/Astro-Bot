import discord
from discord.ext import commands
import random

class ScpCommands():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def scp(self,params='help'):
        #DBOI (9)
        DBoilist = ["Voler toutes les cartes", "Parler avec un accent québécois ou allemand ou américain style rambo", "Ne ramasser aucune carte", "Ne jamais courir", "Ne pas communiquer", "Jouer sans aucun son", "Ne parler qu'en disant D-Boi jusqu'a la mort", "Trouver le flingue avant d'upgrade les cartes", "Se faire capturer par des NTF et les faire chier le plus longtemps possible"]
        randd = int(random.randint(0, 8))
        Dboipd = str(DBoilist[randd])
        #SCP (7)
        SCPlist = ["Jouer sans aucun son", "Ne pas communiquer", "Si SCP-049, ne ressuciter personne", "Si SCP-106, jouer sans portail", "Si SCP-106, se tp dans son portail à chaque kill","Si SCP-096, ne pas casser des portes", "Si SCP-173, attendre 15 secondes avant de sortir"]
        randscp = int(random.randint(0, 6))
        SCPpd = str(SCPlist[randscp])
        #NTF (7)
        NTFlist = ["Parler avec un accent québécois ou allemand ou américain style rambo", "Ne pas attendre à tous les ascenseurs ses collègues", "Ne pas communiquer", "Jouer sans aucun son", "Drop la radio au début de la partie", "Tuer toutes les classes D", "Ne fermer aucune gate"]
        randntf = int(random.randint(0, 6))
        NTFpd = str(NTFlist[randntf])
        #CHAOS (6)
        Chaoslist = ["Parler avec un accent québécois ou allemand ou américain style rambo", "Ne pas attendre à tous les ascenseurs ses collègues", "Sauve les scientifiques et laisse les classes D", "Jouer sans aucun son", "Tuer un mec en criant Allah Akbar", "Raconter une blague à l'intercom"]
        randchaos = int(random.randint(0, 5))
        Chaospd = str(Chaoslist[randchaos])
        #NERD (6)
        Nerdlist = ["Marcher en crabe", "Parler avec un accent québécois ou allemand ou américain style rambo", "Ne jamais courir", "Jouer sans aucun son", "Ne faire que rabaisser les classes D", "Ne parler qu'en disant Yee jusqu'a la mort"]
        randnerd = int(random.randint(0, 5))
        Nerdpd = str(Nerdlist[randnerd])
        if (params == "D-Boi" or params == "D-boi" or params == "DBoi" or params == "Dboi" or params == "ClasseD" or params == "D" or params == "d" or params == "Déchet"):
            await self.bot.say("Ton défi : **" + Dboipd + "**")
        elif (params == "SCP" or params == "scp"):
            await self.bot.say("Ton défi : **" + SCPpd + "**")
        elif (params == "NTF" or params == "MTF" or params == "ntf" or params == "mtf"):
            await self.bot.say("Ton défi : **" + NTFpd + "**")
        elif (params == "Chaos" or params == "CI"):
            await self.bot.say("Ton défi : **" + Chaospd + "**")
        elif (params == "Nerd" or params == "Scientist" or params == "scientist" or params == "Scientifique"):
            await self.bot.say("Ton défi : **" + Nerdpd + "**")
        else:
            await self.bot.say("```css"+"\n"+
            "[Roulette SCP]"+"\n"+"!scp <role>" + "\n" + "\n" +
            "Avec <Role> = D-Boi, SCP, NTF, Chaos ou Nerd" + "\n" +
            "Envoie un defi aleatoire selon le role sur SCP Secret Laboratory" + "```")

def setup(bot):
    bot.add_cog(ScpCommands(bot))
