# -*- coding: utf-8 -*-
"""
[kick.py]
Kick Plugin
[Author]
Angelo Giacco
[About]
kicks a user
[Commands]
>>>.kick user
kicks the user off the channel
"""

class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info['args'][1:][0].split()
            if len(msgs) > 0:
                if info['command'] == 'PRIVMSG' and msgs[0] == '.kick':
                    if len(msgs) == 1:
                        methods["send"](info["address"],"You must state the username that you want to kick")
                    elif len(msgs) == 2:
                        user = info["prefix"].split("!")[0]
                        if msgs[1] != user:
                            name = msgs[1]
                            channel = info["address"]
                            kick_command = "KICK "+ channel + " " + name + " \r\n"
                            methods["send_raw"](kick_command)
                        else:
                            methods["send"](info["address"],"You can not kick yourself!")
                    else:
                        methods["send"](info["address"],"Kick function requires .kick followed by one argument which is the name of the user you want to kick!")

        except Exception as e:
            print('woops kick plugin error', e)
