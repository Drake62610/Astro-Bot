import discord
from discord.ext import commands
from src.utils import default
import logging

class AdminCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger('AstroLog')
        self.config = default.get("config.json")

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
                        Quand c'est fait nous te demandons de remplir la condition indiquée à la fin du post et je te donnerai le rôle d'invité.\n\
                        \n\
                        Bonne lecture !"
        await member.send(join_message)

    # Give roles commands
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        celestis_guild_id = 161079565832159232
        # Accept reglement detection, watch rules message
        if payload.message_id == 178672774263341067:
            arrivant_role_id = 183244699329363972
            print(payload.emoji.name)
            if payload.emoji.name == '🆗':
                role = self.bot.get_guild(celestis_guild_id).get_role(arrivant_role_id)
                await self.bot.get_guild(celestis_guild_id).get_member(payload.user_id).add_roles(role)

        # Role reaction detection, watch #rules channel
        if payload.channel_id == 571774099911606284:
            # Each case represent a role to give compare emoji "name"            
            admWeabRoleId = self.config.admWeabRoleId
            admOwRoleId = self.config.admOwRoleId
            admYugiohRoleId = self.config.admYugiohRoleId
            admTabletopRoleId = self.config.admTabletopRoleId
            admMinecraftRoleId = self.config.admMinecraftRoleId
            admCarteRoleId = self.config.admCarteRoleId
            admJdrRoleId = self.config.admJdrRoleId

            if payload.emoji.name == self.config.admWeabEmoji:
                role = self.bot.get_guild(celestis_guild_id).get_role(admWeabRoleId)
            elif payload.emoji.name == self.config.admOwbEmoji:
                role = self.bot.get_guild(celestis_guild_id).get_role(admOwRoleId)
            elif payload.emoji.name == self.config.admYugiohEmoji:
                role = self.bot.get_guild(celestis_guild_id).get_role(admYugiohRoleId)
            elif payload.emoji.name == self.config.admTabletopEmoji:
                role = self.bot.get_guild(celestis_guild_id).get_role(admTabletopRoleId)
            elif payload.emoji.name == self.config.admMinecraftEmoji:
                role = self.bot.get_guild(celestis_guild_id).get_role(admMinecraftRoleId)
            elif payload.emoji.name == self.config.admCarteEmoji:
                role = self.bot.get_guild(celestis_guild_id).get_role(admCarteRoleId)
            elif payload.emoji.name == self.config.admJdrEmoji:
                role = self.bot.get_guild(celestis_guild_id).get_role(admJdrRoleId)

            # Missing case where a bad emoji is inputed
            await self.bot.get_guild(celestis_guild_id).get_member(payload.user_id).add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        # Role reaction detection
        if payload.channel_id == 571774099911606284:
            # Each case represent a role to give compare emoji "name"
            celestis_guild_id = 161079565832159232
            weab_role_id = 571783195973124113
            ow_role_id = 571783638757408783
            yugioh_role_id = 571784801431060492
            tabletop_role_id = 571783820722962452
            minecraft_role_id = 571783779517988904
            carte_role_id = 571783602157649922
            jdr_role_id = 571783692754878507
            if payload.emoji.name == '🇯🇵':
                role = self.bot.get_guild(celestis_guild_id).get_role(weab_role_id)
            elif payload.emoji.name == 'OW':
                role = self.bot.get_guild(celestis_guild_id).get_role(ow_role_id)
            elif payload.emoji.name == 'kuribo':
                role = self.bot.get_guild(celestis_guild_id).get_role(yugioh_role_id)
            elif payload.emoji.name == 'tabouret':
                role = self.bot.get_guild(celestis_guild_id).get_role(tabletop_role_id)
            elif payload.emoji.name == 'dark':
                role = self.bot.get_guild(celestis_guild_id).get_role(minecraft_role_id)
            elif payload.emoji.name == '🗺':
                role = self.bot.get_guild(celestis_guild_id).get_role(carte_role_id)
            elif payload.emoji.name == '🎲':
                role = self.bot.get_guild(celestis_guild_id).get_role(jdr_role_id)

            await self.bot.get_guild(celestis_guild_id).get_member(payload.user_id).remove_roles(role)

def setup(bot):
    bot.add_cog(AdminCommands(bot))
logger = logging.getLogger('AstroLog')

