from soturi_bot import SoturiBot
from discord.ext import commands
import random


class RolePlaying:

    def __init__(self, bot: SoturiBot):
        self.bot = bot
        self.completed_rolls = []

    @commands.command()
    async def roll(self, ctx, roll="1d20", *args):
        self.completed_rolls = []
        repeat = 1
        and_index = 0

        if "/r" in args:
            repeat = int(args[args.index("/r") + 1])

        for i in range(repeat):
            self.roll_die(roll)

        for arg in args:
            if arg == "and":
                die_str = args[args.index("and", and_index) + 1]
                and_index = args.index(die_str)
                for i in range(repeat):
                    self.roll_die(die_str)

        if "/dl" in args:
            [item.remove(min(item)) for item in self.completed_rolls]

        if "/t" in args:
            totaled = f"Total: {sum([sum(item) for item in self.completed_rolls])}"
        else:
            totaled = ""

        await ctx.send(f"```{self.completed_rolls}\n{totaled}```")

    def roll_die(self, roll):
        number_of_dice = 1
        number_of_sides = 20
        buffer = ""
        for c in roll:
            print(buffer)
            if c != 'd':
                buffer += c
            else:
                number_of_dice = int(buffer)
                buffer = ""

        number_of_sides = int(buffer)

        rolls = []
        for j in range(number_of_dice):
            rolls.append(random.randint(1, number_of_sides))

        self.completed_rolls.append(rolls)


def setup(bot):
    bot.add_cog(RolePlaying(bot))
