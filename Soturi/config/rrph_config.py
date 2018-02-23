import json


class RRPH:

    with open("config/rrph_config.json") as file:
        rrph = json.load(file)

    id = rrph["id"]

    sudoRole = rrph["sudo_role"]
    adminRole = rrph["admin_role"]
    modRole = rrph["mod_role"]

    styxAdminRole = rrph["styx_admin_role"]
    styxUserRole = rrph["styx_user_role"]

    welcomeChannel = rrph["welcome_channel"]
    freeGameNewsChannel = rrph["free_game_news_channel"]
