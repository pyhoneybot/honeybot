# -*- coding: utf-8 -*-
"""
[maths.py]
Miscellaneous Maths Operations Plugin

[Author]
Abdur-Rahmaan Janhangeer, pythonmembers.club

[About]
some maths related commands

[Commands]
>>> .sin <number>
returns sine of number

>>> .cos <number>
returns cosine of number

>>> .tan <number>
returns tangent of number

>>> .rand <number1> <number2>
returns number between number1 and number2
"""
import math
import random


class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info):
        try:
            # if '!~' in info['prefix']:
                # print(info)
            msgs = info['args'][1:][0].split()
            # print(msgs)
            if info['command'] == 'PRIVMSG':
                if len(msgs) > 1:
                    if msgs[0] == '.sin':
                        sine = math.sin(int(msgs[1]))
                        methods['send'](info['address'], '{}'.format(sine))
                    elif msgs[0] == '.cos':
                        cosine = math.cos(int(msgs[1]))
                        methods['send'](info['address'], '{}'.format(cosine))
                    elif msgs[0] == '.tan':
                        tangent = math.tan(int(msgs[1]))
                        methods['send'](info['address'], '{}'.format(tangent))
                    elif msgs[0] == '.rand':
                        rand = random.randint(int(msgs[1]), int(msgs[2]))
                        methods['send'](info['address'], '{}'.format(rand))
        except Exception as e:
            print('\n*error*\nwoops plugin', __file__, e, '\n')
