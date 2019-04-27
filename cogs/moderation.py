from config.rrph_config import RRPH
from soturi_bot import SoturiBot
from discord.ext import commands
from discord.utils import get
from discord import Member
from asyncio import TimeoutError


class Moderation:

    def __init__(self, bot: SoturiBot):
        self.bot = bot

    @commands.command()
    @commands.has_role('mod')
    @commands.guild_only()
    async def kick(self, ctx: commands.Context, target: Member, *, reason):
        """Begin the kicking process for a member.

        After you start the kick process, there is 5 minutes of time for any other mod to confirm the kick.
        Make sure you include a reason for the kick."""
        mod_role = get(ctx.guild.roles, id=RRPH.mod_role)
        reason = "".join(reason)

        def check(reaction, user):
            return str(reaction.emoji) == '🛑' and mod_role in user.roles and user != ctx.author

        await ctx.message.delete()
        msg = await ctx.send(f"{mod_role.mention}\n"
                             f"{target.mention} is to be kicked for:"
                             f"```fix\n{reason}```"
                             f"Needs one more mod to confirm action (others may react to show support for the motion).")

        await msg.add_reaction('🛑')

        try:
            await ctx.bot.wait_for('reaction_add', timeout=60.0*5, check=check)
        except TimeoutError:
            await msg.delete()
        else:
            await target.kick(reason=reason)

    @commands.command()
    @commands.has_role('mod')
    @commands.guild_only()
    async def ban(self, ctx: commands.Context, target: Member, *, reason):
        """Begin the ban process for a member.

        After you start the ban process, there is 5 minutes of time for any other mod to confirm the ban.
        Make sure you include a reason for the ban."""
        mod_role = get(ctx.guild.roles, id=RRPH.mod_role)
        reason = "".join(reason)

        def check(reaction, user):
            return str(reaction.emoji) == '🛑' \
                   and mod_role in user.roles \
                   and user != ctx.author \
                   and reaction.message.id == msg.id

        await ctx.message.delete()
        msg = await ctx.send(f"{mod_role.mention}\n"
                             f"{target.mention} is to be **BANNED** for:"
                             f"```diff\n- {reason}```"
                             f"Needs one more mod to confirm action (others may react to show support for the motion).")

        await msg.add_reaction('🛑')

        try:
            await ctx.bot.wait_for('reaction_add', timeout=60.0 * 5, check=check)
        except TimeoutError:
            await msg.delete()
        else:
            await target.ban(reason=reason)


    @commands.command()
    @commands.has_role('mod')
    @commands.guild_only()
    async def silence(self, ctx: commands.Context, target: Member, *, reason):
        """Remove all roles from someone"""
        reason = "".join(reason)
        roles = []

        for role in target.roles:
            if (role.id != "376461381702254613") and \
                    (role.id != "376461598459559937") and \
                    (role.id != "411060339908542465") and \
                    (role.id != "235187792265609217"):
                roles.append(role)

        target.remove_roles(roles, reason)
        ch = target.create_dm()
        await ch.send("Oopsie woopsie, wooks wike someone fogwot the woows!\nPwease, we-wead the wuwes! \n" +
                "We don't want another fucksie-wucksie wike dis again! uwu\n" +
                "(Reread rules 1, 2, and 3. Stop being a dick)")


def setup(bot):
    bot.add_cog(Moderation(bot))
