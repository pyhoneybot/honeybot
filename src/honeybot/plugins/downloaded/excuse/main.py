# -*- coding: utf-8 -*-
"""
[excuse.py]
Random excuse Plugin

[Author]
Rakesh Seal

[About]
Returns a random excuse for you.
[Website]


[Commands]
>>> .excuse
Returns a random excuse for you.
"""

import requests


class Plugin:
    def __init__(self):
        self.url = "https://excuser.herokuapp.com/v1/excuse"

    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info["args"][1:][0].split()
            if info["command"] == "PRIVMSG" and msgs[0] == ".excuse":
                excuse = requests.get(self.url).json()[0]["excuse"]
                methods["send"](info["address"], excuse)
        except Exception as e:
            print("No excuse for you!", e)
