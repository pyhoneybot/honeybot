# -*- coding: utf-8 -*-
"""
[proverb.py]
Proverb Plugin

[Author]
Sushant Kumar

[About]
sends a random proverb on request

[Commands]
>>> .proverb
returns a random proverb
"""
import random


class Plugin:
    def __init__(self):
        pass

    def proverb(self):
        proverbs = ['Absence makes the heart grow fonder.',
'Actions speak louder than words.',
'Don’t put off until tomorrow what you can do today.',
'Don’t put too many irons in the fire.',
'Good things come to those who wait.',
'Half bread is better than nothing.',
'Where there is smoke there is fire',
'An early bird catches worm',
'People who live in glass houses should not throw stones at others',
'Strike while the iron is hot',
'Rome was not built in a day',
'The darkest cloud has the silver lining',
'As you sow, so you reap',
'All that glitters is not good',
'People who live in glass houses should not throw stones at others',
'A cat has nine lives',
'Charity begins at home',
'The dog that bites does not bark',
'A snake may shed its skin, but it\'s still a snake',
'Until the rotten tooth is pulled out, the mouth must chew with caution',
'Todays flat tits were yesterdays pointed ones'
]

        return '{}'.format(random.choice(proverbs))

    def run(self, incoming, methods, info, bot_info):
        try:
            # if '!~' in info['prefix']:
                # print(info)
            msgs = info['args'][1:]
            if info['command'] == 'PRIVMSG' and msgs[0] == '.proverb':
                methods['send'](info['address'], Plugin.proverb(self))
        except Exception as e:
            print('woops plug', e)
