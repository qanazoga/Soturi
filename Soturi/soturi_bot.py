import discord
from discord import Game
from discord.ext.commands import Bot
from os import listdir


class SoturiBot(Bot):

    async def on_ready(self):
        game = Game(name=f"{self.command_prefix}help")
        print(f"Successfully logged in as {self.user.name}")
        await self.change_presence(game=game)

    async def on_message(self, message: discord.Message):
        print(f"{message.author.name}: {message.content}")
        await self.process_commands(message)

    def reload_extensions(self):
        extensions = [file.replace(".py", "") for file in listdir("cogs")
                      if not file.endswith("__*") and file.endswith('.py')]

        for extension in extensions:
            try:
                self.load_extension(f"cogs.{extension}")
                print(f"Loaded {extension}")
            except Exception as e:
                print(f"[Failed to load extension {extension}!]:\n\t{e}")

