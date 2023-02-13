"""
[date.py]
Date Plugin

[Author]
Gico Carlo Evangelista, https://gicocarlo.me/

[About]
Will post the current date

[Commands]
>>> .date today
returns the current date
"""

from datetime import date


class Plugin:
    def __init__(self):
        pass

    # Date attribute
    # Returns date in string format
    def __date():
        curr_date = date.today()
        day = curr_date.strftime("%d")
        month = curr_date.strftime("%B")
        year = curr_date.strftime("%Y")
        return f"Today is {month} {day}, {year}"

    def run(self, incoming, methods, info, bot_info):
        try:
            if info["command"] == "PRIVMSG" and info["args"][1] == ".date today":
                methods["send"](info["address"], Plugin.__date())
        except Exception as e:
            print("woops plug", e)
