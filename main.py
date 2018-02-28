#!/usr/bin/env python3

from config.config import Config
from soturi_bot import SoturiBot

config = Config()
bot = SoturiBot(config.prefix)

bot.reload_extensions()
bot.run(config.token)
