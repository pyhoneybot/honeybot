# -*- coding: utf-8 -*-
"""
[random_color.py]
Random Color Plugin

[Author]
Jeet Trivedi

[About]
responds to .rancol, returns a color code

[Commands]
>>> .rancol
"""
from random import choice

class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info, bot_info):
        try:
            msg = info['args']
            if info['command'] == 'PRIVMSG' and msg[0]=='.rancol':
                random_col_msg = '^C'+ choice(range(16))+ ''.join(msg[1:]) +'^C'
                methods['send'](info['address'], random_col_msg)
        except Exception as e:
            print('woops plug',e)