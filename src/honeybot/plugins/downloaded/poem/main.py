# -*- coding: utf-8 -*-
"""
[poem.py]
say poem Plugin

[Author]
Komeil Parseh

[About]
say a random poem with the given language('en' by default)

[Commands]
>>> .poem <lang>
return a random poem in the given language
"""

import json

try:
    import requests
except ImportError:
    print("No module named 'requests' found")


class Plugin:
    def __init__(self):
        pass

    @staticmethod
    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info["args"][1:][0].split()

            if info["command"] == "PRIVMSG":
                if len(msgs) > 1:
                    if msgs[0] == ".poem":
                        if len(msgs < 2):
                            msgs[1] = "en"
                        methods["send"](info["address"], random_poem(msgs[1]))
        except Exception as ex:
            print("woops plugin", __file__, ex)

    @property
    def random_poem(language: str) -> str:

        if language == "en":
            content = json.loads(requests.get("https://poetrydb.org/random").content)[0]

            return f"{content['title']} - {content['author']}" + "\n".join(
                content["lines"]
            )
        elif language == "fa":
            content = json.loads(
                requests.get("http://c.ganjoor.net/beyt-json.php").content
            )

            return (
                f"شاعر {content['poet']}"
                + f"\n\n{content['m1']} "
                + f" {content['m2']}"
                + f"\nلینک: {content['url']}"
            )
        else:
            return "ERROR: language not supported"
