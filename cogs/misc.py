import random
from config.config import Config
from soturi_bot import SoturiBot
from discord.ext import commands
from discord import User, Embed, Colour, File, utils
from asyncio import sleep
from time import time
from glob import glob
from re import sub


class Misc(commands.Cog):

    def __init__(self, bot: SoturiBot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """Gets the websocket latency for this bot (its ping!)"""
        await ctx.send(f"{int(ctx.bot.latency*1000)}ms")

    @commands.command(aliases=['choose', 'pick'])
    async def choice(self, ctx: commands.Context, *args: commands.clean_content()):
        """Picks between any number of things at random.

        Better than eenie-meenie-minie-moe, good for indecisive people."""
        await ctx.send(f"I choose:\n\n\t`{random.choice(args)}`")

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

    @commands.command(aliases=["avatar"])
    async def get_avatar(self, ctx: commands.Context, *target: User):
        """Gets a user's profile picture.

        Can also be used to get avatars of multiple users at once!
        """
        await ctx.send("\n".join([member.avatar_url for member in target]))

    @commands.command(aliases=['tfw', 'mrw'])
    @commands.cooldown(1, 120, type=commands.BucketType.user)
    async def mfw(self, ctx):
        """>mfw you don't know what this command does -.-
        Sends a reaction image to the chat, we try to keep them optimized to fit as many situations as they can
        Has a 2 minute cooldown on a per-user basis to prevent annoying spamming."""
        file_name_glob = 'cogs/cogdata/mfw/*'

        try:
            async with ctx.channel.typing():
                await ctx.send(file=File(random.choice(glob(file_name_glob))))
        except Exception:
            await ctx.send("mfw I can't find my pics ;~;")

    @commands.command(aliases=['addmfw'])
    @commands.is_owner()
    async def add_mfw(self, ctx):
        """Adds an attached picture to the reaction picture collection."""
        if not ctx.message.attachments:
            await ctx.send("There's no picture here!")
            await ctx.message.add_reaction("👎")
            return

        for file in ctx.message.attachments:
            await file.save(f"cogs/cogdata/mfw/{file.filename}")

        await ctx.message.add_reaction("👍")

    @commands.command(aliases=["template", "react"])
    async def create_reaction_template(self, ctx: commands.Context, reaction_text: str, message_id: int):
        """Tries to add a text in the form of reaction emoji to a given message. CLICK THE THINGS!!!

        This is for TEMPLATING, not leaving messages with the bot. Soturi will remove its reactions after 20 seconds,
        make sure to add yours in that time.

        Try is the keyword, this can fail for multiple reasons, including the use of the same letter multiple times in
        your text, or the letter already being used in the reactions on that message.

        In the future message_id may be an optional parameter, defaulting to the message before yours.
        """
        msg = await ctx.channel.get_message(message_id)
        reaction_text = sub(r"[^A-Z0-9]", "", reaction_text.upper())

        if len(reaction_text) != (len(set(reaction_text))):
            await ctx.message.add_reaction("❌")
            await ctx.channel.send("Your message contains letters used more than once, "
                                   "but you can't do this with reactions\n*you might need to get a little creative*",
                                   delete_after=30)
            return

        emoji_queue = []
        for char in reaction_text.upper():
            emoji_queue.append(self.character_to_emoji(char))

        if [reaction.emoji for reaction in msg.reactions if reaction.emoji in emoji_queue]:
            await ctx.message.add_reaction("❌")
            await ctx.send("The message already has one of the reaction letters you need!", delete_after=30)
            return

        for emoji in emoji_queue:
            await msg.add_reaction(emoji)

        await sleep(15)

        for emoji in emoji_queue:
            await msg.remove_reaction(emoji, ctx.guild.me)

        try:
            await ctx.message.delete()
        except:
            pass  # if we get to this point, it's fine if we can't delete the message, usually just don't have perms

    @commands.command()
    async def vote(self, ctx):
        """Adds an up and down vote reaction to your message.

        >vote to call this the best command, anyone?"""
        await ctx.message.add_reaction("⬆")
        await ctx.message.add_reaction("⬇")

    @commands.command(aliases=["uptime", "invite"])
    async def info(self, ctx: commands.Context):
        """Gets a bunch of info about the bot."""
        embed = Embed(colour=Colour(0xffa000))

        embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/241113397935079424/aec3e60e346f1626bb96ec65b44729d9.webp")

        creator = self.bot.get_user(Config.ownerId)
        embed.add_field(name="Creator:", value=f"{creator.name}#{creator.discriminator}")
        embed.add_field(name="Server Count:", value=str(len(self.bot.guilds)))  # hush, I got tired of the yellow line
        embed.add_field(name="Uptime:", value=self.uptime())
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

    def character_to_emoji(self, character):
        return f"{character}\u20E3" if character.isdigit() else chr(0x1f1e6 + ord(character.upper()) - 0x41)


def setup(bot):
    bot.add_cog(Misc(bot))

