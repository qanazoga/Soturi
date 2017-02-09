import json
import traceback

from Soturi.bot import SoturiBot

with open("files/config") as file:
    config = json.load(file)

token = config["token"]
prefix = config["prefix"]

bot = SoturiBot(prefix)

for extension in ('soturi_commands',):
    try:
        bot.load_extension(extension)
    except ModuleNotFoundError:
        traceback.print_exc()

bot.pm_help = True
bot.run(token)
bot.session.close()
