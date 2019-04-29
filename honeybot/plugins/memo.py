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

    def run(self, incoming, methods, info):
        try:
            msgs = info['args'][1:][0].split()
            if info['command'] == 'PRIVMSG' and msgs[0] == '.memo' and \
                    msgs[1] == 'add':
                methods['mem_add']('global', 'VALUES', msgs[2], msgs[3])
            if info['command'] == 'PRIVMSG' and msgs[0] == '.memo' and \
                    msgs[1] == 'rem':
                methods['mem_rem']('global', 'VALUES', msgs[2])
            if info['command'] == 'PRIVMSG' and msgs[0] == '.memo' and \
                    msgs[1] == 'fetch':
                try:
                    val = methods['mem_fetch']('global', 'VALUES', msgs[2])
                    methods['send'](info['address'], val)
                except KeyError:
                    methods['send'](info['address'], 'value not found')
                
        except Exception as e:
            print('woops plug', e)
