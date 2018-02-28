from discord.ext import commands
from discord.utils import get


def convert_to_member(ctx: commands.Context, target):
    """Attempts to convert a string to a member"""

    member = get(ctx.guild.members, name=target)

    if member is not None:
        return member

    member = get(ctx.guild.members, id=target)

    if member is not None:
        return member

    return member
