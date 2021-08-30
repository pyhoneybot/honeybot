# -*- coding: utf-8 -*-
"""
[channeljoin.py]
Join Plugin

[Author]
Marcelo Benesciutti

[About]
Bot Will join a given channel in the server

[Commands]
>>> .channeljoin channel
bot joins the given channel
"""


class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info["args"][1:][0].split()
            if info["command"] == "PRIVMSG" and msgs[0] == ".channeljoin":
                raw_user = info["prefix"]
                user_index = raw_user.find("!")
                user = raw_user[0:user_index]
                with open("settings/OWNERS.conf", "r") as f:
                    for owner in f:
                        if owner.strip() == user:
                            methods["join"](msgs[1])
                            break
                    else:
                        methods["send"](
                            info["address"],
                            "only bot owners can execute this function, "
                            + "make sure your IRC nickname is in the settings/OWNERS.conf file",
                        )

        except Exception as e:
            print("woops plugin error: ", e)
