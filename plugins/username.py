# -*- coding: utf-8 -*-
"""
[username.py]
Username Generator Plugin

[Author]
Abdur-Rahmaan Janhangeer, pythonmembers.club

[About]
generates random usernames, used for inspiration

[Commands]
>>> .uname
returns generated username
"""
import random


class Plugin:
    def __init__(self):
        pass
    
    def gen_uname(self):
        """Return a string containing a randomly-generated username based on an adjectives list 
        (p1) and a noun list (p2)"""
        p1 = ['hopeful', 'young', 'sloppy', 'magic', 'intelligent', 'uncommon', 'cute', 'dangerous'
        'innocent', 'spooky', 'crazy', 'young', 'desperate', 'epic', 'anonymous']
        p2 = ['star', 'tree', 'ant', 'spider', 'moon', 'bug', 'name', 'heisenberg', 'dragon'
         'snake', 'lion', 'rebel', 'patriot', 'flower', 'popsicle', 'sun', 'failure']
        return '{}{}'.format(random.choice(p1), random.choice(p2))

    def run(self, incoming, methods, info, bot_info):
        try:
            # if '!~' in info['prefix']:
                # print(info)
            msgs = info['args'][1:]
            if info['command'] == 'PRIVMSG' and msgs[0] == '.uname':
                methods['send'](info['address'], Plugin.gen_uname(self))
        except Exception as e:
            print('woops plug', e)
