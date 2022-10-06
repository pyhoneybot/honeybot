# -*- coding: utf-8 -*-
"""
[url_shorten.py]
URL Shortener Plugin

[Author]
Rakesh Seal

[About]
Shorten an url with cleanuri and returns the smaller url.
[Website]


[Commands]
>>> .url_shorten <url>
Shorten an url with cleanuri and returns the smaller url.
"""

import requests


class Plugin:
    def __init__(self):
        self.url = "https://cleanuri.com/api/v1/shorten"

    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info["args"][1:][0].split()
            if info["command"] == "PRIVMSG" and msgs[0] == ".url_shorten":
                query = msgs[
                    1
                ]  # not entertaining multiple url. also assuming url is encoded i.e. no space will be there inside url.
                short_url = (
                    requests.post(self.url, json={"url": query})
                    .json()
                    .get("result_url", "")
                )
                methods["send"](info["address"], short_url)
        except Exception as e:
            print("unexpected error occured!", e)
