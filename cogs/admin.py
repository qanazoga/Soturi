import asyncio
import traceback
from config.rrph_config import RRPH
from soturi_bot import SoturiBot
from utils.checks import is_in_guild
from discord import Member
from discord.ext import commands
from discord.utils import get
from discord import Forbidden


class Admin(commands.Cog):

    def __init__(self, bot: SoturiBot):
        self.bot = bot

    async def __local_check(self, ctx):
        return await self.bot.is_owner(ctx.author)

    @commands.command()
    @is_in_guild(RRPH.id)
    async def sudo(self, ctx: commands.Context):
        """Gives you sudo permissions."""
        sudo = get(ctx.guild.roles, id=RRPH.sudo_role)

        if sudo in ctx.author.roles:
            await ctx.send("You're already `sudo`!")
            return

        await ctx.author.add_roles(sudo, reason="sudo")
        await ctx.message.add_reaction("👍")
        await asyncio.sleep(2)
        await ctx.message.delete()
        await asyncio.sleep(120)
        await ctx.author.remove_roles(sudo, reason="sudo time is up")

    @commands.group(invoke_without_command=True)
    async def clean(self, ctx: commands.Context, num: int=100):
            """Removes any number of messages (default 100)"""
            await ctx.channel.purge(limit=num+1)

    @clean.group()
    async def until(self, ctx: commands.Context, message_id: int):
        """Removes messages up until the given message, but not that one (up to 100)."""
        counter = 0
        async for message in ctx.history(limit=100):
            if message.id == message_id:
                await ctx.channel.purge(limit=counter)
                return
            else:
                counter += 1

        await ctx.send("That message couldn't be found in the last 100 messages!\n"
                       f"Try again after `{ctx.prefix}clean`?")

    @commands.command(aliases=["begone", "ban_spam"])
    async def ban_spammer(self, ctx, spammer: Member, *, reason=None):
        try:
            await ctx.guild.ban(spammer, reason=reason, delete_message_days=7)
        except Forbidden:
            await ctx.send(f'```\n{traceback.format_exc()}\n```')
        else:
            await ctx.send("bye felicia")

    @commands.command(hidden=True)
    async def load(self, ctx, *, module):
        """Loads a module."""
        try:
            self.bot.load_extension(module)
        except Exception:
            await ctx.send(f'```\n{traceback.format_exc()}\n```')
        else:
            await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')

    @commands.command(hidden=True)
    async def unload(self, ctx, *, module):
        """Unloads a module."""
        try:
            self.bot.unload_extension(module)
        except Exception:
            await ctx.send(f'```\n{traceback.format_exc()}\n```')
        else:
            await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')

    @commands.command(name='reload', hidden=True)
    async def _reload(self, ctx, *, module):
        """Reloads a module."""
        try:
            self.bot.unload_extension(module)
            self.bot.load_extension(module)
        except Exception:
            await ctx.send(f'```\n{traceback.format_exc()}\n```')
        else:
            await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')

    @commands.command()
    async def add_this_cog(self, ctx: commands.Context, path):
        """Adds a cog sent to the bot."""
        if len(ctx.message.attachments) < 1:
            return

        for cog in ctx.message.attachments:
            try:
                if cog.filename.endswith(".py"):
                    await cog.save(path+cog.filename)
                    await ctx.send(f"Added {path+cog.filename}")
            except Exception as e:
                await ctx.send(f"Failed on {path+cog.filename}\n`{e}`")


def setup(bot):
    bot.add_cog(Admin(bot))

