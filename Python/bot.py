import discord
import json
import traceback
from discord.ext.commands import Bot
from scripts.message_handler import handle


class SoturiBot(Bot):
    freeze_mode = False

    async def on_ready(self):
        print(f"Successfully logged in as {self.user.name}.")
        print("---------------------------------\n")
        self.change_status(game=f"{self.command_prefix}help")

    async def on_message(self, message: discord.Message):
        print(f"{message.author.name} in {message.channel.name}:\n{message.content}\n")

        if message.author != self.user:
            await handle(self, message)
            if not self.freeze_mode:
                print(self.freeze_mode)
                await self.process_commands(message)

    async def on_command_error(self, exception, context):
        print(f"[COMMAND ERROR]:"), traceback.print_exc()

    async def on_error(self, exception, context):
        print("[GENERAL ERROR]:"), traceback.print_exc()


with open("config.json") as file:
    config = json.load(file)

token = config["token"]
prefix = config["prefix"]

bot = SoturiBot(prefix)

for extension in ('cogs.soturi_commands',):
    try:
        bot.load_extension(extension)
    except ModuleNotFoundError:
        print(f"[MODULE NOT FOUND!]: {extension}"), traceback.print_exc()

bot.pm_help = True
bot.run(token)
bot.session.close()
