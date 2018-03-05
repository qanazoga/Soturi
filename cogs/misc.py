import random
from config.config import Config
from soturi_bot import SoturiBot
from discord.ext import commands
from discord import User, Embed, Colour
from time import time


class Misc:

    def __init__(self, bot: SoturiBot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """Gets the websocket latency for this bot (it's ping!)"""
        await ctx.send(f"{int(ctx.bot.latency*1000)}ms")

    @commands.command(aliases=['choose', 'pick'])
    async def choice(self, ctx: commands.Context, *args):
        """Picks between any number of things at random.

        Better than eenie-meenie-minie-moe, good for indecisive people."""
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

    @commands.command()
    async def avatar(self, ctx: commands.Context, *target: User):
        """Gets a user's profile picture.

        Can also be used to get avatars of multiple users at once!
        """
        await ctx.send("\n".join([member.avatar_url for member in target]))

    @commands.command()
    async def info(self, ctx: commands.Context):
        embed = Embed(colour=Colour(0xffa000))

        embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/241113397935079424/aec3e60e346f1626bb96ec65b44729d9.webp")

        creator = self.bot.get_user(Config.ownerId)
        embed.add_field(name="Creator:", value=f"{creator.name}#{creator.discriminator}")
        embed.add_field(name="Server Count:", value=len(self.bot.guilds))
        embed.add_field(name="Uptime:", value=self.uptime())
        embed.add_field(name="")
        embed.add_field(name="Invite Link", value=Config.invite, inline=False)

        await ctx.send(embed=embed)

    def uptime(self):

        total_seconds = time() - Config.launch_time

        # Helper vars:
        MINUTE = 60
        HOUR = MINUTE * 60
        DAY = HOUR * 24

        # Get the days, hours, etc:
        days = int(total_seconds / DAY)
        hours = int((total_seconds % DAY) / HOUR)
        minutes = int((total_seconds % HOUR) / MINUTE)
        seconds = int(total_seconds % MINUTE)

        # Build up the pretty string (like this: "N days, N hours, N minutes, N seconds")
        string = ""
        if days > 0:
            string += str(days) + " " + (days == 1 and "day" or "days") + ", "
        if len(string) > 0 or hours > 0:
            string += str(hours) + " " + (hours == 1 and "hour" or "hours") + ", "
        if len(string) > 0 or minutes > 0:
            string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes") + ", "
        string += str(seconds) + " " + (seconds == 1 and "second" or "seconds")

        return string


def setup(bot):
    bot.add_cog(Misc(bot))
