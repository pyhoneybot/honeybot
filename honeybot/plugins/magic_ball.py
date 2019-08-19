# -*- coding: utf-8 -*-
"""
[magic_ball.py]
Magic 8 ball Plugin

[Author]
Zakaria Talhami

[About]
Fortune-telling for question using a magic 8 ball

[Commands]
>>> .8ball <<question>>
returns It is certain

>>> .magic8ball <<question>>
returns Very doubtful
"""

import random


class Plugin:
    def __init__(self):
        pass

    def answer():
        possible_answers = [
            "It is certain",
            "It is decidedly so",
            "Without a doubt",
            "Yes - definitely",
            "You may rely on it",
            "As I see it, yes",
            "Most likely",
            "Outlook good",
            "Yes",
            "Signs point to yes",
            "Reply hazy, try again",
            "Ask again later",
            "Better not tell you now",
            "Cannot predict now",
            "Concentrate and ask again",
            "Don't count on it",
            "My reply is no",
            "My sources say no",
            "Outlook not so good",
            "Very doubtful",
        ]
        return random.choice(possible_answers)

    def run(self, incoming, methods, info, bot_info):
        try:
            print('In the 8 ball area')
            msgs = info['args'][1:][0].split()
            if info['command'] == 'PRIVMSG' and (msgs[0] == '.8ball' or msgs[0] == '.magic8ball'):
                question = " ".join(msgs[1:])
                if '?' in question:
                    methods['send'](info['address'], Plugin.answer())
                else:
                    methods['send'](info['address'], 'You must ask a question')
        except Exception as e:
            print('woops plug', e)
