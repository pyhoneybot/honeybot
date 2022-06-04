# -*- coding: utf-8 -*-
"""
[log.py]
Log Plugin

[Author]
Gico Carlo Evangelista, https://gicocarlo.me/

[About]
Logs the chat into a log.txt file
"""

# UPDATE: 13/4/2019
# Due to logging module in main.py, log.py will now log the chat using
# standard python file handling

import os
from datetime import datetime

# Makes a new log dir if not existent
# Change according to where you have honeybot dir
log_path = "{}/log".format(os.getcwd())
if not os.path.exists(log_path):
    os.makedirs("log")

# Current date
curr_date = datetime.today().strftime("%d-%m-%Y")


class Plugin:
    def __init__(self):
        pass

    def run(self, methods, info, bot_info):
        msgs = info["args"][1:]
        try:
            if info["command"] == "PRIVMSG":
                # Make log file (if not existent) using current date
                f = open("log/{}.txt".format(curr_date), "a+")

                # Current time
                curr_time = datetime.now().strftime("%H:%M:%S")

                # Parse the user ID from info['prefix']
                raw_user = info["prefix"]
                user_index = raw_user.find("!")
                user = raw_user[0:user_index]

                # Logging the chat into txt file
                f.write("{}: {}: {}\r\n".format(curr_time, user, msgs[0]))

        except Exception as e:
            print("woops plugin error ", e)
