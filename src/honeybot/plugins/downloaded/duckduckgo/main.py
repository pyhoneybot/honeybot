# -*- coding: utf-8 -*-
"""
[duckduckgo.py]
Duckduckgo Plugin

[Author]
Rakesh Seal

[About]
Returns a abstract of the search query from a duckduckgo Search. Return empty if no abstract found.
[Website]


[Commands]
>>> .duck <query>
returns abstrack from duckduckgo search
"""

import requests


class Plugin:
    def __init__(self):
        pass

    def __gen_url_from_query(self, query):
        return "https://duckduckgo.com/?q=" + query + "&format=json&pretty=1"

    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info["args"][1:][0].split()
            if info["command"] == "PRIVMSG" and msgs[0] == ".duck":
                query = " ".join(msg for msg in msgs[1:])
                duck_abstract = requests.get(self.__gen_url_from_query(query)).json()["Abstract"]
                methods["send"](info["address"], duck_abstract)
        except Exception as e:
            print("quack quack!", e)
