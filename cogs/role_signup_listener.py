from config.rrph_config import RRPH
from soturi_bot import SoturiBot
from discord.utils import get
from discord import Guild, Member, RawReactionActionEvent
from discord.ext import commands
from discord.ext.commands import Cog
import json


class RoleSignupSystem(commands.Cog):

    def __init__(self, bot: SoturiBot):
        self.bot = bot

    @Cog.listener()
    async def on_raw_reaction_add(self, pl: RawReactionActionEvent):
        if (pl.channel_id != RRPH.welcome_channel) \
                and (pl.channel_id != RRPH.iconoclasm_id)\
                and (pl.channel_id != RRPH.role_signup_channel):
            return

        print("Adding role")
        with open("config/roles.json", "r") as file:
            translator = json.load(file)

        guild: Guild = self.bot.get_guild(id=pl.guild_id)
        role = get(guild.roles, id=translator[str(pl.message_id)])

        member = guild.get_member(pl.user_id)
        await member.add_roles(role, reason="Role Signup System")

    @Cog.listener()
    async def on_raw_reaction_remove(self, pl: RawReactionActionEvent):
        if (pl.channel_id != RRPH.welcome_channel) \
                and (pl.channel_id != RRPH.iconoclasm_id)\
                and (pl.channel_id != RRPH.role_signup_channel):
            return

        print("removing role")
        with open("config/roles.json", "r") as file:
            translator = json.load(file)

        guild: Guild = self.bot.get_guild(id=pl.guild_id)
        role = get(guild.roles, id=translator[str(pl.message_id)])

        member = guild.get_member(pl.user_id)
        await member.remove_roles(role, reason="Role Signup System")


def setup(bot):
    bot.add_cog(RoleSignupSystem(bot))
