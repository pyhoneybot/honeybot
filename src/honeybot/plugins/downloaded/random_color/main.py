"""
[random_color.py]
Random Color Plugin

[Author]
Jeet Trivedi

[About]
responds to .randcol, returns a HEX color code

[Commands]
>>> .randcol
returns a HEX color code: a 6-character string representing RGB
"""

from random import randrange


class Plugin:
    def __init__(self):
        pass

    # this function returns a random 6-character HEX string, representing RGB
    def __gen_rgb_hex():
        rgb_hex_chars = [hex(randrange(16))[2:] for hex_char in range(6)]
        rgb_hex_str = "".join(rgb_hex_chars)
        rgb_hex_str = rgb_hex_str.upper()
        return rgb_hex_str

    def run(self, incoming, methods, info, bot_info):
        try:
            # if '!~' in info['prefix']:
            # print(info)
            if info["command"] == "PRIVMSG" and info["args"][1] == ".randcol":
                methods["send"](info["address"], "Hex: " + Plugin.__gen_rgb_hex())
        except Exception as e:
            print("woops plug", e)
