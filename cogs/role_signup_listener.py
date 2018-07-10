from config.rrph_config import RRPH
from soturi_bot import SoturiBot
from discord.utils import get
from discord import Guild, Member
import json


class RoleSignupSystem:

    def __init__(self, bot: SoturiBot):
        self.bot = bot

    async def on_raw_reaction_add(self, emoji, message_id, channel_id, user_id):
        if (channel_id != RRPH.welcome_channel) and (channel_id != RRPH.iconoclasm_id):
            return

        print("Adding role")
        with open("config/roles.json", "r") as file:
            translator = json.load(file)

        guild: Guild = self.bot.get_channel(channel_id).guild
        member: Member = get(guild.members, id=user_id)
        role = get(guild.roles, id=translator[str(message_id)])

        await member.add_roles(role, reason="Role Signup System")

    async def on_raw_reaction_remove(self, emoji, message_id, channel_id, user_id):
        if (channel_id != RRPH.welcome_channel) and (channel_id != RRPH.iconoclasm_id):
            return

        print("Removing role")
        with open("config/roles.json", "r") as file:
            translator = json.load(file)

        guild: Guild = self.bot.get_channel(channel_id).guild
        member: Member = get(guild.members, id=user_id)
        role = get(guild.roles, id=translator[str(message_id)])

        await member.remove_roles(role, reason="Role Signup System")


def setup(bot):
    bot.add_cog(RoleSignupSystem(bot))
