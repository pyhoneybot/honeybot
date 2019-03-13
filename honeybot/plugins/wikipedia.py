# -*- coding: utf-8 -*-
"""
[wikipedia.py]
Wikipedia Plugin

[Author]
Gabriele Ron

[About]
sends a random wikipedia article on request

[Commands]
>>> .wiki
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
                article = wikipedia.page(wikipedia.random(1))
                methods['send'](info['address'], article)
        except Exception as e:
            print('woops plug', e)
