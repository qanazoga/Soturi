from config.rrph_config import RRPH
from soturi_bot import SoturiBot
from discord.ext import commands
from discord.utils import get
from discord import Member
from utils import checks
import traceback


class Styx(commands.Cog):

    def __init__(self, bot: SoturiBot):
        self.bot = bot

    @commands.group(name="styx")
    @commands.has_role("styx-admins")
    @checks.is_in_guild(RRPH.id)
    async def styx(self, ctx):
        """[GROUP] of commands related to Styx."""
        ...

    @styx.command(name="add")
    async def _add(self, ctx, target: Member):
        """Adds styx user role to a target."""
        role = get(ctx.guild.roles, id=RRPH.styx_user_role)
        try:
            await target.add_roles(role)
            await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
        except Exception:
            await ctx.send(f"```py\n{traceback.format_exc()}\n```")

    @styx.command()
    async def remove(self, ctx, target: Member):
        """Removes styx user role from a target."""
        role = get(ctx.guild.roles, id=RRPH.styx_user_role)
        try:
            await target.remove_roles(role)
            await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
        except Exception:
            await ctx.send(f"```py\n{traceback.format_exc()}\n```")


def setup(bot):
    bot.add_cog(Styx(bot))
