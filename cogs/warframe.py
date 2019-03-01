from discord.ext import commands
from soturi_bot import SoturiBot
from config.rrph_config import RRPH
from discord import Embed, Colour, Member
import urllib.request as request
import traceback
import feedparser
import json
import asyncio
import time


class Warframe:

    def __init__(self, bot: SoturiBot):
        self.bot = bot
        self.bot.loop.create_task(self.check_warframe_rss())

    async def check_warframe_rss(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            feed = feedparser.parse("http://content.warframe.com/dynamic/rss.php")
            entries = feed.entries
            saved_items = [line.strip() for line in open('cogs/cogdata/warframe/guids.txt')]
            new_items = [entry for entry in entries if entry.guid not in saved_items]
            warframe_channel = self.bot.get_channel(RRPH.warframe_alerts_channel)
            with open('cogs/cogdata/warframe/needs.json', 'r') as fp:
                data = json.load(fp)
                registered_users = [item for item in data]

            for rssItem in new_items:
                members_that_want = []
                for member in warframe_channel.members:
                    if str(member.id) in registered_users:
                        if [want for want in data[str(member.id)] if want in rssItem.title.lower()]:
                            members_that_want.append(member.mention)

                if members_that_want:
                    embed = Embed(title=rssItem.title, colour=self.get_color(rssItem.author))
                    embed.set_footer(text=rssItem.guid)

                    await warframe_channel.send(f"{' '.join(set(members_that_want))}", embed=embed)

            saved_items = [entry.guid for entry in feed.entries]
            with open('cogs/cogdata/warframe/guids.txt', 'w') as fp:
                [fp.write(f"{item}\n") for item in saved_items]

            await asyncio.sleep(10)

    @commands.group(name='wf')
    @commands.has_role(name="warframe")
    async def warframe(self, ctx):
        """[GROUP] of Warframe related commands. Mostly Alert System.

        Some items in Warframe only come from alerts, or are annoying to get anywhere else,
        but alerts happen all day, and only a few have things you want, while the others are complete trash.
        use the `subscribe` command to subscribe to just the alerts about the items you want.
        """
        ...

    @warframe.command(aliases=['sub'])
    async def subscribe(self, ctx, *needs):
        """Subscribe to all references of anything you need in all alerts, invasions, or otherwise!

        If there are spaces in your needed item, put quotes around the whole thing. ex:
        wf subscribe "orokin reactor"

        You can subscribe to receive multiple items at a time; space seperate them, and follow the previous rule, ex:
        wf subscribe "orokin reactor" "orokin catalyst" "forma"

        (in this example, 'forma' technically did not need quotes, since it has no spaces, but ¯\_(ツ)_/¯)
        """
        needs = [need.lower() for need in needs]

        with open('cogs/cogdata/warframe/needs.json', 'r') as fp:
            data = json.load(fp)

        try:
            if str(ctx.author.id) not in [ids for ids in data]:
                with open('cogs/cogdata/warframe/needs.json', 'w') as fp:
                    data.setdefault(str(ctx.author.id), []).extend(needs)
                    json.dump(data, fp)
                    await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
            else:
                with open('cogs/cogdata/warframe/needs.json', 'w') as fp:
                    data[str(ctx.author.id)].extend(needs)
                    json.dump(data, fp)
                    await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')

        except Exception:
            await ctx.send(f'```\n{traceback.format_exc()}\n```')

    @warframe.command(aliases=['unsub'])
    async def unsubscribe(self, ctx, need):
        """Unsubscribe from an item you're subscribed to."""
        with open('cogs/cogdata/warframe/needs.json') as fp:
            data = json.load(fp)

        if need in data[str(ctx.author.id)]:
            try:
                with open('cogs/cogdata/warframe/needs.json', 'w') as fp:
                    data[str(ctx.author.id)].remove(need)
                    json.dump(data, fp)
                    await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
            except Exception:
                await ctx.send(f'```\n{traceback.format_exc()}\n```')
        else:
            await ctx.send(f"You aren't subscribed to `{need}`.")

    @warframe.command(aliases=['getsubs', 'get_subs', 'subs'])
    async def get_subscriptions(self, ctx):
        """List all items you're subscribed to."""
        with open('cogs/cogdata/warframe/needs.json') as fp:
            data = json.load(fp)
            await ctx.send(data[str(ctx.author.id)])

    @warframe.group(invoke_without_command=True)
    async def poe(self, ctx):
        """Get the time on Cetus and Plains of Eidolon, or Alert yourself for the next night"""
        origin = 1518558300 # 1518342300
        minutes_into_cycle = int((time.time() - origin) / 60 % 150)
        if minutes_into_cycle < 50:
            embed = Embed(title=f"It's night, {50 - minutes_into_cycle} minutes left", colour=Colour(0x000000))
        else:
            embed = Embed(title=f"It's day, {150 - minutes_into_cycle} minutes left", colour=Colour(0xffffff))
        await ctx.send(embed=embed)

    @poe.command(aliases=["alert"])
    async def alert_me(self, ctx):
        """Get a one time alert that night is coming to the plains"""
        origin = 1518558300 # 1518342300
        minutes_into_cycle = int((time.time() - origin) / 60 % 150)
        time_left = 150 - minutes_into_cycle

        if time_left <= 10:
            await ctx.send(f"Night hasn't started yet, but there's only {time_left} minutes left!")
        else:
            await ctx.send(f"The next night starts in {150 - minutes_into_cycle}m.\n"
                           f"Setting a timer for {150 - minutes_into_cycle - 10}m.")

            await self.poe_alert((150 - minutes_into_cycle - 10) * 60, ctx.author)

    @warframe.command(aliases=["fis"])
    async def fissures(self, ctx):
        """Shows the current location of Void Fissures"""
        url = "https://ws.warframestat.us/pc"
        req = request.Request(url, headers={'User-Agent': "Magic Browser"})
        con = request.urlopen(req)
        data = json.loads(con.read().decode("utf-8"))
        fissures = sorted(data['fissures'], key=lambda k: k['tierNum'])
        pl = []
        for item in fissures:
            pl.append(f"```asciidoc\nLocation :: {item['node']}\nRelic :: {item['tier']}\n"
                      f"Mission :: {item['missionType']}\nTime Remaining :: {item['eta']}\n```")

        await ctx.send("".join(pl))

    async def poe_alert(self, time_left, member: Member):
        await asyncio.sleep(time_left)
        wf = self.bot.get_channel(RRPH.warframe_alerts_channel)
        await wf.send(f"{member.mention}, only 10 minutes until night!")

    def get_color(self, mission_type):
        return {
            "Alert": Colour(0xff0000),
            "Invasion": Colour(0x000001),
            "Outbreak": Colour(0x00ff00)
        }.get(mission_type)


def setup(bot):
    bot.add_cog(Warframe(bot))
