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

    @commands.command(aliases=['8ball', '8_ball', 'eightball', 'magic_conch'])
    async def eight_ball(self, ctx: commands.Context):
        """Let the magic eight ball decide your fate!"""
        await ctx.send(random.choice([
            "It is certain",
            "It is decidedly so",
            "Without a doubt",
            "Yes definitely",
            "You may rely on it",
            "As I see it, yes",
            "Most likely",
            "Outlook good",
            "Yes",
            "Signs point to yes",
            "Reply hazy try again",
            "Ask again later",
            "Better not tell you now",
            "Cannot predict now",
            "Concentrate and ask again",
            "Don't count on it",
            "My reply is no",
            "My sources say no",
            "Outlook not so good",
            "Very doubtful"
        ]))


def setup(bot):
    bot.add_cog(Misc(bot))
