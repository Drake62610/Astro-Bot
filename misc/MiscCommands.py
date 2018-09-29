import discord
from discord.ext import commands
import random
import logging
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
        if "membres du crew" in [y.name.lower() for y in ctx.message.author.roles]:
            await self.bot.send_message(await self.bot.start_private_message(ctx.message.author), ovwtxt)

    @commands.command()
    async def overwatchCLST(self):
        pass

def setup(bot):
    bot.add_cog(MiscCommands(bot))
