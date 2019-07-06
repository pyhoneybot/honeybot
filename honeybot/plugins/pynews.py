# -*- coding: utf-8 -*-
"""
[pynews.py]
Python news checking plugin

[Author]
Sam Deans

[Github]
@sdeans0

[About]
Finds the top five news items on python.org and prints them to the IRC

[Commands]
>>> .pynews
returns the top 5 python.org news articles
"""


import requests,requests_html

class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info, bot_info):
        try:
            #msgs = info['args'][1:][0].split()

            if info['command'] == 'PRIVMSG' and info['args'][1] == '.pynews':
                session = HTMLSession()
                py_site = session.get('https://www.python.org')
                # Get a list of <li> elements under the blog heading.
                blog_links = py.html.find('div.shrubbery')[0].find('ul.menu')[0].find('li')
                # Iterate through the list to preserve the order of the blog links
                links = []
                for element_li in blog_links:
                    links.append(': '.join([element_li.text,element_li.links.pop()]))
                message = '\n'.join(links)
                methods['send'](info['address'], message)

        except Exception as e:
            print('woops plugin', __file__, e)
