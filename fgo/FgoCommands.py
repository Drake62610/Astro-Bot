import asyncio
from main import bot
from fgo import fgoroll
from discord.ext import commands

class FgoCommands():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def roll(self,ctx, number=1, mode="Story", is_ticket="False", is_pretty="False"):
        # TODO: Faire en sorte que fgodb et gacha soient initialisable au lancement du bot, et pas à chaque roll
        fgodb = fgoroll.Fgodb()
        gacha = fgoroll.Gacha(fgodb)

        if gacha.check_mode(mode):
            gacha.change_mode(mode)
            result = gacha.simulate(number, is_ticket)

            if is_pretty == "True":
                await self.show_pretty_roll(result, gacha, ctx)
            else:
                await self.show_roll(result)
        else:
            msg = "Mode inexistant"
            await self.bot.say(msg)


    async def show_roll(self,result):
        for pulled in result:
            if isinstance(pulled, fgoroll.Servant):
                msg = str(pulled.name) + "   (" + str(pulled.sclass) + ")   " + str(pulled.stars) + "⭐\n"
                images = " " + str(pulled.image_url)
            else:
                msg = str(pulled.name) + "   " + str(pulled.stars) + "⭐\n"
                images = " " + str(pulled.image_url)
            await self.bot.say(msg + "\n" + images)
            await asyncio.sleep(5)

    async def show_pretty_roll(self,result, gacha, ctx):
        msg_queue = gacha.pretty_print(result)
        await self.bot.say("Roll en cours... (x" + str(len(result)) + ")")
        for mes in msg_queue:
            if mes['type'] == "upload":
                await self.bot.upload(mes['content'])
            elif mes['type'] == "say":
                await self.bot.say(mes['content'])
            else:
                await asyncio.sleep(5)
                await self.bot.purge_from(ctx.message.channel, limit=1)
        await self.bot.say("Roll terminé !")

    async def is_bot(self,m):
        return m.author == self.bot.user

def setup(bot):
    bot.add_cog(FgoCommands(bot))
