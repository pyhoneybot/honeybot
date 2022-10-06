# -*- coding: utf-8 -*-
"""
[random_image.py]
Random Image Plugin

[Author]
Rakesh Seal

[About]
Returns a random image url.
[Website]


[Commands]
>>> .random_image
returns a random image url.
"""

import requests


class Plugin:
    def __init__(self):
        self.url = "https://random.imagecdn.app/v1/image?width=500&height=150&category=buildings&format=json"

    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info["args"][1:][0].split()
            if info["command"] == "PRIVMSG" and msgs[0] == ".random_image":
                image_url = requests.get(self.url).json()["url"]
                methods["send"](info["address"], image_url)
        except Exception as e:
            print("blank!", e)
