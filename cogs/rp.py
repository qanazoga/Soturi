from soturi_bot import SoturiBot
from discord.ext import commands
from discord import Embed
import random
import json


class RolePlaying:

    def __init__(self, bot: SoturiBot):
        self.bot = bot
        self.completed_rolls = []

    @commands.command()
    async def roll(self, ctx, roll="1d20", *args):
        args = list(args)
        self.completed_rolls = []
        repeat = 1
        and_index = 0

        if "/r" in args or "repeat" in args:
            repeat = int(args[args.index("/r") + 1])

        for i in range(repeat):
            self.roll_die(roll)

        for arg in args:
            if arg == "and":
                die_str = args[args.index("and", and_index) + 1]
                and_index = args.index(die_str)
                for i in range(repeat):
                    self.roll_die(die_str)

        if "/dl" in args or "drop_lowest" in args:
            [item.remove(min(item)) for item in self.completed_rolls]

        if "/dh" in args or "drop_highest" in args:
            [item.remove(max(item)) for item in self.completed_rolls]

        if "+" in args:
            [item.append(int(args[args.index("+", and_index) + 1])) for item in self.completed_rolls]
            args.append("/t")

        if "-" in args:
            [item.append(-int(args[args.index("-", and_index) + 1])) for item in self.completed_rolls]
            args.append("/t")

        if "/t" in args or "total" in args:
            totaled = f"Total: {sum([sum(item) for item in self.completed_rolls])}"
        else:
            totaled = ""

        if len(self.completed_rolls) == 1:
            self.completed_rolls = self.completed_rolls[0]

        await ctx.send(f"```{self.completed_rolls}\n{totaled}```")

    def roll_die(self, roll):
        number_of_dice = 1
        number_of_sides = 20
        rolls = []
        if roll != ".":
            buffer = ""
            for c in roll:
                if c != 'd':
                    buffer += c
                else:
                    number_of_dice = int(buffer)
                    buffer = ""

            number_of_sides = int(buffer)

        for j in range(number_of_dice):
            rolls.append(random.randint(1, number_of_sides))

        self.completed_rolls.append(rolls)

    @commands.command()
    @commands.has_role("narrator")
    async def say(self, ctx, who, *, msg):
        await ctx.message.delete()
        embed = Embed(title=who, description=msg)

        with open('cogs/cogdata/rp/avatars.json', 'r') as fp:
            data = json.load(fp)

        url = [item["URL"] for item in data if item["name"].lower() == who.lower()]

        if url:
            embed.set_thumbnail(url=url[0])

        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_role("narrator")
    async def add_char(self, ctx, name, url):
        await ctx.message.delete()

        with open('cogs/cogdata/rp/avatars.json', 'r') as fp:
            data = json.load(fp)

        with open('cogs/cogdata/rp/avatars.json', 'w') as fp:
            d = {"name": name, "URL": url}
            data.append(d)
            json.dump(data, fp)

    #@commands.command()
    #@commands.has_role() TODO
    async def rename_char(self, ctx, name, new_name):
        await ctx.message.delete()

        with open('cogs/cogdata/rp/avatars.json', 'r') as fp:
            data = json.load(fp)

        data = [item["name"] for item in data if item["name"].lower() == name.lower()]

def setup(bot):
    bot.add_cog(RolePlaying(bot))
