from discord.ext import commands
import random
import os


class Memes:

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def kms(self, ctx):
        """Use when you have nothing left to do"""
        await self.bot.say(f"Will someone please put {ctx.message.author.mention} out of their misery?\n"
                           f"https://youtu.be/LTnq268y2ms?t=13s")

    @commands.command(pass_context=True)
    async def kys(self, ctx):
        """Give a user the final solution"""
        response = ""
        if len(ctx.message.mentions):
            response += "Hey, "
            for user in ctx.message.mentions:
                response += f"{user.mention}, "

            response += "here's some free advice:\n"

        response += random.choice(["https://youtu.be/ByC8sRdL-Ro", "https://youtu.be/2dbR2JZmlWo"])

        await self.bot.say(response)

    @commands.command(pass_context=True)
    async def pepe(self, ctx):
        """Sends a random pepe!"""
        source = ctx.message.channel
        path = './files/img/pepe/'
        await self.bot.send_typing(source)
        try:
            await self.bot.send_file(source, path + random.choice(os.listdir(path)))
        except Exception:
            await self.bot.say("I can't find my pepes ;~;")

    @commands.command(pass_context=True)
    async def mfw(self, ctx):
        """>MFW you don't know what this command does -.-
        sends a reaction image to the chat, we try to keep them optimized to fit as many situations as they can"""
        source = ctx.message.channel
        path = './files/img/mfw/'
        await self.bot.send_typing(source)
        try:
            await self.bot.send_file(source, path + random.choice(os.listdir(path)))
        except Exception:
            await self.bot.say("mfw I can't find my pics ;~;")


def setup(bot):
    bot.add_cog(Memes(bot))
