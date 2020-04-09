# -*- coding: utf-8 -*-
"""
[greet.py]
Greet Plugin

[Author]
Abdur-Rahmaan Janhangeer, pythonmembers.club

[About]
responds to .hi, demo of a basic plugin

[Commands]
>>> .hi
returns hoo
"""


class Plugin:
    def __init__(self):
        pass

    @staticmethod
    def run(incoming, methods, info, bot_info):

        try:
            # if '!~' in info['prefix']:
                # print(info)
            if info['command'] == 'PRIVMSG' and info['args'][1] == '.hi':
                methods['send'](info['address'], 'hooo')
        except Exception as e:
            print('woops plug', e)


