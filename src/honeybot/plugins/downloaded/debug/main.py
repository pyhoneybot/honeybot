"""
[debug.py]
Debug plugin : Un

[Author]
Abdur-Rahmaan Janhangeer, pythonmembers.club

[About]
prints all parameters passed to bot

[Commands]
>>> .debug
prints some parameters
"""


class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info, bot_info):
        try:
            # if '!~' in info['prefix']:
            # print(info)
            if info["command"] == "PRIVMSG" and info["args"][1] == ".debug":
                methods["send"](info["address"], info["prefix"])
        except Exception as e:
            print("woops plug", e)
