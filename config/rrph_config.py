import json


class RRPH:

    with open("config/rrph_config.json") as file:
        rrph = json.load(file)

    id = rrph["id"]

    sudo_role = rrph["sudo_role"]
    admin_role = rrph["admin_role"]
    mod_role = rrph["mod_role"]

    styx_admin_role = rrph["styx_admin_role"]
    styx_user_role = rrph["styx_user_role"]

    free_game_news_role = rrph["free_game_news_role"]

    welcome_channel = rrph["welcome_channel"]
    free_game_news_channel = rrph["free_game_news_channel"]
    warframe_channel = rrph["warframe_channel"]
    warframe_alerts_channel = rrph["warframe_alerts_channel"]
    bot_dev_channel = rrph["bot_dev_channel"]
    mod_chat_channel = rrph["mod_chat_channel"]

    iconoclasm = rrph["iconoclasm"]
