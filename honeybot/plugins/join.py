# -*- coding: utf-8 -*-
"""
[join.py]
Join Plugin

[Author]
Marcelo Benesciutti

[About]
Will join a given channel in the server

[Commands]
>>> .join channel
joins the given channel
"""

class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info):
        try:
            msgs = info['args'][1:][0].split()
            raw_user = info['prefix']
            user_index = raw_user.find('!')
            user = raw_user[0:user_index]
            f = open("settings/OWNERS.conf", "r")
            for owner in f:
                if owner.strip() == user:
                    if info['command'] == 'PRIVMSG' and msgs[0] == '.join':
                        methods['join'](msgs[1])

        except Exception as e:
            print('woops plugin error: ', e)