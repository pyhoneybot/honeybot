# -*- coding: utf-8 -*-
"""
[onthisday.py]
On This Day
[Author]
Kenneth Gargan
[About]
Gets an interesting fact about today!
[Commands]
>>> .onthisday
returns fact's about today
"""

import requests
import datetime
import json
import random

# URL where we are getting the facts from:
URL = "https://byabbe.se/on-this-day/"


class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info, bot_info):
        try:
            if info["command"] == "PRIVMSG" and info["args"][1] == ".onthisday":
                # Make the request and include the month and day
                dt = datetime.datetime.today()
                r = requests.get(
                    "https://byabbe.se/on-this-day/" +
                    str(dt.month) +
                    "/" +
                    str(dt.day) +
                    "/events.json"
                )

                events = json.loads(r.content)
                # Pick out a random fact to print
                randomChoice = random.choice(events["events"])
                onthisday = (
                    "On this day in" +
                    randomChoice["year"] +
                    "," +
                    randomChoice["description"] +
                    "Read more @" +
                    randomChoice["wikipedia"][0]["wikipedia"]
                )
                methods["send"](info["address"], onthisday)

        except Exception as e:
            print("woops plugin error ", e)
