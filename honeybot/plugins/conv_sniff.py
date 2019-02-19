# -*- coding: utf-8 -*-
"""
[conv_sniff.py]
Conversation Sniffer Plugin

[Author]
Abdur-Rahmaan Janhangeer, pythonmembers.club

[About]
senses conversation topic with sensitivity set by user, also supports 
word-specific sensing
"""
import random

class Plugin:
    """
    checkin 
    L checks in list
    S checks in string
    """
    def __init__(self):
        self.topics = {
                'bot':{
                       'elems':['bot', 'robot', 'artificial intelligence', 'ai'],
                       'occurs':1,
                       'replies':['you are thinking about me and my cousins', 
                       'bots are we?'],
                       'checkin':'L'
                        },
                'nature':{
                       'elems':['earth', 'flower', 'lake', 'sea', 'world', 
                                'forest', 'grass'],
                       'occurs':2,
                       'replies':['we must remind ourselves to protect our lovely '+
                                'planet', 
                                'plant a tree when you can'],
                       'checkin':'L'
                        },
                'alhmd':{
                       'elems':['a','l','ha','m','d'],
                       'occurs':5,
                       'replies':[' yes indeed, praise be to allah (الحَمْد لله) . . .'],
                       'checkin':'S'
                        }
                }


    def run(self, incoming, methods, info):
        try:
            msgs = info['args'][1:][0].split()
            
            if info['command'] == 'PRIVMSG':
                if len(msgs) > 1:
                    msgs = set(msgs)
                    
                    for topic in self.topics:
                        if self.topics[topic]['checkin'] == 'L':
                            meet = set(self.topics[topic]['elems']).intersection(msgs)
                            
                            if len(meet) == self.topics[topic]['occurs']:
                                methods['send'](info['address'], 
                                       random.choice(self.topics[topic]['replies'])
                                       )
                        elif self.topics[topic]['checkin'] == 'S':
                                for word in msgs:
                                    meet = set(self.topics[topic]['elems']).intersection(set(word))
                                    occurs = self.topics[topic]['occurs']
                                    if meet and len(meet) > occurs-2:
                                        methods['send'](info['address'], 
                                               random.choice(self.topics[topic]['replies'])
                                               )
                                        break
                                
                        
        except Exception as e:
            print('\n*error*\nwoops plugin', __file__, e, '\n')
