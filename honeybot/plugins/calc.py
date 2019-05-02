# -*- coding: utf-8 -*-
"""
[calc.py]
Maths Operation Plugin

[Author]
Abdur-Rahmaan Janhangeer, pythonmembers.club

[About]
evaluates maths expressions in the format supported by py

[Commands]
>>> .calc <maths expression>
returns evaluated expression
"""
from string import ascii_letters


class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info['args'][1:][0].split()

            if info['command'] == 'PRIVMSG':
                if len(msgs) > 1:
                    if msgs[0] == '.calc':
                        expr = msgs[1]
                        for c in ascii_letters:
                            expr = '' + expr.replace(c, '')
                        methods['send'](info['address'], '{}'.format(
                                eval(expr))
                        )
        except Exception as e:
            print('woops plugin', __file__, e)
