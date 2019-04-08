# -*- coding: utf-8 -*-
"""
[googleSearch.py]
Google Search Plugin

[Author]
Justin Walker

[About]
Returns the first several links from a google search.

[Commands]
>>> .google <<search term>> <<link count>>
returns search links
"""

try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found")

class Plugin:
    def __init__(self):
        pass

    def __google(self, search_term, search_count):
        if search_count != None:
            num = search_term
        else:
            num = 10

        return search(search_term, num=search_count, start=0)


    def run(self, incoming, methods, info):
        try:
            msgs = info['args'][1:][0].split()
   
            if info['command'] == 'PRIVMSG' and msgs[0] == '.google':
                count = None
                if len(msgs) == 2:
                    term = msgs[1]
                    if len(msgs) == 3:
                        count = msgs[2]
                    methods['send'](info['address'], self.__google(term,count))
                else:
                    methods['send'](info['address'], "Input error. '.google search_term search_count'.")
    
        except Exception as e:
            print('woops plugin error: ', e)



def send(info, message):
    print(message)


def test_them(plugin, msg):

    methods = {"send":send}
    msg = msg
    info = {'args':[None,msg],
            'command':'PRIVMSG',
            'address':'That place'}
    plug.run("",methods,info)


plug = Plugin()

test_them(plug, ".google cool")