import discord
from discord.ext import commands
import logging

class AdminCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger('AstroLog')

    # Server information commands
    # Inspired from https://github.com/AlexFlipnote/discord_bot.py/blob/master/cogs/discord.py

    @commands.command()
    @commands.guild_only()
    async def profil(self, ctx, *, user: discord.Member = None):
        """ Get the profile picture"""
        if user is None:
            user = ctx.author
    
        await ctx.send(f"Image de profil de **{user.name}**\n{user.avatar_url_as(size=1024)}")

    @commands.command()
    @commands.guild_only()
    async def server_logo(self, ctx):
        """ Get the profile picture"""    
        await ctx.send(f"Logo du discord **{ctx.guild.name}**\n{ctx.guild.icon_url_as(size=1024)}")

    @commands.command()
    @commands.guild_only()
    async def joined_at(self, ctx, *, user: discord.Member = None):
        """ Check when a user joined the current server """
        if user is None:
            user = ctx.author

        embed = discord.Embed(colour=user.top_role.colour.value)
        embed.set_thumbnail(url=user.avatar_url)
        embed.description = f'**{user}** a rejoins **{ctx.guild.name}**\n{user.joined_at.strftime("%d %B %Y, %H:%M")}'
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def user(self, ctx, *, user: discord.Member = None):
        """ Get user information """
        if user is None:
            user = ctx.author

        embed = discord.Embed(colour=user.top_role.colour.value)
        embed.set_thumbnail(url=user.avatar_url)

        embed.add_field(name="Pseudo complet", value=user, inline=True)
        embed.add_field(name="Surnom", value=user.nick if hasattr(user, "nick") else "None", inline=True)
        embed.add_field(name="Créé le", value=user.created_at.strftime("%d %B %Y, %H:%M"), inline=True)
        embed.add_field(name="A rejoins Celestis le", value=user.joined_at.strftime("%d %B %Y, %H:%M"), inline=True)

        embed.add_field(
            name="Roles",
            value=', '.join([f"<@&{x.id}>" for x in user.roles if x is not ctx.guild.default_role]) if len(user.roles) > 1 else 'None',
            inline=False
        )

        await ctx.send(embed=embed)


    # Server vital commands
    @commands.Cog.listener()
    async def on_member_join(self, member:discord.Member):
        """Send a private message to the joiner in order to inform him what to do"""
        join_message = "Bienvenue sur le server de Celestis !\n\
                        Afin de pouvoir avoir accès au reste du serveur tu dois lire le règlement qui se situe dans ```#accueil```!\n\
                        Quand c'est fait nous te demandons de remplir la condition indiqué à la fin du post et je te donnerai le rôle d'invité.\n\
                        \n\
                        Bonne lecture !"
        await member.send(join_message)


def setup(bot):
    bot.add_cog(AdminCommands(bot))
logger = logging.getLogger('AstroLog')

