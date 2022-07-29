# -*- coding: utf-8 -*-
"""
[story.py]
Story Plugin

[Author]
Tuan Thai

[About]
Sends a random story
Sourced stories from
http://www.read.gov/aesop/001.html

[Commands]
>>> .story
returns random story
"""

import random

import requests
from bs4 import BeautifulSoup


class Plugin:
    def __init__(self):
        pass

    def story(self):
        number = random.randint(2, 147)
        if number < 10:
            story = "00" + str(number)
        elif number < 100:
            story = "0" + str(number)
        else:
            story = str(number)

        story_url = requests.get("http://www.read.gov/aesop/" + story + ".html")
        soup = BeautifulSoup(story_url.content, "html.parser")
        texts = soup.find("div", {"id": "page"})
        for paragraph in texts.findAll("p"):
            return str(paragraph.text)

    def run(self, incoming, methods, info, bot_info):
        try:
            if info["command"] == "PRIVMSG" and info["args"][1] == ".story":
                methods["send"](info["address"], Plugin.story(self))
        except Exception as e:
            print("woops plugin error: ", e)
