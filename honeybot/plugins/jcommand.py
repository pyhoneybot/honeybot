# -*- coding: utf-8 -*-
"""
[.py]


[Author]
Abdur-Rahmaan Janhangeer, pythonmembers.club

[About]


[Commands]

"""
import random


class Plugin:
    def __init__(self):
        pass


    def run(self, incoming, methods, info):
        try:
            # if '!~' in info['prefix']:
                # print(info)
            msgs = info['args'][1:]
            if info['command'] == 'PRIVMSG' and msgs[0] == '.join':
                methods['join'](msgs[1])
        except Exception as e:
            print('woops plug', e)