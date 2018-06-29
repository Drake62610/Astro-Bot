import discord
from discord.ext import commands
import random

class ScpCommands():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def scp(self,params='help'):
        #DBOI (11)
        DBoilist = ["Parler dans une langue étrangère", "Parler comme un pirate", "Ne jamais courir", "Marcher en crabe", "Ne pas communiquer", "Jouer sans aucun son", "Voler toutes les cartes", "Ne ramasser aucune carte", "Ne parler qu'en disant D-Boi jusqu'a la mort", "Trouver le flingue avant d'upgrade les cartes", "Se faire capturer par des NTF et les faire chier le plus longtemps possible"]
        randd = int(random.randint(0, 10))
        Dboipd = str(DBoilist[randd])
        #SCP (7)
        SCPlist = ["Ne pas communiquer", "Jouer sans aucun son", "Si SCP-049, ne ressuciter personne", "Si SCP-096, ne pas casser des portes", "Si SCP-106, jouer sans portail", "Si SCP-106, se tp dans son portail à chaque kill", "Si SCP-173, attendre 15 secondes avant de sortir"]
        randscp = int(random.randint(0, 6))
        SCPpd = str(SCPlist[randscp])
        #NTF (11)
        NTFlist = ["Parler dans une langue étrangère", "Parler comme un pirate", "Ne jamais courir", "Marcher en crabe", "Ne pas communiquer", "Jouer sans aucun son", "Ne pas attendre à tous les ascenseurs ses collègues", "Sauve les classes D et laisse les scientifiques", "Ne fermer aucune gate", "Drop la radio au début de la partie", "Tuer toutes les classes D"]
        randntf = int(random.randint(0, 10))
        NTFpd = str(NTFlist[randntf])
        #CHAOS (11)
        Chaoslist = ["Parler dans une langue étrangère", "Parler comme un pirate", "Ne jamais courir", "Marcher en crabe", "Ne pas communiquer", "Jouer sans aucun son", "Ne pas attendre à tous les ascenseurs ses collègues", "Sauve les scientifiques et laisse les classes D", "Ne fermer aucune gate", "Tuer un mec en criant Allah Akbar", "Raconter une blague à l'intercom"]
        randchaos = int(random.randint(0, 10))
        Chaospd = str(Chaoslist[randchaos])
        #NERD (8)
        Nerdlist = ["Parler dans une langue étrangère", "Parler comme un pirate", "Ne jamais courir", "Marcher en crabe", "Jouer sans aucun son", "Ne faire que rabaisser les classes D", "Ne parler qu'en disant Yee jusqu'a la mort", "Trouver une escouade de NTF et les faire chier"]
        randnerd = int(random.randint(0, 7))
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
