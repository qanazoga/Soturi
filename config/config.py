import json
import time


class Config:

    with open("config/config.json", "r") as file:
        config = json.load(file)

    token = config["token"]
    ownerId = config["ownerId"]
    prefix = config["prefix"]
    invite = config["invite"]
    launch_time = time.time()


