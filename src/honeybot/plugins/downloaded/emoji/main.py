class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info["args"][1:][0].split()
            print(len(msgs))
            if info["command"] == "PRIVMSG" and msgs[0] == ".emoji":
                meaning = emoji.demojize(str(msgs[1]))
                methods["send"](info["address"], meaning)
        except Exception as e:
            print("woops plugin error ", e)
