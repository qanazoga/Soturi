import random
from Soturi.config.config import Config
from Soturi.soturi_bot import SoturiBot
from discord.ext import commands


class Misc:

    def __init__(self, bot: SoturiBot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send(f"{int(ctx.bot.latency*1000)}ms")

    @commands.command()
    async def get_invite(self, ctx: commands.Context):
        await ctx.send(Config.invite)

    @commands.command(aliases=['choose', 'pick'])
    async def choice(self, ctx: commands.Context, *args):
        await ctx.send(random.choice(args))


def setup(bot):
    bot.add_cog(Misc(bot))
