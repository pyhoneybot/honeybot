class Plugin:
    def __init__(self):
        pass

    def __meaning(emoji):
        d = {
            "😀": "Grinning Face",
            "😃": "Grinning Face with Big Eyes",
            "😄": "Grinning Face with Smiling Eyes",
            "😁": "Beaming Face with Smiling Eyes",
            "😆": "Grinning Face with Sweat",
            "🤣": "Rolling on the Floor Laughing",
            "😂": "Face with Tears of Joy",
            "🙂": "Slightly Smiling Face",
            "🙃": "Upside-Down Face",
            "😉": "Winking Face",
            "😊": "Smiling Face with Smiling Eyes",
            "😇": "Smiling Face with Halo",
            "🥰": "Smiling Face with Hearts",
            "😍": "Smiling Face with Heart-Eyes",
            "🤩": "Star-Struck",
            "😘": "Face Blowing a Kiss",
            "😗": "Kissing Face",
            "😉": "Winking Face",
            "😊": "Smiling Face with Smiling Eyes",
            "😇": "Smiling Face with Halo",
            "🥰": "Smiling Face with Hearts",
            "😍": "Smiling Face with Heart-Eyes",
            "🤩": "Star-Struck",
            "😘": "Face Blowing a Kiss",
            "😗": "Kissing Face",
            "😚": "Kissing Face with Closed Eyes",
            "😙": "Kissing Face with Smiling Eyes",
            "😋": "Face Savoring Food",
            "😛": "Face with Tongue",
            "😜": "Winking Face with Tongue",
            "🤪": "Zany Face",
            "😝": "Squinting Face with Tongue",
            "🤑": "Money-Mouth Face",
            "🤗": "Smiling Face with Open Hands",
            "🤭": "Face with Hand Over Mouth",
        }
        if emoji in d.keys():
            return d[emoji]
        else:
            return "not supported"

    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info["args"][1:][0].split()
            print(len(msgs))
            if info["command"] == "PRIVMSG" and msgs[0] == ".emoji":
                emoji = str(msgs[1])
                methods["send"](info["address"], Plugin.__meaning(emoji))
        except Exception as e:
            print("woops plugin error ", e)
