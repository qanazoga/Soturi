import discord
from discord.ext.commands import Bot

from Soturi.message_handler import handle


class SoturiBot(Bot):

    async def on_ready(self):
        print(f"Successfully logged in as {self.user.name}.")
        print("---------------------------------\n")
        self.change_status(game=f"{self.command_prefix}help")

    async def on_message(self, message: discord.Message):
        print(f"{message.author.name} in {message.channel.name}:\n{message.content}\n")

        if message.author != self.user:
            await handle(self, message)
            await self.process_commands(message)

    async def on_command_error(self, exception, context):
        print(f"[COMMAND ERROR]:\n{exception}\n")

    async def on_error(self, exception, context):
        print(f"[GENERAL ERROR]:\n{exception}\n")