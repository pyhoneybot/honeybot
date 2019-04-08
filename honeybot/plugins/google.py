# -*- coding: utf-8 -*-
"""
[googleSearch.py]
Google Search Plugin

[Author]
Justin Walker

[About]
Returns the first several links from a google search.

[Commands]
>>> .google <<search term>> <<optional link count, default 3>>
returns search links
"""

try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found")


class Plugin:
    def __init__(self):
        pass

    def __google(search_term, search_count):
        # num is number of links, start is what link to start with,
        # only_standard limits it to normal links instead of adds and extra
        # links.
        return search(search_term, start=1, stop=search_count, \
                      only_standard=True)

    def run(self, incoming, methods, info):
        try:
            msgs = info['args'][1:][0].split()
   
            if info['command'] == 'PRIVMSG' and msgs[0] == '.google':
                # First argurment after .google should be search term,
                # if it exists
                count = 3
                term = ''
                if len(msgs) > 1:
                    for msg in msgs[1:]:
                        if msg[0] == "'":
                            #Find a way to separate int count from whole string mesage.
                        for link in Plugin.__google(term, count):
                            methods['send'](info['address'], link)
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

test_them(plug, ".google something")