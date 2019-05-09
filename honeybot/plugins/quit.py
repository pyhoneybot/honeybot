# -*- coding: utf-8 -*-
"""
[quit.py]
Quit Plugin
[Author]
Angelo Giacco
[About]
quits user and leaves a message
[Commands]
>>>.quit message
quits the user from the channel and leaves a message
"""
class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info['args'][1:][0].split()
            if len(msgs) > 0:
                if info['command'] == 'PRIVMSG' and msgs[0] == '.quit':
                    if len(msgs) == 1:
                        methods["send_raw"]("QUIT \r\n")
                    elif len(msgs) > 1:
                        message = " ".join(msgs[1:])
                        methods["send_raw"]("QUIT "+message+" \r\n")
                    else:
                        methods["send"](info["address"],"Quit function requires .quit followed and can be followed by a message")

        except Exception as e:
            print('woops quit plugin error', e)
