# -*- coding: utf-8 -*-
"""
[nick.py]
nick Plugin
[Author]
Angelo Giacco
[About]
nicks a user
[Commands]
>>>.nick user
changes user's nickname
"""

class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info['args'][1:][0].split()
            if len(msgs) > 0:
                if info['command'] == 'PRIVMSG' and msgs[0] == '.nick':
                    if len(msgs) == 1:
                        methods["send"](info["address"],"You must state what you want to change your nickname to")
                    elif len(msgs) == 2:
                        methods["send_raw"]("NICK "+msgs[1]+" \r\n")
                    else:
                        methods["send"](info["address"],"NICK function requires .nick followed by your new nickname")
        except Exception as e:
            print('woops nick plugin error', e)
