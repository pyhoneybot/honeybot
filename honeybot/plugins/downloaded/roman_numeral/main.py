# -*- coding: utf-8 -*-
"""
roman_numeral.py]
Roman Numeral Converter Plugin

[Author]
Nick Wiley

[About]
Returns the roman numeral equivalent of the number inputted

[Commands]
>>> .roman <number>
returns number represented in roman numerals
"""


class Plugin:
    def __init__(self):
        pass

    def __convert_roman_numeral(self, num):
        """Converts number into a roman numeral"""
        roman_numerals = [
            "I",
            "II",
            "III",
            "IV",
            "V",
            "VI",
            "VII",
            "VIII",
            "IX",
            "X",
            "L",
            "C",
            "D",
            "M",
        ]
        if num >= 1000:
            num -= 1000
            return roman_numerals[13] + Plugin.__convert_roman_numeral(self, num)
        elif num >= 500:
            num -= 500
            return roman_numerals[12] + Plugin.__convert_roman_numeral(self, num)
        elif num >= 400:
            num -= 400
            return (
                roman_numerals[11]
                + roman_numerals[12]
                + Plugin.__convert_roman_numeral(self, num)
            )
        elif num >= 100:
            num -= 100
            return roman_numerals[11] + Plugin.__convert_roman_numeral(self, num)
        elif num >= 90:
            num -= 90
            return (
                roman_numerals[9]
                + roman_numerals[11]
                + Plugin.__convert_roman_numeral(self, num)
            )
        elif num >= 50:
            num -= 50
            return roman_numerals[10] + Plugin.__convert_roman_numeral(self, num)
        elif num >= 40:
            num -= 40
            return (
                roman_numerals[9]
                + roman_numerals[10]
                + Plugin.__convert_roman_numeral(self, num)
            )
        elif num > 10:
            num -= 10
            return roman_numerals[9] + Plugin.__convert_roman_numeral(self, num)
        elif num > 0:
            return roman_numerals[num - 1]
        else:
            return ""

    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info["args"][1:][0].split()
            if info["command"] == "PRIVMSG":
                if len(msgs) > 1:
                    if msgs[0] == ".roman":
                        num = int(msgs[1])
                        if num < 1:
                            methods["send"](
                                info["address"], "Input a number greater than 0"
                            )
                        else:
                            methods["send"](
                                info["address"],
                                Plugin.__convert_roman_numeral(self, num),
                            )

        except Exception as e:
            print("Error with roman_numeral plugin:", e)
