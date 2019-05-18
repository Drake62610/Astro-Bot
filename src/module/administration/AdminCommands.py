import discord
from discord.ext import commands
import logging

class AdminCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger('AstroLog')

    @commands.command()
    @commands.guild_only()
    async def joined_at(self, ctx, *, user: discord.Member = None):
        """ Check when a user joined the current server """
        if user is None:
            user = ctx.author

        embed = discord.Embed(colour=user.top_role.colour.value)
        embed.set_thumbnail(url=user.avatar_url)
        embed.description = f'**{user}** joined **{ctx.guild.name}**\n{user.joined_at.strftime("%d %B %Y, %H:%M")}'
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(AdminCommands(bot))
logger = logging.getLogger('AstroLog')

