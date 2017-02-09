import random
import json


async def handle(bot, message):
    lcmessage = message.content.lower()

    if (
        "fuck u" in lcmessage or
        "fuk u" in lcmessage or
        "fuq u" in lcmessage or
        "fuc u" in lcmessage or
        "fuck you" in lcmessage or
        "fuk you" in lcmessage or
        "fuq you" in lcmessage or
        "fuc you" in lcmessage or
        "hh q" in lcmessage or
        "fh q" in lcmessage
    ):
        await bot.send_message(message.channel, "fuck u")

    if (
        "member when" in lcmessage or
        "member "in lcmessage and "?" in lcmessage
    ):
        await bot.send_message(message.channel, random.choice(["Ooh, I 'member!", "Yeah, I 'member!"]))

    if (
        "what" in lcmessage and "ur" in lcmessage and "name" in lcmessage
    ):
        await bot.send_message(message.channel, "My real name is " + get_real_name())

    if message.author.id == get_author() and ">freeze" in lcmessage:
        bot.freeze_mode = not bot.freeze_mode
        await bot.send_message(message.author, f"FREEZE MODE: {bot.freeze_mode}")


def get_real_name():
    with open("./config.json") as file:
        return json.load(file)["real_name"]


def get_author():
    with open("./config.json") as file:
        return json.load(file)["author_id"]
