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
from math import *

class Plugin:
    def __init__(self):
        self.safe_functs = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos',
                 'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor',
                 'fmod', 'frexp', 'hypot', 'ldexp', 'log', 'log10',
                 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt',
                 'tan', 'tanh']
        self.safe_dict = dict([(k, locals().get(k, None)) for k in safe_functs])
        pass

    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info['args'][1:][0].split()

            if info['command'] == 'PRIVMSG':
                if len(msgs) > 1:
                    if msgs[0] == '.calc':
                        expr = msgs[1]
                        methods['send'](info['address'], '{}'.format(
                                eval(expr, {"__builtins__":None}, safe_dict))
                        )
        except Exception as e:
            print('woops plugin', __file__, e)
