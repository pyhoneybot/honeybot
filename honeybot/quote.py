# -*- coding: utf-8 -*-
"""
[Quote.py]
Quote Plugin

[Author]
Divyanshu Mehta

[About]
Extracts quotes and send random quote from Trailer Park Boys

[Commands]
>>>.Quote <count>
"""
from bs4 import BeautifulSoup
import urllib
import random
import sys

class Plugin:

    def __init__(self):
        pass
    
    def run():
        #try:
        data = urllib.urlopen("https://en.wikiquote.org/wiki/Trailer_Park_Boys").read()
        bs = BeautifulSoup(data,"lxml")

        quotes=[]

        for i in bs.find_all('dl'):
            quotes.append(i.text)
        for i in range(int(sys.argv[1])):
            print random.choice(quotes)
            print ("--------------------------------------------------------------------------")
   
        except:
           print "Check your internet Connection"
