"""
[dictionary.py]
Dictionary Plugin

[Author]
Milad H,

[About]
Searches the python documentatioin(pydocs) for the related keyword(s)
and returns some of the relevant links


[Commands]
>>> .pydocs <keyword>
returns links in python documentation related to the keyword
"""
from PyDictionary import PyDictionary


class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info["args"][1:][0].split()

            if info["command"] == "PRIVMSG" and msgs[0] == ".dictionary":
                dict = PyDictionary()
                word = str(msgs[1])
                defin = dict.meaning(word)["Noun"]
                for definition in defin:
                    methods["send"](info["address"], definition)
        except Exception as e:
            print("woops plug", e)
