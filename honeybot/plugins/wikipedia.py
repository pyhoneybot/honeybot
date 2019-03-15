# -*- coding: utf-8 -*-
"""
[wikipedia.py]
Wikipedia Plugin

[Author]
Gabriele Ron

[About]
sends a wikipedia article on request based off of a search or random query

[Commands]
>>> .wiki <command> <topic>
returns a wikipedia article
"""

import wikipedia

class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info):
        # if '!~' in info['prefix']:
            # print(info)
        try:
            if info['command'] == 'PRIVMSG' and info['args'][1] == '.wiki':
                if info['args'][2] == 'random':
                    article = wikipedia.page(wikipedia.random(1))
                    methods['send'](info['address'], article)
                elif info['args'][2] == 'search':
                    article = wikipedia.search(info['args'][3])
                    methods['send'](info['address'], article)
        except Exception as e:
            print('woops plug', e)
