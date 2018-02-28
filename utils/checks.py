from discord.ext import commands


def is_in_guild(guild_id):
    async def predicate(ctx):
        return ctx.guild and ctx.guild.id == guild_id
    return commands.check(predicate)


def is_in_channel(channel_id):
    async def predicate(ctx):
        return ctx.channel.id == channel_id
    return commands.check(predicate)
