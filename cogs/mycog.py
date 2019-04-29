from discord.ext import commands

#cogs must now subclass commands.Cog
class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #listeners now must have a decorator
    @commands.Cog.listener()
    async def on_message(self, message):
        print(message.content)

    @commands.command()
    async def echo(self, ctx, *, message):
        await ctx.send(message)

#this is technically part of extensions
def setup(bot):
    bot.add_cog(MyCog(bot))
