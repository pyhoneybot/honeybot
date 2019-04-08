# -*- coding: utf-8 -*-
"""
[joins.py]
Joins Plugin

[Author]
Gico Carlo Evangelista, https://gicocarlo.me/

[About]
Greets everyone who joins the channel
"""

class Plugin:

    def __init__(self):
        pass

    def run(self, incoming, methods, info):
        try:
            if info['command'] == 'JOIN':
                # Parse the user ID from info['prefix']
                raw_user = info['prefix']
                user_index = raw_user.find('!')
                user = raw_user[0:user_index]

                # Greets joined user
                channel = info['args'][0]
                greet = "Hello {} welcome to {} !".format(user, channel)
                methods['send'](info['address'], '{}'.format(greet))

        except Exception as e:
            print('woops plugin error ', e)
