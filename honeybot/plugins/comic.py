# -*- coding: utf-8 -*-
"""
[comic.py]
Image search plugin

[Author]
Miguel Boekhold

[About]
Returns a random comic from xkcd

[Commands]
>>> .comic
returns a url of a random comic
"""

import requests
from random import randint


class Plugin:
    def __init__(self):
        pass

    def __comic():
        r = requests.get("http://xkcd.com/info.0.json")
        data = r.json()

        r = requests.get("http://xkcd.com/%d/info.0.json" % randint(1, data["num"]))
        data = r.json()
        image_url = data["img"]
        return image_url

    def run(self, incoming, methods, info, bot_info):
        try:
            if info["command"] == "PRIVMSG" and info["args"][1] == ".comic":
                methods["send"](info["address"], Plugin.__comic())
        except Exception as e:
            print("woops plugin error: ", e)
