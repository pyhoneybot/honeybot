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
        pass

    @staticmethod
    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info["args"][1:][0].split()

            if info["command"] == "PRIVMSG" and len(msgs) > 1 and msgs[0] == ".calc":
                safe_dict = {
                    "acos": acos,
                    "asin": asin,
                    "atan": atan,
                    "atan2": atan2,
                    "ceil": ceil,
                    "cos": cos,
                    "cosh": cosh,
                    "degrees": degrees,
                    "e": e,
                    "exp": exp,
                    "fabs": fabs,
                    "floor": floor,
                    "fmod": fmod,
                    "frexp": frexp,
                    "hypot": hypot,
                    "ldexp": ldexp,
                    "log": log,
                    "log10": log10,
                    "modf": modf,
                    "pi": pi,
                    "pow": pow,
                    "radians": radians,
                    "sin": sin,
                    "sinh": sinh,
                    "sqrt": sqrt,
                    "tan": tan,
                    "tanh": tanh,
                }
                expr = msgs[1]
                methods["send"](
                    info["address"],
                    "{}".format(eval(expr, {"__builtins__": None}, safe_dict)),  # nosec eval_used
                )
        except Exception as ex:
            print("woops plugin", __file__, ex)
