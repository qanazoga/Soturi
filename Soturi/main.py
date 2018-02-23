from Soturi.config.config import Config
from Soturi.soturi_bot import SoturiBot

config = Config()
bot = SoturiBot(config.prefix)

bot.reload_extensions()

bot.run(config.token)
