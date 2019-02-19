# -*- coding: utf-8 -*-
"""
[joke.py]
Joke Plugin

[Author]
Abdur-Rahmaan Janhangeer, pythonmembers.club

[About]
sends a random joke on request

[Commands]
>>> .joke
returns a random joke
"""
import random


class Plugin:
    def __init__(self):
        pass

    def joke(self):
        jokes = [
'Why did the physics teacher break up with the biology teacher? There was no \
chemistry.',
'I asked my daughter if she’d seen my newspaper. She told me that newspapers \
are old school.She said that people use tablets nowadays and handed me her \
iPad. The fly didn’t stand a chance',
'A recent scientific study showed that out of 2,293,618,367 people, 94% are \
too lazy to actually read that number.',
'Why is it a bad idea to insult an octopus? because it is well armed'
]

        return '{}'.format(random.choice(jokes))

    def run(self, incoming, methods, info):
        try:
            # if '!~' in info['prefix']:
                # print(info)
            msgs = info['args'][1:]
            if info['command'] == 'PRIVMSG' and msgs[0] == '.joke':
                methods['send'](info['address'], self.joke())
        except Exception as e:
            print('woops plug', e)
