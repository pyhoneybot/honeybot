"""

[book_of_day.py]
Book of the Day Plugin
[Author]
Schoberg, UMD
[About]
using bookoftheday.org, get the title and link of the book of the day
[Commands]
>>> .bookoftheday
https://bookoftheday.org/fleishman-is-in-trouble-taffy-brodesser-akner/
"""

import requests
from bs4 import BeautifulSoup

class Plugin:
    def __init__(self):
        pass

    def book(self):
        headers = {'Accept' : 'application/json'}
        r = requests.get('http://bookoftheday.org', headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        d = soup.find_all("div", {"class":"chpcs_foo_content"})

        return str(d[0].a['href'])

    def run(self, incoming, methods, info, bot_info):
        try:
            if info['command'] == 'PRIVMSG' and info['args'][1] == '.bookofday':
                methods['send'](info['address'], Plugin.book(self))
        except Exception as e:
            print('woops book_of_day plugin error', e)