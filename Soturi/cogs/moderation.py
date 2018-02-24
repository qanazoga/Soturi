from Soturi.config.rrph_config import RRPH
from Soturi.soturi_bot import SoturiBot
from Soturi.utils.general_utils import convert_to_member
from discord.ext import commands
from discord.utils import get
from discord import Member


class Moderation:

    def __init__(self, bot: SoturiBot):
        self.bot = bot

    @commands.command()
    @commands.has_role('mod')
    async def kick(self, ctx, target):
        await ctx.message.delete()
        mods = get(ctx.guild.roles, id=RRPH.modRole)
        msg = await ctx.send(f"{mods.mention}")
        mbr: Member = get(ctx.guild.members, name=target)

        await ctx.send(f"I'm just a test, but I was targeting {mbr.mention}")


def setup(bot):
    bot.add_cog(Moderation)