# -*- coding: utf-8 -*-
"""
[test.py]
Test Plugin

[Author]
Abdur-Rahmaan Janhangeer, pythonmembers.club

[About]
tests run
"""


class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info):
        # if '!~' in info['prefix']:
            # print(info)
        try:
            if info['command'] == 'PRIVMSG' and info['args'][1] == '.test':
                methods['send'](info['address'], 'test ok')
        except Exception as e:
            print('woops plug', e)
