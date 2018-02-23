from Soturi.config.rrph_config import RRPH
from Soturi.soturi_bot import SoturiBot
from discord.ext import commands
from discord.utils import get


class Moderation:

    def __init__(self, bot: SoturiBot):
        self.bot = bot

    @commands.command()
    @commands.has_role('mods')
    async def kick(self, ctx: commands.Context, target, *reason):
        await ctx.message.delete()
        mods = get(ctx.guild.roles, id=RRPH.modRole)
        msg = await ctx.send(f"{mods.mention}")


def setup(bot):
    bot.add_cog(Moderation)