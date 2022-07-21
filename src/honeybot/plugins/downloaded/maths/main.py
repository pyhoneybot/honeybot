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

    def run(self, incoming, methods, info, bot_info):
        try:
            # if '!~' in info['prefix']:
            # print(info)
            msgs = info["args"][1:][0].split()
            if info["command"] == "PRIVMSG":
                if len(msgs) > 1:
                    if msgs[0] == ".sin":
                        try:
                            sine = math.sin(float(msgs[1]))
                            methods["send"](info["address"], "{}".format(sine))
                        except ValueError:
                            methods["send"](info["address"], ".sin must have numbers")
                    elif msgs[0] == ".cos":
                        try:
                            cosine = math.cos(float(msgs[1]))
                            methods["send"](info["address"], "{}".format(cosine))
                        except ValueError:
                            methods["send"](info["address"], ".cos must have numbers")
                    elif msgs[0] == ".tan":
                        try:
                            tangent = math.tan(float(msgs[1]))
                            methods["send"](info["address"], "{}".format(tangent))
                        except ValueError:
                            methods["send"](info["address"], ".tan must have numbers")
                    elif msgs[0] == ".rand":
                        try:
                            if int(msgs[1]) >= int(msgs[2]):
                                methods["send"](
                                    info["address"],
                                    ".rand requires two integers that are not "
                                    "equal and the first must be biggest",
                                )
                            else:
                                rand = random.randint(int(msgs[1]), int(msgs[2]))
                                methods["send"](info["address"], "{}".format(rand))
                        except ValueError:
                            methods["send"](info["address"], ".rand must have numbers")
        except Exception as e:
            print("\n*error*\nwoops plugin", __file__, e, "\n")
