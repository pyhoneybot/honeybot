# -*- coding: utf-8 -*-
"""
[send_message.py]
Send Message Plugin

[Author]
Justin Walker

[About]
Sends a message to another channel.

[Commands]
>>> .send #channel .u riceabove .m how are you?
Sends a message to #channel like
'IronPenguin from #channel says to riceabove: how are you?'

>>> .send #channel hi all
Sends a message to #channel like
'IronPenguin from #channel says: hi all'

Checks if user online first and says "User not online."
"""


class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info["args"][1:][0].split()
            if info["command"] == "PRIVMSG" and msgs[0] == ".send":
                message = ""
                # Take raw suffix and pull out sender name from before !
                bang = info["prefix"].find("!")
                channel_destination = msgs[1]
                sender = info["prefix"][0:bang]
                sender_channel = info["address"]

                # Checks for general message type
                if len(msgs) >= 3 and msgs[2][0] != ".":
                    message = Plugin.send_general_message(msgs, sender, sender_channel)
                    methods["send"](channel_destination, message)
                # Checks for specific message type
                elif len(msgs) >= 6 and msgs[2] == ".u" and msgs[4] == ".m":
                    recipient = msgs[3]

                    # Sends whois to server to determine online status
                    methods["send_raw"]("whois {0} \r\n".format(recipient))

                    # Recieves message back from server and converts to be
                    # usable.
                    data = self.irc.recv(2048)
                    raw_msg = data.decode("UTF-8")
                    msg = raw_msg.strip("\n\r")

                    if msg.endswith("No such nick/channel"):
                        methods["send"](info["address"], sender + " isn't online.")
                    else:
                        message = Plugin.send_specific_message(
                            msgs, recipient, sender, sender_channel
                        )
                    methods["send"](channel_destination, message)
                else:
                    methods["send"](
                        info["address"],
                        "Command input error. Needs to be '.send "
                        + "#channel message' or '.send #channel .u "
                        + "username .m message'.",
                    )
        except Exception as e:
            print("woops plugin error: ", e)

    def send_general_message(msgs, sender, sender_channel):
        message = ""
        for word in msgs[2:]:
            message += word + " "
        complete_message = "{0} from {1} says: {2}".format(
            sender, sender_channel, message.rstrip()
        )
        return complete_message

    def send_specific_message(msgs, recipient, sender, sender_channel):
        message = ""
        for word in msgs[5:]:
            message += word + " "
        complete_message = "{0} from {1} says to {2}: {3}".format(
            sender, sender_channel, recipient, message.rstrip()
        )
        return complete_message
