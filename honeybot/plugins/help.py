# -*- coding: utf-8 -*-
"""
[help.py]
Help Plugin

[Author]
Eduardo Moraes de Mello, https://github.com/edumello

[About]
Show link with all the functionalities of the bot.

[Commands]
>>> .help 
returns link of plugins informations
"""


class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info, bot_info):

        try:
            if info['command'] == 'PRIVMSG' and info['args'][1] == '.help':
                message = "Page with all functionalities and commands: https://github.com/Abdur-rahmaanJ/honeybot/blob/master/honeybot/plugins_info.md"
                methods['send'](info['address'], message)
        except Exception as e:
            print('woops plug', e)
