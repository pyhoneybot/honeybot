# -*- coding: utf-8 -*-
"""
[googleSearch.py]
Google Search Plugin

[Author]
Justin Walker

[About]
Returns the first three links from a google search.

[Commands]
>>> .google <<search term>>
returns search links
"""

try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found")


class Plugin:
    def __init__(self):
        pass

    def __google(search_term):
        # start is what link to start with, stop is how many links to get 
        # only_standard limits it to normal links instead of ads and extra
        # links.
        return search(search_term, start=1, stop=3, \
                      only_standard=True)

    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info['args'][1:][0].split()
   
            if info['command'] == 'PRIVMSG' and msgs[0] == '.google':
                # All further messages, if there are any are added to search term.
                term = ''
                if len(msgs) > 1:
                    for msg in msgs[1:]:
                        term += msg
                    for link in Plugin.__google(term):
                        methods['send'](info['address'], link)
                else:
                    methods['send'](info['address'], "Input error. '.google search_term'.")
    
        except Exception as e:
            print('woops plugin error: ', e)