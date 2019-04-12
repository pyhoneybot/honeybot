# -*- coding: utf-8 -*-
"""
[quote.py]
Humour Plugin

[Author]
Angelo Giacco

[About]
Returns a riddle

[Commands]
>>> .riddle
returns a random riddle
"""
import random

class Plugin:
    def __init__(self):
        pass

    def riddle(self):
        riddles = [
            'The more you have of it, the less you see. What is it?', # darkness
            'What has a head, a tail, is brown, and has no legs?', #a penny
            'What English word has three consecutive double letters?', # Bookkeeper
            'I know a word of letters three. Add two, and fewer there will be!', #few
            'Two in a corner, 1 in a room, 0 in a house, but 1 in a shelter. What am I?', # the letter r
            'What starts with a T, ends with a T, and has T in it?', # a teapot
            'What happens when you throw a yellow rock into a purple stream?', # a splash
            'Say my name and I disappear. What am I?', #silence
            'What is it that after you take away the whole, some still remains?', #wholesome
            'A box without hinges, lock or key, yet golden treasure lies within. What is it?', #an egg
            'Forward I’m heavy, but backwards I’m not. What am I?', #ton
            'I am a box that holds keys without locks, yet they can unlock your soul. What am I?', # a piano
            'What gets wetter as it dries?', # a towel
            'I’m full of holes, yet I’m full of water. What am I?', #a sponge
            'What question can you never honestly answer yes to?', # are you asleep or dead
            'What has a neck and no head, two arms but no hands?', # a shirt
            'Feed me and I live, give me drink and I die. What am I?', # a fire
            'A man went to the hardware store to buy items for his house. 1 would cost $.25, 12 would cost $.50, 122 would cost $.75. What was he buying?', # House numbers
            'What is a thing that the more you take, the more you leave behind?', # footsteps
            'Remove six letters from this sequence to reveal a familiar English word. BSAINXLEATNTEARS' # remove six letters to get bananas
        ]

        return '{}'.format(random.choice(riddles))

    def run(self, incoming, methods, info):
        try:
            msgs = info['args'][1:]
            if info['command'] == 'PRIVMSG' and msgs[0] == '.riddle':
                methods['send'](info['address'], self.riddle(self))
        except Exception as e:
            print('Error with Riddle Plugin!', e)
