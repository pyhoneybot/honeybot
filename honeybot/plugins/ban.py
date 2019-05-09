# -*- coding: utf-8 -*-
"""
[ban.py]
Ban Plugin
[Author]
Angelo Giacco
[About]
bans a user from the channel for a specified or default length of time
[Commands]
>>>.ban user time
bans the user from the channel for a length of time
"""

class Plugin:
    def __init__(self):
        pass

    def ban(self, methods, info, user, time = 60): #default ban is a minute
        ban_command = "BAN -ku"+str(time)+" "+ user + " \r\n"
        methods["send_raw"](ban_command)

    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info['args'][1:][0].split()
            if len(msgs) > 0:
                if info['command'] == 'PRIVMSG' and msgs[0] == '.ban':
                    if len(msgs) == 1:
                        methods["send"](info["address"],"You must state the username that you want to ban")
                    elif len(msgs) == 2:
                        user = info["prefix"].split("!")[0]
                        if msgs[1] != user:
                            ban(methods,info,msgs[1])
                        else:
                            methods["send"](info["address"],"You can not ban yourself!")
                    elif len(msgs) == 3:
                        try:
                            if msgs[2] > 600:
                                raise ValueError
                            ban(methods,info,msgs[1],int(msgs[2]))
                        except ValueError:
                            methods["send"](info["address"],"Invalid period of time, must be a number less than 600")
                    else:
                        methods["send"](info["address"],"Kick function requires .kick followed by one or two arguments which are the name of the user you want to ban and you may specify a duration of the ban in seconds!")

        except Exception as e:
            print('woops ban plugin error', e)
