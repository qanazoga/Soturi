import json
from config.rrph_config import RRPH
from soturi_bot import SoturiBot
from discord.utils import get


class RoleSignupSystem:

    def __init__(self, bot: SoturiBot):
        self.bot = bot

    async def on_raw_reaction_add(self, emoji, message_id, channel_id, user_id):
        if channel_id != RRPH.welcomeChannel:
            return

        with open("config/roles.json", "r") as file:
            translator = json.load(file)

        rrph: Guild = get(self.bot.guilds, id=RRPH.id)
        member: Member = get(rrph.members, id=user_id)
        role = get(rrph.roles, id=translator[str(message_id)])

        await member.add_roles(role)

    async def on_raw_reaction_remove(self, emoji, message_id, channel_id, user_id):
        if channel_id != RRPH.welcomeChannel:
            return

        with open("config/roles.json", "r") as file:
            translator = json.load(file)

        rrph: Guild = get(self.bot.guilds, id=RRPH.id)
        member: Member = get(rrph.members, id=user_id)
        role = get(rrph.roles, id=translator[str(message_id)])

        await member.remove_roles(role)


def setup(bot):
    bot.add_cog(RoleSignupSystem(bot))
