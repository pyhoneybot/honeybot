# -*- coding: utf-8 -*-
"""
[uptime.py]
Uptime Plugin

[Author]
Nick Wiley

[About]
Returns how long the bot has been running for

[Commands]
>>> .uptime
returns the bot uptime
"""

import time


class Plugin:
    def __init__(self):
        pass

    def __convert_time(start_time):
        """
        Calculates how long the bot has been running then formats the output
        """
        current_time = time.time()
        uptime = current_time - start_time
        hrs = int(uptime / 3600)
        uptime -= hrs * 3600
        mins = int(uptime / 60)
        uptime -= mins * 60
        sec = int(uptime)

        msg = "Bot has been up for {0} hr, {1} min, and {2} sec.".format(hrs, mins, sec)
        return msg

    def run(self, methods, info, bot_info):
        try:
            if info["command"] == "PRIVMSG" and info["args"][1] == ".uptime":
                start_time = bot_info["time"]
                methods["send"](info["address"], Plugin.__convert_time(start_time))
        except Exception as e:
            print("Plugin Error: ", e)
