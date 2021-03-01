# development of cointoss plugin for honeybot
"""
[Toss.py]
A plugin to toss a coin 

[Author]
Shriram Bhat

[About]
Responds to .cointoss, Returns head or tail at random 

[commands]
>>> .cointoss
returns head/ tail
"""

import random


class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info, bot_info):
        try:
            a = random.randint(0, 9)
            b = "It's Heads!"
            if a < 5:
                b = "It's Tails!"

            if info["command"] == "PRIVMSG" and info["args"][1] == ".cointoss":
                methods["send"](info["address"], b)
        except Exception as e:
            print("woops plug", e)
