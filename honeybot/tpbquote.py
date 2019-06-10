# -*- coding: utf-8 -*-
"""
[Quote.py]
Quote Plugin

[Author]
Divyanshu Mehta

[About]
Extracts quotes and send random quote from Trailer Park Boys

[Commands]
>>>.quote <count>
"""
import requests
import random
from bs4 import BeautifulSoup

class Plugin:

    def __init__(self):
        pass
    
    def quote(self):
        data = requests.get("https://en.wikiquote.org/wiki/Trailer_Park_Boys").text
        bs = BeautifulSoup(data,"lxml")
        quotes=[]
        for quote in bs.find_all('dl'):
            quotes.append(quote.text)
        return random.choice(quotes)
    
    def run(self,incoming,methods,info,bot_info):
        try:
            msg = info['args'][1:]
            if info['command'] == 'PRIVMSG' and msg[0]=='.quote':
                for i in range(int(msg[1])):
                    methods['send'](info['address'], Plugin.quote(self))
        except Exception as e:
            print ('Error:',e)
