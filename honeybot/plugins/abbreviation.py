# -*- coding: utf-8 -*-
"""
[abbreviation.py]
Abbreviation Plugin

[Author]
Erin Moon

[About]
responds to .def lol

[Commands]
>>> .def lol
returns lots of love
"""


class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info, bot_info):
        try:
            # if '!~' in info['prefix']:
                # print(info)
            if info['command'] == 'PRIVMSG' and info['args'][1] == '.def':
                if info['args'][2] == 'lol':
                    methods['send'](info['address'], 'lots of love')
        except Exception as e:
            print('woops, abbreviation plugin error', e)
