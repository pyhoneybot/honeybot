"""
[abbreviation.py]
Abbreviation Plugin

[Author]
Erin Moon, Sourav Dutta

[About]
responds to .def lol

[Commands]
>>> .def lol
returns lots of love
"""


class Plugin:
    abbreviations = {
        "idk": "I don’t know",
        "idc": "I don’t care",
        "idm": "I don’t mind",
        "idr": "I don’t remember",
        "idrm": "I don’t really mind",
        "rly": "really",
        "rlly": "really",
        "sme": "same",
        "sm": "same",
        "lol": "laughing out loud / lots of love",
        "lmao": "laughing my ass off",
        "wtf": "what the fuck",
        "wth": "what the heck",
        "lmfao": "laughing my fucking ass off",
        "kys": "kill your-self",
        "kms": "kill my-self",
        "pls": "please",
        "plz": "please",
        "ye": "yes / yeah",
        "yea": "yes / yeah",
        "so": "significant other / shoutout",
        "bf": "boyfriend",
        "gf": "girlfriend",
        "smh": "shaking my head",
        "cos": "because",
        "cuz": "because",
        "cus": "because",
        "cause": "because",
        "omg": "oh my god",
        "oml": "oh my lord",
        "pic": "picture",
        "wyd": "what you doing",
        "wud": "what you doing",
        "wywd": "what you wanna do",
        "wuwd": "what you wanna do",
        "u": "you",
        "tb": "text back",
        "nr": "no reply(s)",
        "nrs": "no reply(s)",
        "bro": "brother",
        "nm": "nothing much",
        "nvm": "never mind",
        "dm": "direct message / doesn’t matter",
        "tbh": "to be honest",
        "m8": "mate",
        "prob": "pobably",
        "probs": "probably",
        "ly": "love you",
        "lysm": "love you so much",
        "lysfm": "love you so fucking much",
        "lyl": "love you loads",
        "ly2": "love you too",
        "gn": "good-night",
        "gm": "good-morning",
        "jk": "just kidding",
        "jw": "just wondering",
        "ppl": "people",
    }

    def __init__(self):
        pass

    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info["args"][1].split()
            if info["command"] == "PRIVMSG" and msgs[0] == ".def":
                abbreviation = msgs[1].lower()
                if abbreviation in Plugin.abbreviations.keys():
                    methods["send"](info["address"], Plugin.abbreviations[abbreviation])
                else:
                    methods["send"](info["address"], "Result not found!")
        except Exception as e:
            print("woops, abbreviation plugin error", e)
