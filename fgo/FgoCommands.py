import asyncio
from main import bot
from fgo import fgoroll
from discord.ext import commands


class FgoCommands:
    def __init__(self, bot):
        self.bot = bot
        self.fgodb = fgoroll.Fgodb()
        self.gacha = fgoroll.Gacha(self.fgodb)

    @commands.command(pass_context=True)
    async def roll(self,ctx, number=1, mode="Story", is_ticket=False, is_pretty=False):
        if self.gacha.check_mode(mode):
            r = fgoroll.Roll(self.gacha, mode, number, is_ticket)

            if is_pretty == "True":
                await self.show_pretty_roll(r, ctx)
            else:
                await self.show_roll(r.result)
        else:
            msg = "Mode inexistant."
            msg += " Le format de la commande est : !roll nombre mode ticket? pretty?." \
                  " Exemple: !roll 10 Story False True"
            await self.bot.say(msg)
            msg2 = "Les campagnes disponibles sont : Story"
            for c in self.gacha.campaigns:
                msg2 += ", " + c.title
            await self.bot.say(msg2)

    async def show_roll(self,result):
        for r in result:
            if isinstance(r, fgoroll.Servant):
                msg = str(r.name) + "   (" + str(r.sclass) + ")   " + str(r.stars) + "⭐\n"
                images = " " + str(r.image_url)
            else:
                msg = str(r.name) + "   " + str(r.stars) + "⭐\n"
                images = " " + str(r.image_url)
            await self.bot.say(msg + "\n" + images)
            await asyncio.sleep(5)

    async def show_pretty_roll(self, r, ctx):
        msg_queue = r.pretty_print()
        await self.bot.say("Roll en cours... (x" + str(len(r.result)) + ")")
        for mes in msg_queue:
            if mes['type'] == "upload":
                await self.bot.upload(mes['content'])
            elif mes['type'] == "say":
                await self.bot.say(mes['content'])
            else:
                await asyncio.sleep(5)
                await self.bot.purge_from(ctx.message.channel, limit=1, check=is_bot)
        await self.bot.say("Roll terminé !")

    async def is_bot(self,m):
        return m.author == self.bot.user


def setup(bot):
    bot.add_cog(FgoCommands(bot))


# # TEST
# fgodb = fgoroll.Fgodb()
# gacha = fgoroll.Gacha(fgodb)
# roll = fgoroll.Roll(gacha,"Camelot Pickup Summon",10,False)
#
# print("===ROLL===")
# for pulled in roll.result:
#     if isinstance(pulled, fgoroll.Servant):
#         msg = str(pulled.name) + "   (" + str(pulled.sclass) + ")   " + str(pulled.stars) + "⭐\n"
#         images = " " + str(pulled.image_url)
#     else:
#         msg = str(pulled.name) + "   " + str(pulled.stars) + "⭐\n"
#         images = " " + str(pulled.image_url)
#     print(msg)
# print("===END===")