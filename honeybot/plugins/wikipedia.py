# -*- coding: utf-8 -*-
"""
[wikipedia.py]
Wikipedia Plugin

[Author]
Gabriele Ron

[About]
sends a wikipedia article on request based off of a search or random query
requires wikipedia library. Can use pip -> "pip install wikipedia"

[Website]
https://Macr0Nerd.github.io

[Commands]
>>> .wiki <command> <topic>
returns a wikipedia article
"""

import wikipedia

class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info, bot_info):
        # if '!~' in info['prefix']:
            # print(info)
        try:
            msgs = info['args'][1:][0].split()

            if info['command'] == 'PRIVMSG' and msgs[0] == '.wiki':
                if msgs[1] == 'random':
                    print("You want the random article!")

                    article = wikipedia.page(wikipedia.random(1)).summary
                    methods['send'](info['address'], article)
                elif msgs[1] == 'search':
                    print(f"You wanted {msgs[2]}")

                    article = wikipedia.page(msgs[2]).summary
                    methods['send'](info['address'], article)
        except Exception as e:
            print('woops plug', e)