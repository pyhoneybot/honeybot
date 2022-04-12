# -*- coding: utf-8 -*-
"""
[dadjoke.py]
Dad joke plugin

[Author]
moffetma Oregon State University CS

[About]
Sends a random "dad joke" from icanhazdadjoke.com

[Commands]
>>> .dadjoke
Have you heard of the band 1023MB? They haven't got a gig yet.
"""


import requests


class Plugin:
    def __init__(self):
        pass

    def dadjoke(self):
        headers = {"Accept": "application/json"}
        r = requests.get("https://icanhazdadjoke.com", headers=headers)
        j = r.json()
        joke = j["joke"]
        return joke

    def run(self, incoming, methods, info, bot_info):
        try:
            if info["command"] == "PRIVMSG" and info["args"][1] == ".dadjoke":
                methods["send"](info["address"], Plugin.dadjoke(self))
        except Exception as e:
            print("woops dadjoke plugin error", e)
