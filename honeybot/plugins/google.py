# -*- coding: utf-8 -*-
"""
[googleSearch.py]
Google Search Plugin

[Author]
Justin Walker

[About]
Returns the first several links from a google search.

[Commands]
>>> .google <<search term>> <<optional link count, default 10>>
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
        # num is number of links, start is what link to start with,
        # only_standard limits it to normal links instead of adds and extra
        # links.
        return search(search_term, num=search_count, start=0,
                      only_standard=True)

    def run(self, incoming, methods, info):
        try:
            msgs = info['args'][1:][0].split()
   
            if info['command'] == 'PRIVMSG' and msgs[0] == '.google':
                count = 10
                # First argurment after .google should be search term,
                # if it exists
                if len(msgs) == 2:
                    term = msgs[1]
                    # Second argument should be count if it exists.
                    if len(msgs) == 3:
                        count = msgs[2]

                    for link in self.__google(term, count):
                        methods['send'](info['address'], link)
                else:
                    methods['send'](info['address'], "Input error. '.google search_term search_count'.")
    
        except Exception as e:
            print('woops plugin error: ', e)