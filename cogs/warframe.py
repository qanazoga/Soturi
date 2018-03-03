from discord.ext import commands
from soturi_bot import SoturiBot
from config.rrph_config import RRPH
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
            warframe_channel = self.bot.get_channel(419555992448008192)  # TODO: THIS IS ONLY A TEMPORARY FIX
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
                    await warframe_channel.send(f"{' '.join(set(members_that_want))},\n"
                                                f"**I think you might want this!**\n"
                                                f"{rssItem.title}")

            saved_items = [entry.guid for entry in feed.entries]
            with open('cogs/cogdata/warframe/guids.txt', 'w') as fp:
                [fp.write(f"{item}\n") for item in saved_items]

            await asyncio.sleep(10)

    @commands.group(name='wf')
    async def warframe(self, ctx):
        """qanazoga's Warframe Alert System

        qanazoga's pride and joy: Some items in Warframe only come from alerts, or are annoying to get anywhere else,
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
                    data[str(ctx.author.id)] = [needs]
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

    @warframe.command()
    async def poe(self, ctx):
        """Get the time on Cetus and Plains of Eidolon"""
        first_day = 1518342840
        now = int(time.time())


def setup(bot):
    bot.add_cog(Warframe(bot))
