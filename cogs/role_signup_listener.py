from config.rrph_config import RRPH
from soturi_bot import SoturiBot
from discord.utils import get
from discord import Guild, Member
import json


class RoleSignupSystem:

    def __init__(self, bot: SoturiBot):
        self.bot = bot

    async def on_raw_reaction_add(self, event):
        if (event.channel_id != RRPH.welcome_channel) \
                and (event.channel_id != RRPH.iconoclasm_id)\
                and (event.channel_id != RRPH.role_signup_channel):
            return

        print("Adding role")
        with open("config/roles.json", "r") as file:
            translator = json.load(file)

        guild: Guild = self.bot.get_channel(event.channel_id).guild
        member: Member = get(guild.members, id=event.user_id)
        role = get(guild.roles, id=translator[str(event.message_id)])

        await member.add_roles(role, reason="Role Signup System")

    async def on_raw_reaction_remove(self, event):
        if (event.channel_id != RRPH.welcome_channel) \
                and (event.channel_id != RRPH.iconoclasm_id)\
                and (event.channel_id != RRPH.role_signup_channel):
            return

        print("Removing role")
        with open("config/roles.json", "r") as file:
            translator = json.load(file)

        guild: Guild = self.bot.get_channel(event.channel_id).guild
        member: Member = get(guild.members, id=event.user_id)
        role = get(guild.roles, id=translator[str(event.message_id)])

        await member.remove_roles(role, reason="Role Signup System")


def setup(bot):
    bot.add_cog(RoleSignupSystem(bot))
