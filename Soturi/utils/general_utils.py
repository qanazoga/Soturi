from discord.ext import commands
from discord.utils import get


def convert_to_member(ctx: commands.Context, arg):
    """Attempts to convert a string to a member"""

    member = get(ctx.guild.members, name=arg)

    if member is not None:
        return member

    member = get(ctx.guild.members, id=arg)

    if member is not None:
        return member

    return member
