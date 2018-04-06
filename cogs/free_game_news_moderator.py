from config.rrph_config import RRPH
from discord import Message
from discord.utils import get


class FreeGameNewsModerator:

    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message: Message):
        if message.channel.id != RRPH.free_game_news_channel:
            return

        fgnr = get(message.guild.roles, id=RRPH.free_game_news_role)

        if fgnr in message.role_mentions and 'http' in message.clean_content:
            return

        await message.delete()

        ch = await message.author.create_dm()
        await ch.send("Your message has been removed from #free-game-news\n"
                      "Please remember to include a link to the game, "
                      "and a mention `@free-game-news` to prevent this in the future.")



def setup(bot):
    bot.add_cog(FreeGameNewsModerator(bot))