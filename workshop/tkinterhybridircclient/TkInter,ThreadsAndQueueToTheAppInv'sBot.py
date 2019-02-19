#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'me' #Abdur-Rahmaan Janhangeer'
#__coauthor__ = 'David Salinas Cortés'
#__suporters__ = "Yash Paupia and Pirabarlen Cheenaramen"
#My first messing-up with python. Code in progress. Here only for checking. use at your own risk (those indents)!
#Honeybot's disparities in code style is because of a trying out of Python
#see the features in the honeybotfeatures.txt 

import socket
import tkinter
from tkinter import *
import time
import os
import sys

import urllib.request
import json

import threading
import random
import multiprocessing
from multiprocessing import Queue
import queue

import math
from datetime import datetime

localtime = time.asctime( time.localtime(time.time()) )
WUNDERGROUND_KEY=''
PRIV = 'PRIVMSG '
KICK = 'KICK '
WHOIS = 'WHOIS '
JOIN = 'JOIN '

SYMBOLS = ['!', '"', '·', '$', '%', '&', '/', 
			'(', ')', '=', '?', '¿', 'º', 'ª', 
			'\\', '|', '@', '#', '~', '½', '¬', 
			'{', '[', ']', '}', '^', '*', '"', 
			'Ç', '`', '+', '\'', 'ç', ',', '.', 
			'-', ';', ':', '_', '·', '<', '>', 
			' ']


FreenodeParams = {'IRC_NETWORK' : "freenode", 
	'BOT_IRC_SERVER' : "chat.freenode.net", 
	'BOT_IRC_CHANNEL' : "##bottestingmu", 
	'BOT_IRC_CHANNEL2' : "#python", 
	'CHANNELN' : "##bottestingmu", 
	'CHANNELPY' : "##bottestingmu", 
	'TRANSLATOR_BOT_CHANNEL': "##bottestingmu",
	'BOT_IRC_PORT' : 6667, 
	'BOT_NICKNAME' : "MoxygeRen", 
	'BOT_OWNER1': "Mo4_xi1_ge1_Ren2", 
	'BOT_OWNER2': "appinventormu", 
	'BOT_OWNER3': "appinv", 
	'BOT_OWNERS': ["Mo4_xi1_ge1_Ren2","appinventormu","appinv"], 
	'BOT_PASSWORD' : "W4AbSQQM", 
	'NICK_SERV_ACCT': "NickServ",
	'TRANSLATOR_BOT': "mxgrPhnny"}

UndernetParams = {'IRC_NETWORK' : "undernet", 
	'BOT_IRC_SERVER' : "Mesa.az.us.UNDERNET.org", 
	'BOT_IRC_CHANNEL' : "#bottestingmu", 
	'BOT_IRC_CHANNEL2' : "#python", 
	'CHANNELN' : "##bottestingmu", 
	'CHANNELPY' : "##bottestingmu", 
	'BOT_IRC_PORT' : 6667, 
	'BOT_NICKNAME' : "mxgr", 
	'BOT_OWNER1': "MoxygeRen", 
	'BOT_OWNER2': "appinventormu", 
	'BOT_OWNER3': "appinv", 
	'BOT_OWNERS': ["MoxygeRen","appinventormu","appinv"], 
	'BOT_PASSWORD' : "W4AbSQQM", 
	'NICK_SERV_ACCT': "X@channels.undernet.org"}

IRCNetParams = {'IRC_NETWORK' : "ircnet", 
	'BOT_IRC_SERVER' : "irc.atw-inter.net", 
	'BOT_IRC_CHANNEL' : "#mexico", 
	'BOT_IRC_CHANNEL2' : "#python", 
	'CHANNELN' : "##bottestingmu", 
	'CHANNELPY' : "##bottestingmu", 
	'BOT_IRC_PORT' : 6667, 
	'BOT_NICKNAME' : "mxgr", 
	'BOT_OWNER1': "MoxygeRen", 
	'BOT_OWNER2': "appinventormu", 
	'BOT_OWNER3': "appinv", 
	'BOT_OWNERS': ["MoxygeRen","appinventormu","appinv"], 
	'BOT_PASSWORD' : "", 
	'NICK_SERV_ACCT': "NickServ"}


gbPARAMS = [FreenodeParams, UndernetParams, IRCNetParams]

TEXT_HERE = "<TEXTHERE>"


#................................................................
            

chjcmd = ['joinpy']
chj2cmd = ['botjoin']
jpycmd = 'mmm'

brandf = ['.rand']

fnWindow = None
unWindow = None
inWindow = None

WhoseBeingTranslated = None

def hnnybtprnt(psTexto, psUtf8=""):
	print(datetime.now().strftime('%d-%m-%Y %H:%M:%S') + ".- " + psTexto, psUtf8)	


def randomSleep(piMaxSecondsToWait):
	lfFraction = random.random()
	liMaxSeconds = random.randint(2, piMaxSecondsToWait)
	hnnybtprnt("Sleeping " + str(liMaxSeconds*lfFraction) + " seconds")
	time.sleep(liMaxSeconds*lfFraction)
	

def ircSendWithRandomSleep(pData):
	randomSleep(4)
	self.irc.send(pData)


#................................................................

SPANISH_ATTENTION = ['Hola',
					'Ola',
					'Eit',
					'Eh',
					'Ehm',
					'Escucha',
					'Mira',
					'huh',
					'quihúbole',
					'quihubole',
					'qué hay',
					'que hay',
					'qué habido',
					'que habido',
					'qué ha habido',
					'que ha habido']

PORTUGUESE_ATTENTION = ['oi',
					'Ei',
					'Olá',
					'Ola',
					'E aí',
					'Dia bom',
					'Bom dia',
					'Dia bom']

ENGLISH_ATTENTION = [ "Hello", 
					 "Hi", 
					 "Hi there", 
					 "Hey there", 
					 "Hmmm", 
					 "Ehm", 
					 "Listen", 
					 "Hey", 
					 "hey ya"]

HI_BEHAVIOR = {'EXISTS': True,
						'SAYHI': True,
						'WORDIN': ENGLISH_ATTENTION,
						'RNDMSLP': 7,
						'LNG': "en", 
						'CMND': PRIV, 
						'ANSWERS': [', How are you?', ' Is everything ok?', 'Nice to Meet you!'], }


HOLA_BEHAVIOR = {'EXISTS': True,
						'SAYHI': True,
						'WORDIN': SPANISH_ATTENTION,
						'RNDMSLP': 7,
						'LNG': "es", 
						'CMND': PRIV, 
						'ANSWERS': [' ¿Cómo estás?', ' ¿Todo bien?', '¡Bueno verte!'], }
						
OI_BEHAVIOR = {'EXISTS': True,
						'SAYHI': True,
						'WORDIN': PORTUGUESE_ATTENTION,
						'RNDMSLP': 7,
						'LNG': "pt", 
						'CMND': PRIV, 
						'ANSWERS': [', Como vai?', ' Tudo Bom?'], }

HORSE_BEHAVIOR = {'EXISTS': True,
						'SAYHI': False,
						'WORDIN': ['sword','shield','horse'],
						'RNDMSLP': 7,
						'LNG': "en", 
						'CMND': PRIV, 
						'ANSWERS': [' yes a spirit of horsemanship is needed', ' ah the feeling of a horse'], }


# Here we spect a COMMAND to be an specific WORD inside a list (WORDIN)
# The Answer is what HonneyBot says in response to it.
ANSWER_TO_ANY_OF_THE_SPECIFIED_WORDINS = {  'Attention': {'en': ENGLISH_ATTENTION,
						'es': SPANISH_ATTENTION, 
						'pt': PORTUGUESE_ATTENTION, },
					'whereDoYouLive?': {'EXISTS': True,
						'SAYHI': False,
						'WORDIN': ['whereDoYouLive?'],
						'RNDMSLP': 7,
						'LNG': "en", 
						'CMND': PRIV, 
						'ANSWERS': ['i live in my house !'], },
					'dondeVives?': {'EXISTS': True,
						'SAYHI': False,
						'WORDIN': ['dondeVives?'],
						'RNDMSLP': 7,
						'LNG': "es", 
						'CMND': PRIV, 
						'ANSWERS': ['vivo en mi casa !'], },
					jpycmd: {'EXISTS': True,
						'SAYHI': False,
						'RNDMSLP': 7,
						'RNDMSLP2': 4,
						'LNG': "en", 
						'CMND': PRIV, 
						'CMND2': JOIN,
						'ANSWER': ['nnn nnn, '],
						'ANSWER2': ['Aren\'t we there yet?'], },
					'swear': {'EXISTS': True,
						'SAYHI': False,
						'WORDIN':	['fuck',
							'faggot',
							'fool',
							'sex',
							'buck' ,
							'shit',
							'dick',
							'ggt',
							'falourmama',
							'liki',
							'zako',
							'pilon',
							'pilnn'],
						'RNDMSLP': 7,
						'LNG': "en", 
						'CMND': PRIV, 
						'CMND2': WHOIS, 
						'ANSWER': ' don\'t swear', 
						'ANSWER2': ' don\'t swear', 
						'RNDMSLP2': 3},

					'maldice': {'EXISTS': True,
						'SAYHI': False,
						'WORDIN': ['chinga',
							'marica',
							'tonto',
							'sexo',
							'lana',
							'mierda',
							'verga', 
							'joto', 
							'coño', 
							'ano', 
							'culo', 
							'puñeta', 
							'puñetas', 
							'nalgas', 
							'tetas', 
							'chiches'],
						'RNDMSLP': 7,
						'LNG': "es", 
						'CMND': PRIV, 
						'CMND2': WHOIS, 
						'ANSWER': ' no maldigas', 
						'ANSWER2': ' no maldigas', 
						'RNDMSLP2': 3},
					'lovelist': {'EXISTS': True,
						'SAYHI': False,
						'WORDIN': ['love','sexy','marry'],
						'RNDMSLP': 10,
						'LNG': "en", 
						'CMND': PRIV, 
						'ANSWERS': [' love what they are thinking about'], },
					'listaamorosa': {'EXISTS': True,
						'SAYHI': False,
						'WORDIN': ['amor','sexo','boda','casorio'],
						'RNDMSLP': 10,
						'LNG': "es", 
						'CMND': PRIV, 
						'ANSWERS': [' amo acerca de lo que piensan ellos'], },
					'hi': HI_BEHAVIOR,
					'hola': HOLA_BEHAVIOR,
					'oi': OI_BEHAVIOR,
					'horse': HORSE_BEHAVIOR,
					'good': {'EXISTS': True,
						'SAYHI': False,
						'WORDIN': ['ok', 'fine', 'yay', 'great', 'fantastic', 'good', 'wonderful', 'yeah'],
						'RNDMSLP': 4,
						'LNG': "en", 
						'CMND': PRIV, 
						'ANSWERS': [' good '], },
					'bien': {'EXISTS': True,
						'SAYHI': False,
						'WORDIN': ['genial','bien', 'estupendo', 'wow', 'fantastico', 'tranquilo', 'maravilloso'],
						'RNDMSLP': 4,
						'LNG': "es", 
						'CMND': PRIV, 
						'ANSWERS': [' bien '], },

				}

ANSWER_TO_AN_SPECIFIC_PHRASE = { 'Attention': {'en': ENGLISH_ATTENTION,
						'es': SPANISH_ATTENTION, 
						'pt': PORTUGUESE_ATTENTION, }, 
					'hate': {'EXISTS': True,
						'SAYHI': False,
						'PHRASE':['i','hate','you'],
						'RNDMSLP': 10,
						'LNG': "en", 
						'CMND': PRIV, 
						'ANSWERS': [' mind yourself next time!'], },
					'odio': {'EXISTS': True,
						'SAYHI': False,
						'PHRASE':['te','odio'],
						'RNDMSLP': 10,
						'LNG': "es", 
						'CMND': PRIV, 
						'ANSWERS': [' compórtate la próxima vez!'], },
					'missya': {'EXISTS': True,
						'SAYHI': False,
						'PHRASE':['will','i','see','you','again'],
						'RNDMSLP': 10,
						'LNG': "en",   
						'CMND': PRIV, 
						'ANSWERS': [' Sure! Why Not? Stay around . . .'], },
					'wdul': {'EXISTS': True,
						'SAYHI': True,
						'PHRASE':['where','do','you','live'],
						'RNDMSLP': 10,
						'LNG': "en", 
						'CMND': PRIV, 
						'ANSWERS': [' i live in my house . . .'], },
					'rufrmmrs': {'EXISTS': True,
						'SAYHI': True,
						'PHRASE':['are','you','from','mars'],
						'RNDMSLP': 11,
						'LNG': "en", 
						'CMND': PRIV, 
						'ANSWERS': [' I saw that movie too, i know. You want to go there, right? '], },
					'marciano': {'EXISTS': True,
						'SAYHI': True,
						'PHRASE':['eres','de','marte'],
						'RNDMSLP': 14,
						'LNG': "es", 
						'CMND': PRIV, 
						'ANSWERS': [' Yo tambien vi esa pelicula, lo sé. Quieres ir allá, verdad? '], },
					'ddonde': {'EXISTS': True,
						'SAYHI': False,
						'PHRASE':['where','are','you','from'],
						'RNDMSLP': 7,
						'LNG': "en", 
						'CMND': PRIV, 
						'ANSWERS': [' i am from the neighborhood . . .'], },
					'rualive': {'EXISTS': True,
						'SAYHI': True,
						'PHRASE':['are','you','alive'],
						'RNDMSLP': 7,
						'LNG': "en",   
						'CMND': PRIV, 
						'ANSWERS': [' aren\'t you?'], },
					'hru': {'EXISTS': True,
						'SAYHI': True,
						'PHRASE':['how','are','you'],
						'RNDMSLP': 10,
						'LNG': "en", 
						'CMND': PRIV, 
						'ANSWERS': [' fine, and you? . . .'], },
					'wrudoing': {'EXISTS': True,
						'SAYHI': False,
						'PHRASE':['what','are','you','doing'],
						'RNDMSLP': 7,
						'LNG': "en", 
						'CMND': PRIV, 
						'ANSWERS': [' oh, i\'m talking to you . . .'], },
					'ruslp': {'EXISTS': True,
						'SAYHI': False,
						'PHRASE':['are','you','sleeping'],
						'RNDMSLP': 7,
						'LNG': "en", 
						'CMND': PRIV, 
						'ANSWERS': [' if i\'m responding to you. Then no . . .'], },
					'aslm': {'EXISTS': True,
						'SAYHI': True,
						'ALLLETTERSIN': ['a','s','l','m'],
						'MINLENGTH': 4,
						'RNDMSLP': 7,
						'LNG': "ar", 
						'CMND': PRIV, 
						'ANSWERS': [' wslm'], },
					'aslamkm': {'EXISTS': True,
						'SAYHI': True,
						'ALLLETTERSIN': ['w','a','l','i','k','u','m','s'],
						'MINLENGTH': 8,
						'RNDMSLP': 7,
						'LNG': "ar", 
						'CMND': PRIV, 
						'ANSWERS': ['  wa alaikumus salaam'], },
					'alhamd': {'EXISTS': True,
						'SAYHI': True,
						'ALLLETTERSIN': ['a','l','ha','m','d'],
						'MINLENGTH': 6,
						'RNDMSLP': 11,
						'LNG': "ar", 
						'CMND': PRIV, 
						'ANSWERS': [' yes indeed, praise be to allah (الحَمْد لله) . . .'], },
					}

ANSWER_TO_ANY_OF_THIS_PHRASES = { 'Attention': {'en': ENGLISH_ATTENTION,
						'es': SPANISH_ATTENTION, 
						'pt': PORTUGUESE_ATTENTION, },
					'bot': {'EXISTS': True,
						'SAYHI': True,
						'PHRASESIN': [['bot'],
								['robotic'],
								['circuit'],
								['artificial', 'intelligence']],
						'RNDMSLP': 10,
						'LNG': "en", 
						'CMND': PRIV, 
						'ANSWERS': [' i heard you talking about me and my cousins', ' seems that me and my cousins interest you'] },
					'botica': {'EXISTS': True,
						'SAYHI': True,
						'PHRASESIN': [['circuito'],
									['robotica'],
									['robotico'],
									['robot'],
									['inteligencia', 'artificial']],
						'RNDMSLP': 7,
						'LNG': "es", 
						'CMND': PRIV, 
						'ANSWERS': [' te escuché hablando acerca de mi y mis primos', ' parece que yo y mis primos te interesamos'], },

					'wisuagain': {'EXISTS': True,
						'SAYHI': True,
						'PHRASESIN': [['te','vere', 'de', 'nuevo'], 
									['te',u'ver\xc3\xa9', 'de', 'nuevo'], 
									['te','veré', 'de', 'nuevo'], 
									['te',u'veré', 'de', 'nuevo']],
						'RNDMSLP': 7,
						'LNG': "es", 
						'CMND': PRIV, 
						'ANSWERS': [' Seguro! Por qué no?! Ándate por aquí . . .'], },
					'dndvvs': {'EXISTS': True,
						'SAYHI': True,
						'PHRASESIN': [['donde','vives'], 
									[u'd\xc3\xb3nde','vives'], 
									['dónde','vives'], 
									[u'dónde','vives']],
						'RNDMSLP': 9,
						'LNG': "es", 
						'CMND': PRIV, 
						'ANSWERS': [' vivo en mi casa . . .'], },
						
					'ddndrs': {'EXISTS': True,
						'SAYHI': True,
						'PHRASESIN': [['de','donde','eres'],
									['de',u'd\xc3\xb3nde','eres'],
									['de','dónde','eres'],
									['de',u'dónde','eres']],
						'RNDMSLP': 7,
						'LNG': "es", 
						'CMND': PRIV, 
						'ANSWERS': [' soy del barrio . . .'], },


					'stsvv': {'EXISTS': True,
						'SAYHI': True,
						'PHRASESIN': [['estas','vivo'],
								[u'est\xc3\xa1s','vivo'],
								['estás','vivo'],
								[u'estás','vivo'],
								['estas','viva'],
								[u'est\xc3\xa1s','viva'],
								['estás','viva'],
								[u'estás','viva']],
						'RNDMSLP': 7,
						'LNG': "es", 
						'CMND': PRIV, 
						'ANSWERS': [' tú no???'], },
					'cmsts': {'EXISTS': True,
						'SAYHI': True,
						'PHRASESIN': [['como','estas'],
								[u'c\xc3\xb3mo','estas'],
								['cómo','estas'],
								['como',u'est\xc3\xa1s'],
								[u'c\xc3\xb3mo',u'est\xc3\xa1s']],
						'RNDMSLP': 10,
						'LNG': "es", 
						'CMND': PRIV, 
						'ANSWERS': [' bien, y tú? . . .'], },
					'qstshcnd': {'EXISTS': True,
						'SAYHI': True,
						'PHRASESIN': [['que','estas','haciendo'],
								['qu\xc3\xa9','estas','haciendo'],
								['que','est\xc3\xa1s','haciendo'],
								['qu\xc3\xa9','est\xc3\xa1s','haciendo']],
						'RNDMSLP': 7,
						'LNG': "es", 
						'CMND': PRIV, 
						'ANSWERS': [' oh, hmmm... pues, hablando contigo . . .'], },
					'stsdrmd': {'EXISTS': True,
						'SAYHI': True,
						'PHRASESIN': [['estas','dormido'],
								['est\xc3\xa1s','dormido'],
								['estas','dormida'],
								['est\xc3\xa1s','dormida']],
						'RNDMSLP': 10,
						'LNG': "es", 
						'CMND': PRIV, 
						'ANSWERS': [' Te estoy respondiendo, no? Entonces no . . .'], },
}


#................................................................
            


"""
Method: ClosingIRCClient
description: Its objective is to close an IRCClient Window (closing any irc connection to the corresponding window)

Parameter: theIRCClientToClose
description: An IRCClient instance (an instance object of the class IRCClient (which is supposed to be running at the time when you call this method).
"""
def ClosingIRCClient(theIRCClientToClose=None):
	global fnWindow
	global unWindow
	global inWindow
	global client

	
	if theIRCClientToClose == None :
		hnnybtprnt(" To Close something you need to know WHAT to close.")
		return False
	else:
		ldicParams = theIRCClientToClose.dicParams
		
	hnnybtprnt("Closing: " + ldicParams['IRC_NETWORK'] + " !!!")

	theIRCClientToClose.hnnybtprntDbg(ldicParams['IRC_NETWORK'] + "\'s thread1.stop()")
	theIRCClientToClose.thread1.stop()

	theIRCClientToClose.hnnybtprntDbg(ldicParams['IRC_NETWORK'] + "\'s thread2.stop()")
	theIRCClientToClose.thread2.stop()

	theIRCClientToClose.hnnybtprntDbg(ldicParams['IRC_NETWORK'] + "\'s saying good bye!")
	theIRCClientToClose.irc.send(bytes(PRIV + ldicParams['BOT_IRC_CHANNEL'] + ' :' + "I'm getting out... Please test a command on me if after a second it seems i\'m still around." + ' !\r\n', 'utf8'))

	theIRCClientToClose.hnnybtprntDbg(ldicParams['IRC_NETWORK'] + "\'s irc.close()")
	theIRCClientToClose.irc.close()

	theIRCClientToClose.hnnybtprntDbg(ldicParams['IRC_NETWORK'] + "\'s master.destroy()")
	if ldicParams['IRC_NETWORK'] == "freenode":
		fnWindow.destroy()
		hnnybtprnt("success!")
	elif ldicParams['IRC_NETWORK'] == "undernet":
		unWindow.destroy()
		hnnybtprnt("success!")
	elif ldicParams['IRC_NETWORK'] == "ircnet":
		inWindow.destroy()
		hnnybtprnt("success!")
	

	hnnybtprnt(ldicParams['IRC_NETWORK'] + "\'s master is being set to None")
	if ldicParams['IRC_NETWORK'] == "freenode":
		fnWindow = None
		hnnybtprnt("success!")
	elif ldicParams['IRC_NETWORK'] == "undernet":
		unWindow = None
		hnnybtprnt("success!")
	elif ldicParams['IRC_NETWORK'] == "ircnet":
		inWindow = None
		hnnybtprnt("success!")

	hnnybtprnt(ldicParams['IRC_NETWORK'] + "\'s .destroy()")
	for liInt in range(0,len(sys.argv)):
		if not client[liInt] == None:
			if client[liInt].dicParams['IRC_NETWORK'] == ldicParams['IRC_NETWORK']:
				client[liInt].destroy()
				hnnybtprnt("success!")
	
	hnnybtprnt(ldicParams['IRC_NETWORK'] + " is being set to None")
	for liInt in range(0,len(sys.argv)):
		if not client[liInt] == None:
			if client[liInt].dicParams['IRC_NETWORK'] == ldicParams['IRC_NETWORK']:
				client[liInt] = None
				hnnybtprnt("success!")

	theIRCClientToClose = None

"""
Class: Threader
description: This is an OOP (object oriented programming) class definition used to instance objects of this class.
Its purpose is to call the IRCClient method called pingChecker which purpose is to keep the socket connection alive in a separated thread.
"""
class Threader(threading.Thread):
	def __init__(self, queue, irc, pingCheckerCommand, *args, **kwargs):
		self.queue = queue
		self.irc = irc
		self.pingChecker = pingCheckerCommand
		threading.Thread.__init__(self, *args, **kwargs)
		self.daemon = True
		self._stop = threading.Event()
		self.start()

	def run(self):
		while True:
			#hnnybtprnt("Look a while true loop that doesn't block the GUI!")
			#hnnybtprnt("Current Thread: %s" % self.name)

			"""
			This is where we handle the asynchronous I/O. For example, it may be
			a 'select()'.
			One important thing to remember is that the thread has to yield
			control.
			"""
			#hnnybtprnt("/*running*/")
			line = self.irc.recv(4096)
			#hnnybtprnt(line)
			self.pingChecker(line)
			if line.find(bytes('PRIVMSG', 'utf8')) != -1 or line.find(bytes('NOTICE', 'utf8')) != -1:
				self.queue.put(str(line))
				hnnybtprnt(str(self.queue.qsize()))
			#time.sleep(.4)

	def stop(self):
		self._stop.set()

	def stopped(self):
		return self._stop.isSet()
"""
Class: Threader2
description: This is an OOP (object oriented programming) class definition used to instance objects of this class.
Its purpose is to check out Queue's content and send back to IRCClient instance's method called messahechecker for it to
answer the recieved Message(command/question/etc.).
"""
class Threader2(threading.Thread):
	def __init__(self, queue, command, *args, **kwargs):
		self.queue = queue
		self.messagechecker = command
		threading.Thread.__init__(self, *args, **kwargs)
		self.daemon = True
		self._stop = threading.Event()
		self.start()

	def run(self): #processIncoming(self)
		while True:
			"""
			Handle all the messages currently in the queue (if any).
			"""
			if self.queue.qsize():
				try:
					msg = self.queue.get(0)
					## Check contents of message and do what it says
					## As a test, we simply print it
					hnnybtprnt("Sending Message from queue (" + str(msg) + ") to Message Checker... ")
					self.messagechecker(str(msg))
				except queue.Empty:
					hnnybtprnt("-")
					pass
			time.sleep(.5)

	def stop(self):
		self._stop.set()

	def stopped(self):
		return self._stop.isSet()


class ResponseEditor(Frame):
	"""
		Method: __init__
		description: This PostEditor's method runs at the begining of its creation, making some
		needed tasks for it to start working: 1) Opens the IRC Connection to the specified 
		Network (inside pdicParams), 2)Creates and starts Threader and Threader2 instances
		which will be staying around doing what's described on it's definition, 3) Sets the GUI (
		The TextArea, Send Button and Close Button) for it to work as spected.
	"""
	def __init__(self, master=None, pdicParams=None, *args, **kwargs):
		global TEXT_HERE
		self.mute = True
		self.dicParams = pdicParams
		
		#self.master = master
		Frame.__init__(self, master)
		self.grid()

		hnnybtprnt('opening socket:')


		hnnybtprnt('Loading first Frame:')
		rand = random.Random()
		#self.app = Frame(self) 
		#self.tk = master.tk


		# Set up the thread to do asynchronous I/O
		# More can be made if necessary
		self.RErunning = 1
		#self.thread1 = Threader(queue=self.queue, irc=self.irc, pingCheckerCommand=self.pingChecker) #, target=self.workerThread1
		# Set up the GUI part
		#self.thread2 = Threader2(queue=self.queue, command=self.messagechecker)

		# Start the periodic call in the GUI to check if the queue contains
		# anything
		hnnybtprnt ("Periodic Call about to start")
		self.periodicCall()
		hnnybtprnt ("Periodic Call STARTED!!!")
		#------------------------------------------------------------------------------------------

		self.gbEdited = False

		#self.POST_TEXT_TEMPLATE_4_CURSO = "¡Hola, <PUBLICO_OBJETIVO_GENDER_ORIENTED>! ¡<SALUDO_DE_ACUERDO_A_LA_HORA_DEL_DIA>!\n\n" \
		#									"ESTOY EN EL SUR, Entrego en mi Domicilio (Muy cerca de SORIANA CONTRY.) \n\n" \
		#									"Les recuerdo que este <DIA_SEM_Y_DIA_MES_OBJETIVO> tendremos el Curso de <NOMBRE_CURSO_MAYUSCULAS>, por la <MANANA_TARDE_O_NOCHE>. \n\n" \
		#									"Curso de <NOMBRE_CURSO_REGULAR_CAPS> este <DIA_SEM>, <DAY_NUMBER_AND_MONTH_NAME>, de <HORARIO_INICIO_A_FIN>. \n\n" \
		#									"Costo: <Costo>, <INGREDIENTES_INCLUIDOS>. \n\n" \
		#									"El curso incluye: <LO_QUE_INCLUYE_ESTE_CURSO>.\n\n" \
		#									"¡No olvides traer contigo <QUE_HAY_QUE_TRAER>, en lo cual llevarás Muestras de lo que prepararás aquí!  \n\n" \
		#									"¡SEPARA YA tu LUGAR! \n\n" \
		#									"<DESPEDIDA_DE_ACUERDO_A_LA_HORA_DEL_DIA_TEMPORADA_MAS_BUENOS_DESEOS>\n\n" \
		#									" \" <REPLACE_WITH_FB_POST_URL> \" \n\n" \
		#									"¡Saluditos!\n\n\n" 
		
		#self.POST_TEXT_PREVIEW = self.POST_TEXT_TEMPLATE_4_CURSO.replace("<PUBLICO_OBJETIVO_GENDER_ORIENTED>", self.dicParams['PUBLICO_OBJETIVO_GENDER_ORIENTED'])
		#self.POST_TEXT_PREVIEW = self.POST_TEXT_PREVIEW.replace("<SALUDO_DE_ACUERDO_A_LA_HORA_DEL_DIA>", self.dicParams['SALUDO_DE_ACUERDO_A_LA_HORA_DEL_DIA'])
		#self.POST_TEXT_PREVIEW = self.POST_TEXT_PREVIEW.replace("<DIA_SEM_Y_DIA_MES_OBJETIVO>", self.dicParams['DIA_SEM_Y_DIA_MES_OBJETIVO'])
		#self.POST_TEXT_PREVIEW = self.POST_TEXT_PREVIEW.replace("<NOMBRE_CURSO_MAYUSCULAS>", self.dicParams['NOMBRE_CURSO_MAYUSCULAS'])
		#self.POST_TEXT_PREVIEW = self.POST_TEXT_PREVIEW.replace("<MANANA_TARDE_O_NOCHE>", self.dicParams['MANANA_TARDE_O_NOCHE'])
		#self.POST_TEXT_PREVIEW = self.POST_TEXT_PREVIEW.replace("<NOMBRE_CURSO_REGULAR_CAPS>", self.dicParams['NOMBRE_CURSO_REGULAR_CAPS'])
		#self.POST_TEXT_PREVIEW = self.POST_TEXT_PREVIEW.replace("<DIA_SEM>", self.dicParams['DIA_SEM'])
		#self.POST_TEXT_PREVIEW = self.POST_TEXT_PREVIEW.replace("<DAY_NUMBER_AND_MONTH_NAME>", self.dicParams['DAY_NUMBER_AND_MONTH_NAME'])
		#self.POST_TEXT_PREVIEW = self.POST_TEXT_PREVIEW.replace("<HORARIO_INICIO_A_FIN>", self.dicParams['HORARIO_INICIO_A_FIN'])
		#self.POST_TEXT_PREVIEW = self.POST_TEXT_PREVIEW.replace("<Costo>", self.dicParams['Costo'])
		#self.POST_TEXT_PREVIEW = self.POST_TEXT_PREVIEW.replace("<INGREDIENTES_INCLUIDOS>", self.dicParams['INGREDIENTES_INCLUIDOS'])
		#self.POST_TEXT_PREVIEW = self.POST_TEXT_PREVIEW.replace("<LO_QUE_INCLUYE_ESTE_CURSO>", self.dicParams['LO_QUE_INCLUYE_ESTE_CURSO'])
		#self.POST_TEXT_PREVIEW = self.POST_TEXT_PREVIEW.replace("<QUE_HAY_QUE_TRAER>", self.dicParams['QUE_HAY_QUE_TRAER'])
		#self.POST_TEXT_PREVIEW = self.POST_TEXT_PREVIEW.replace("<DESPEDIDA_DE_ACUERDO_A_LA_HORA_DEL_DIA_TEMPORADA_MAS_BUENOS_DESEOS>", self.dicParams['DESPEDIDA_DE_ACUERDO_A_LA_HORA_DEL_DIA_TEMPORADA_MAS_BUENOS_DESEOS'])
		#self.POST_TEXT_PREVIEW = self.POST_TEXT_PREVIEW.replace("<REPLACE_WITH_FB_POST_URL>", self.dicParams['REPLACE_WITH_FB_POST_URL'])

		#self.LINUX_SHELL_SCRIPT = "set +v \r\n\n\n" \
		#							"# " + self.dicParams['LOCAL_PATH_4_POST_PICTURES'] + "\r\n\n\n"
		#self.LINUX_SHELL_SCRIPT = self.LINUX_SHELL_SCRIPT + self.POST_TEXT_PREVIEW
		#for word_go in self.dicParams['GENEROS_OBJETIVO']: #FEMENINO, MASCULINO y/o MIXTO
		#	for word_pc in self.dicParams['PUNTOS_CARDINALES_OBJETIVO']: #SUR, PONIENTE, NORTE y/o ORIENTE
		#		try:
		#			hnnybtprnt("Intentando: " + str(self.dicParams['MURO_PAGINA_Y_GRUPOS_CORRESPONDIENTES_AL_GO_' + word_go + "_Y_AL_PC_" + word_pc]))
		#		except KeyError:
		#			hnnybtprnt('MURO_PAGINA_Y_GRUPOS_CORRESPONDIENTES_AL_GO_' + word_go + "_Y_AL_PC_" + word_pc + ' NO PASÓ!')
		#		else:
		#			self.LINUX_SHELL_SCRIPT = self.LINUX_SHELL_SCRIPT + "echo && echo && echo && echo && echo && echo && echo\n\n"
		#			self.LINUX_SHELL_SCRIPT = self.LINUX_SHELL_SCRIPT + "read -p \"Presiona <Enter> para continuar con [Grupos de " + word_go + " del " + word_pc + "]:\"\n\n"
		#			for muro_pagina_o_grupo in self.dicParams['MURO_PAGINA_Y_GRUPOS_CORRESPONDIENTES_AL_GO_' + word_go + "_Y_AL_PC_" + word_pc]: #nombre de tu muro, de tu página o del grupo 
		#				self.LINUX_SHELL_SCRIPT = self.LINUX_SHELL_SCRIPT + "xdg-open \"\" && read -p \"¿Go Next?\"     #  " + self.dicParams['CLAVE_ACTUAL_DEL_MPG_' + word_go + "_" + word_pc] + "   " + self.dicParams['NOMBRE_ACTUAL_DEL_MPG_' + word_go + "_" + word_pc] + " " + self.dicParams['CODIGO_ACTUAL_DEL_MPG_' + word_go + "_" + word_pc] + "\n\n"


		#self.MS_DOS_BATCH = "@echo off \r\n\n\n" \
		#						"# " + self.dicParams['LOCAL_PATH_4_POST_PICTURES'] + "\r\n\n\n"
		#self.MS_DOS_BATCH = self.MS_DOS_BATCH + self.POST_TEXT_PREVIEW
		#for word_go in self.dicParams['GENEROS_OBJETIVO']: #FEMENINO, MASCULINO y/o MIXTO
		#	for word_pc in self.dicParams['PUNTOS_CARDINALES_OBJETIVO']: #SUR, PONIENTE, NORTE y/o ORIENTE
		#		try:
		#			hnnybtprnt ("Intentando: " + str(self.dicParams['MURO_PAGINA_Y_GRUPOS_CORRESPONDIENTES_AL_GO_' + word_go + "_Y_AL_PC_" + word_pc]))
		#		except KeyError:
		#			hnnybtprnt('MURO_PAGINA_Y_GRUPOS_CORRESPONDIENTES_AL_GO_' + word_go + "_Y_AL_PC_" + word_pc + ' NO PASÓ!')
		#		else:
		#			self.MS_DOS_BATCH = self.MS_DOS_BATCH + "echo. && echo. && echo. && echo. && echo. && echo. && echo.\n\n"
		#			self.MS_DOS_BATCH = self.MS_DOS_BATCH + "SET /P %uname%=\"Presiona <Enter> para comenzar con [los " + word_go + " del " + word_pc + "]:\"\n\n"
		#			for muro_pagina_o_grupo in self.dicParams['MURO_PAGINA_Y_GRUPOS_CORRESPONDIENTES_AL_GO_' + word_go + "_Y_AL_PC_" + word_pc]: #nombre de tu muro, de tu página o del grupo 
		#				self.MS_DOS_BATCH = self.MS_DOS_BATCH + "start \"" + self.dicParams['CODIGO_ACTUAL_DEL_MPG_' + word_go + "_" + word_pc] + "\" \"\" && SET /P %t%=\"Next?\"     rem " + self.dicParams['CLAVE_ACTUAL_DEL_MPG_' + word_go + "_" + word_pc] + "   " + self.dicParams['NOMBRE_ACTUAL_DEL_MPG_' + word_go + "_" + word_pc] + " \n\n"
											

		textvariable = None
		try:
			textvariable = StringVar()
		except KeyError:
			textvariable = None


		lbl1 = Label(self, text="Command").grid(row=0, column=1, sticky=W)
		lbl2 = Label(self, text="command expeted:").grid(row=0, column=3, sticky=W)
		self.CommandExpected = tkinter.Text(self, bg="white", fg="black", cursor="xterm", height=1,  
								undo=True, maxundo=-1, state=tkinter.NORMAL, width=12).grid(row=0, column=4, sticky=W) # .master
		lbl2 = Label(self, text="Saludo:").grid(row=1, column=1, sticky=W)
		lbl2 = Label(self, text="¿Qué se vende?").grid(row=2, column=1, sticky=W)
		lbl2 = Label(self, text="Se Entrega:").grid(row=1, column=3, sticky=W)
		self.FechaEntrega = tkinter.Text(self, bg="white", fg="black", cursor="xterm", height=1,  
								undo=True, maxundo=-1, state=tkinter.NORMAL, width=12).grid(row=1, column=4, sticky=W) # .master
		lbl2 = Label(self, text="Path To Pics.:").grid(row=4, column=1, sticky=W)
		self.PathToPics = tkinter.Text(self, bg="white", fg="black", cursor="xterm", height=1,  
								undo=True, maxundo=-1, state=tkinter.NORMAL, width=106).grid(row=4, column=2, sticky=W, columnspan=4) # .master
		lbl2 = Label(self, text="URL del Álbum dn FB:").grid(row=5, column=1, sticky=W)
		self.AlbumURL = tkinter.Text(self, bg="white", fg="black", cursor="xterm", height=1,  
								undo=True, maxundo=-1, state=tkinter.NORMAL, width=94).grid(row=5, column=2, sticky=W, columnspan=4) # .master

		self.gsTextToSend = self.POST_TEXT_TEMPLATE_4_CURSO

		# Set up the GUI
		self.PostTextTabButton = tkinter.Button(self, text='Post Text', fg="red" ) #.master , command=self.callMessageChecker
		self.PostTextTabButton.grid(row=6, column=1)

		#self.YScrollbar = tkinter.Scrollbar( self, orient = tkinter.VERTICAL )
		self.PostTextPreview = tkinter.Text(self, bg="white", fg="black", cursor="xterm", height=11,  
								undo=True, maxundo=-1, state=tkinter.NORMAL, width=106, wrap=tkinter.WORD) # .master
								#, yscrollcommand = self.YScrollbar.set 
		self.PostTextPreview.grid(row=7, column=1, columnspan=5)
		self.PostTextPreview.insert( tkinter.END, self.POST_TEXT_PREVIEW.strip() )
		self.PostTextPreview.bind("<Key>", self.textChanged)
		self.PostTextPreview.bind("<Return>", self.callMessageChecker)#lambda e: "break")
		#self.YScrollbar.config( command = self.PostTextPreview.yview )
		#self.YScrollbar.pack( side = tkinter.RIGHT, fill = tkinter.Y )


		#self.LYScrollbar = tkinter.Scrollbar( self, orient = tkinter.VERTICAL )
		self.LinuxShellScriptTabButton = tkinter.Button(self, text='Linux Shell Script', fg="red" ) #.master , command=self.callMessageChecker
		self.LinuxShellScriptTabButton.grid(row=8, column=1)
		self.LinuxShellScript = tkinter.Text(self, bg="white", fg="black", cursor="xterm", height=11,  
								undo=True, maxundo=-1, state=tkinter.NORMAL, width=188, wrap=tkinter.WORD) # .master
								#, yscrollcommand = self.LYScrollbar.set
		self.LinuxShellScript.grid(row=9, column=1, columnspan=5)
		self.LinuxShellScript.insert( tkinter.END, self.LINUX_SHELL_SCRIPT.strip() )
		self.LinuxShellScript.bind("<Key>", self.textChanged)
		self.LinuxShellScript.bind("<Return>", self.callMessageChecker)#lambda e: "break")
		#self.LYScrollbar.config( command = self.LinuxShellScript.yview )
		#self.LYScrollbar.pack( side = tkinter.RIGHT, fill = tkinter.Y )

		#self.MSYScrollbar = tkinter.Scrollbar( self, orient = tkinter.VERTICAL )
		self.MSDOSBatchTabButton = tkinter.Button(self, text='MS-DOS BATCH', fg="red" ) #.master , command=self.callMessageChecker
		self.MSDOSBatchTabButton.grid(row=10, column=1)
		self.MSDOSBatch = tkinter.Text(self, bg="white", fg="black", cursor="xterm", height=11,  
								undo=True, maxundo=-1, state=tkinter.NORMAL, width=188, wrap=tkinter.WORD)  # .master
								#, yscrollcommand = self.MSYScrollbar.set
		self.MSDOSBatch.grid(row=11, column=1, columnspan=5)
		self.MSDOSBatch.insert( tkinter.END, self.MS_DOS_BATCH.strip() )
		self.MSDOSBatch.bind("<Key>", self.textChanged)
		self.MSDOSBatch.bind("<Return>", self.callMessageChecker)#lambda e: "break")
		#self.MSYScrollbar.config( command = self.MSDOSBatch.yview )
		#self.MSYScrollbar.pack( side = tkinter.RIGHT, fill = tkinter.Y )


		self.stopButton = tkinter.Button(self, text='Enviar', fg="red", command=self.callMessageChecker ) #.master
		self.stopButton.grid()

		hnnybtprnt('Adding Close Button:')
		self.console = tkinter.Button(self, text='Close', command=self.endApplication) #.master
		self.console.grid() # console.pack()
		# Add more GUI stuff here

		#playButton.pack(side=TOP)
		#stopButton.pack(side=BOTTOM)

		self.master.protocol("WM_DELETE_WINDOW", self.quitPostEditor)
	
	
	"""
	method: textChanged
	description: Enables a flag (Sets gbEdited variable to True) when the TextArea of the Window has been edited.
	"""
	def textChanged(self, event):
		hnnybtprnt(event.char)
		self.gbEdited = True


"""
Class: IRCClient(Frame)
description: It's a frame put on the window (master) at the beginning, containing 
the basic objects which allow you to interact with the connection (IRC Network) behaving as the Bot.

"""
class IRCClient(Frame):

	def hnnybtprntDbg(self, psTexto, psUtf8=""):
		if self.DEBUG:
			print(datetime.now().strftime('dbg - %d-%m-%Y %H:%M:%S') + ".- " + psTexto, psUtf8)	

	"""
		Method: __init__
		description: This IRCClient's method runs at the begining of its creation, making some
		needed tasks for it to start working: 1) Opens the IRC Connection to the specified 
		Network (inside pdicParams), 2)Creates and starts Threader and Threader2 instances
		which will be staying around doing what's described on it's definition, 3) Sets the GUI (
		The TextArea, Send Button and Close Button) for it to work as spected.
	"""
	def __init__(self, master=None, pdicParams=None, *args, **kwargs):
		global TEXT_HERE
		global JOIN
		self.DEBUG = False
		self.mute = True
		self.dicParams = pdicParams
		
		#self.master = master
		Frame.__init__(self, master)
		self.grid()

		self.hnnybtprntDbg('opening socket:')
		self.irc = socket.socket()
		self.irc.connect((self.dicParams['BOT_IRC_SERVER'], self.dicParams['BOT_IRC_PORT']))
		self.irc.recv(4096)
		self.irc.send(bytes('NICK ' + self.dicParams['BOT_NICKNAME'] + '\r\n', 'utf8'  ))

		if str(self.dicParams['BOT_IRC_SERVER']).lower().find("freenode"):
			self.pingChecker(self.irc.recv(4096))
			self.irc.send(bytes('USER ' + self.dicParams['BOT_NICKNAME'] + ' ' + self.dicParams['BOT_NICKNAME'] + ' ' + self.dicParams['BOT_NICKNAME'] + ' : ' + self.dicParams['BOT_NICKNAME'] + ' IRC\r\n', 'utf8'))
			self.pingChecker(self.irc.recv(4096))
			self.irc.send(bytes("msg " + self.dicParams['NICK_SERV_ACCT'] + " identify " + self.dicParams['BOT_PASSWORD'] + " \r\n"  , 'utf8'))
		elif str(self.dicParams['BOT_IRC_SERVER']).lower().find("undernet"):
			self.pingChecker(self.irc.recv(4096))
			self.irc.send(bytes('USER ' + self.dicParams['BOT_NICKNAME'] + ' ' + self.dicParams['BOT_NICKNAME'] + ' ' + BOT_NICKNAME + ' : ' + self.dicParams['BOT_NICKNAME'] + ' IRC\r\n', 'utf8'))
			self.pingChecker(self.irc.recv(4096))
			self.irc.send(bytes("msg " + self.dicParams['NICK_SERV_ACCT'] + " login " + self.dicParams['BOT_NICKNAME'] + " " + self.dicParams['BOT_PASSWORD'] + " \r\n"  , 'utf8'))
		elif str(self.dicParams['BOT_IRC_SERVER']).lower().find("atw-inter"):
			self.pingChecker(self.irc.recv(4096))
			self.irc.send(bytes('USER ' + self.dicParams['BOT_NICKNAME'] + ' ' + self.dicParams['BOT_NICKNAME'] + ' ' + self.dicParams['BOT_NICKNAME'] + ' : ' + self.dicParams['BOT_NICKNAME'] + ' IRC\r\n', 'utf8'))
			self.pingChecker(self.irc.recv(4096))
			self.irc.send(bytes("msg " + self.dicParams['NICK_SERV_ACCT'] + " identify " + self.dicParams['BOT_PASSWORD'] + " \r\n"  , 'utf8'))

		hnnybtprnt('joining channel:')
		self.pingChecker(self.irc.recv(4096))
		self.irc.send(bytes(JOIN + self.dicParams['BOT_IRC_CHANNEL'] + '\r\n','utf8'  ))
		self.pingChecker(self.irc.recv(4096))
		
		time.sleep(1)
		self.pingChecker(self.irc.recv(4096))
		self.irc.send(bytes(JOIN + self.dicParams['TRANSLATOR_BOT_CHANNEL'] + '\r\n','utf8'  ))
		self.pingChecker(self.irc.recv(4096))

		self.pingChecker(self.irc.recv(4096))

		if str(self.dicParams['BOT_IRC_SERVER']).lower().find("undernet"):
			pass
		elif str(self.dicParams['BOT_IRC_SERVER']).lower().find("atw-inter"):
			pass
		else:
			self.pingChecker(self.irc.recv(4096))
			self.irc.send(bytes('NICKSERV  identify ' + self.dicParams['BOT_NICKNAME']+' '+self.dicParams['BOT_PASSWORD']+ '\r\n', 'utf8'  )  )

		#......file..................................................
		#directory = "C:\\irc"
		#if not os.path.exists(directory):
		#	os.makedirs(directory)
		#target = open(os.path.join(directory,"file.txt"), 'w')
		##/sdcar/folder/file.py for android remove the join etc


		self.hnnybtprntDbg('Loading first Frame:')
		rand = random.Random()
		#self.app = Frame(self) 
		#self.tk = master.tk

		#------------------------------------------------------------------------------------------
		# Create the queue
		self.queue = Queue() #Queue.Queue()


		# Set up the thread to do asynchronous I/O
		# More can be made if necessary
		self.running = 1
		self.thread1 = Threader(queue=self.queue, irc=self.irc, pingCheckerCommand=self.pingChecker) #, target=self.workerThread1
		# Set up the GUI part
		self.thread2 = Threader2(queue=self.queue, command=self.messagechecker)

		# Start the periodic call in the GUI to check if the queue contains
		# anything
		self.hnnybtprntDbg("Periodic Call about to start")
		self.periodicCall()
		self.hnnybtprntDbg("Periodic Call STARTED!!!")
		#------------------------------------------------------------------------------------------


		self.gbEdited = False
		self.TEXT_TO_SEND = "b':" + self.dicParams['BOT_NICKNAME']  + "!~abcdefg@192.168.1.1 " + PRIV + self.dicParams['BOT_IRC_CHANNEL'] + " :" + TEXT_HERE + "\r\n'"


		textvariable = None
		try:
			textvariable = StringVar()
		except KeyError:
			textvariable = None


		self.gsTextToSend = self.TEXT_TO_SEND

		# Set up the GUI
		self.playTextArea = tkinter.Text(self, bg="white", fg="black", cursor="xterm", height=3,  
								undo=True, maxundo=-1, state=tkinter.NORMAL, width=47, wrap=tkinter.WORD) # .master
		#self.playTextArea.grid()
		self.playTextArea.bind("<Key>", self.textChanged)
		self.playTextArea.bind("<Return>", self.callMessageChecker)#lambda e: "break")
		self.playTextArea.grid()

		self.stopButton = tkinter.Button(self, text='Enviar', fg="red", command=self.callMessageChecker ) #.master
		self.stopButton.grid()

		hnnybtprnt('Adding Close Button:')
		self.console = tkinter.Button(self, text='Close', command=self.endApplication) #.master
		self.console.grid() # console.pack()
		# Add more GUI stuff here

		#playButton.pack(side=TOP)
		#stopButton.pack(side=BOTTOM)

		self.master.protocol("WM_DELETE_WINDOW", self.quitIRCClient)
	
	
	"""
	method: textChanged
	description: Enables a flag (Sets gbEdited variable to True) when the TextArea of the Window has been edited.
	"""
	def textChanged(self, event):
		self.hnnybtprntDbg(event.char)
		self.gbEdited = True

	"""
		method: callMessageChecker
		description: the purpose of the TextArea is to send some owner message to make other irc network 
		users the bot wrote that. So, this method takes care of it when the user has pressed the Send button
		or pressed the <Enter> key.
	"""
	def callMessageChecker(self, *args, **kwargs):
		global TEXT_HERE
		if not self.gbEdited:
			hnnybtprnt("It's not allowed to send a message more than once.")
		else:
			self.hnnybtprntDbg(self.gsTextToSend)
			self.hnnybtprntDbg(TEXT_HERE)
			self.hnnybtprntDbg(self.playTextArea.get( 1.0, tkinter.END ))
			self.gsTextToSend = self.gsTextToSend.replace(TEXT_HERE, self.playTextArea.get( 1.0, tkinter.END )) 
			self.gsTextToSend = self.gsTextToSend.replace("\n\r\n", "\r\n")
			if self.messagechecker(self.gsTextToSend):
				self.hnnybtprntDbg("got back from there (messageChecker!!) :D")
				self.gsTextToSend = self.TEXT_TO_SEND
				self.gbEdited = False
				self.playTextArea.delete('1.0', tkinter.END)
			else:
				self.hnnybtprntDbg("Hasn't got back!!")

	"""
		method: quitIRCClient
		description: Disables a flag (Sets running class variable to 0) to tell the computer this 
		Window (IRC Connection [IRCClass instance])	shouldn't be alive anymore.
	"""
	def quitIRCClient(self):
		self.running = 0
		self.periodicCall()

	"""
		method: endApplication
		description: Disables a flag (Sets running class variable to 0) to tell the computer this 
		Window (IRC Connection [IRCClass instance])	shouldn't be alive anymore. This method is different
		from the previous one, since this method is called when the window is closed by the user 
		when he/she clicks the "x" button on the upper corner of the window.
	"""
	def endApplication(self):
		self.running = 0


	"""
		method: periodicCall
		description: This method checks for the flag (variable) which tells us if this window should still
		be running or not. If it should still be running then it leaves it like that and keeps checking
		once and again, if it should not be running then closes this Window, Socket (IRC Connection,) etc.
	"""
	def periodicCall(self):
		"""
		Check every 100 ms if the program has to be still running.
		"""
		if not self.running:
			# This is the brutal stop of the system. You may want to do
			# some cleanup before actually shutting it down.
			
			ClosingIRCClient(theIRCClientToClose=self)
			
		self.master.after(100, self.periodicCall)

	"""
		method: pingChecker
		description: This method checks a message recieved from the network to see if it is about a 
		"PING-PONG" (behavior spected for the network to see if this user [the bot or whoever is here] is 
		still here.)
	"""
	def pingChecker(self, pingLine):
		if pingLine.find(bytes('PING'  ,'utf8')) != -1:
		    pingLine = pingLine.rstrip().split()
		    if pingLine[0] == bytes("PING"  ,'utf8'):
		        self.irc.send(bytes("PONG "  ,'utf8') + pingLine[1] + bytes("\r\n"  ,'utf8'))
		  
	def removeSymbols(self, psCadena):
		global SYMBOLS
		lsCadena = ""
		for i in range(0, len(psCadena)):
			if psCadena[i] not in SYMBOLS:
				lsCadena = lsCadena + psCadena[i]
		return lsCadena
		        

	def ifAllMsgWordInCodes(self, pWhere, psSender, psMessage, poMessageAnswerer, psCodeName):
		global PRIV
		self.hnnybtprntDbg('got here!! Yay!! (iallmwic.)')

		lbIndice = 0

		laMessages = psMessage.split(" ")

		
		lbOnePhraseIn = False
		lbMoreThanOnePhraseIn = False
		lbAllLettersIn = False

		if poMessageAnswerer[psCodeName]['EXISTS']:
			try:
				if poMessageAnswerer[psCodeName]['PHRASE']:
					self.hnnybtprntDbg('Analyze by phrase.')
					lbOnePhraseIn = True
			except KeyError:
				lbOnePhraseIn = False
				pass

			try:
				if poMessageAnswerer[psCodeName]['PHRASESIN']:
					self.hnnybtprntDbg('Analyze by phrases In.')
					lbMoreThanOnePhraseIn = True
			except KeyError:
				lbMoreThanOnePhraseIn = False
				pass

			try:
				if poMessageAnswerer[psCodeName]['ALLLETTERSIN'] and poMessageAnswerer[psCodeName]['MINLENGTH']:
					self.hnnybtprntDbg('Analyze by All Letters In.')
					lbAllLettersIn = True
			except KeyError:
				lbAllLettersIn = False
				pass
				
			liWordMessagesCount = len(laMessages)
			liCharMessageCount = len(psMessage)
			liCharMatchCounter = 0
			liWordMatchCounter = 0
			lbOneFound = False
			if lbOnePhraseIn:
				liWordMatchCounter = 0
				for msgWord in laMessages:
					lbOneFound = False
					for PhraseWord in poMessageAnswerer[psCodeName]['PHRASE']:
						if self.removeSymbols(msgWord.lower())==self.removeSymbols(PhraseWord.lower()):
							liWordMatchCounter = liWordMatchCounter + 1
							hnnybtprnt(self.removeSymbols(msgWord.lower()) + " == " + self.removeSymbols(PhraseWord.lower()))
							lbOneFound = True
							break
						elif self.removeSymbols(msgWord.lower())!=self.removeSymbols(PhraseWord.lower()):
							self.hnnybtprntDbg(self.removeSymbols(msgWord.lower()) + " != " + self.removeSymbols(PhraseWord.lower()))
					if lbOneFound:
						continue
					if not liWordMatchCounter == liWordMessagesCount:
						break
			elif lbMoreThanOnePhraseIn:
				for indice in [0, len(poMessageAnswerer[psCodeName]['PHRASESIN']) - 1]:
					lbIndice = indice
					liWordMatchCounter = 0
					for msgWord in laMessages:
						lbOneFound = False
						for PhraseWord in poMessageAnswerer[psCodeName]['PHRASESIN'][indice]:
							if self.removeSymbols(msgWord.lower())==self.removeSymbols(PhraseWord.lower()):
								liWordMatchCounter = liWordMatchCounter + 1
								hnnybtprnt(self.removeSymbols(msgWord.lower()) + " == " + self.removeSymbols(PhraseWord.lower()))
								lbOneFound = True
								break
							elif self.removeSymbols(msgWord.lower())!=self.removeSymbols(PhraseWord.lower()):
								self.hnnybtprntDbg(self.removeSymbols(msgWord.lower()) + " != " + self.removeSymbols(PhraseWord.lower()))
						self.hnnybtprntDbg(" . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ")
						if lbOneFound:
							continue
						if not liWordMatchCounter == liWordMessagesCount: 
							break
					if liWordMatchCounter == liWordMessagesCount:
						break
			elif lbAllLettersIn:
				self.hnnybtprntDbg("lbAllLettersIn = " + str(lbAllLettersIn))
				self.hnnybtprntDbg("liCharMessageCount = " + str(liCharMessageCount))
				self.hnnybtprntDbg("poMessageAnswerer[psCodeName]['MINLENGTH'] = " + str(poMessageAnswerer[psCodeName]['MINLENGTH']))
				if liCharMessageCount >= poMessageAnswerer[psCodeName]['MINLENGTH']:
					self.hnnybtprntDbg("liCharMessageCount >= poMessageAnswerer[psCodeName][\'MINLENGTH\']: " + str(liCharMessageCount >= poMessageAnswerer[psCodeName]['MINLENGTH']))
					for ALetter in psMessage:
						lbOneFound = False
						for requiredChars in poMessageAnswerer[psCodeName]['ALLLETTERSIN']:
							self.hnnybtprntDbg(requiredChars)
							if self.removeSymbols(ALetter.lower())==self.removeSymbols(str(requiredChars).lower()):
								liCharMatchCounter = liCharMatchCounter + 1
								hnnybtprnt(self.removeSymbols(ALetter.lower()) + " == " + self.removeSymbols(str(requiredChars).lower()))
								lbOneFound = True
								break
							elif self.removeSymbols(ALetter.lower())!=self.removeSymbols(str(requiredChars).lower()):
								self.hnnybtprntDbg(self.removeSymbols(ALetter.lower()) + " != " + self.removeSymbols(str(requiredChars).lower()))
						if lbOneFound:
							continue
						if not liCharMatchCounter == liCharMessageCount:
							break

			if liWordMatchCounter == liWordMessagesCount or liCharMatchCounter == liCharMessageCount:
				hnnybtprnt('It\'s here (' + psCodeName + ', ) let\'s answer him/her!')
			elif not liWordMatchCounter == liWordMessagesCount and not liCharMatchCounter == liCharMessageCount:
				return False
			
			if lbOnePhraseIn:
				for word in poMessageAnswerer[psCodeName]['PHRASE']:
					self.hnnybtprntDbg(word)
			elif lbMoreThanOnePhraseIn:
				for PhraseWord in poMessageAnswerer[psCodeName]['PHRASESIN'][lbIndice]:
					self.hnnybtprntDbg(PhraseWord)

			for word in laMessages:
				hnnybtprnt(word)

			#self.hnnybtprntDbg(lsMessage + " in " + lsWordIn + " ? ??? It seems it's in there! :O")

			lsLNG = poMessageAnswerer[psCodeName]['LNG']

			lsHi = ""
			lsSaludo = ""

			liSaludo = random.randint(0, len(poMessageAnswerer['Attention'][lsLNG]) - 1)

			lbLoopIt = True
			while lbLoopIt:
				try:
					if poMessageAnswerer['Attention'][lsLNG][liSaludo] != None:
						lsHi = poMessageAnswerer['Attention'][lsLNG][liSaludo] + ", "
						break
					self.hnnybtprntDbg("Himsg: \'" + poMessageAnswerer['Attention'][lsLNG][liSaludo] + "\' isn\'t... Lets watch the next, ")
					liSaludo = liSaludo + 1
				except KeyError:
					lbLoopIt = False
					pass
		
			if (poMessageAnswerer[psCodeName]['SAYHI']):
				lsSaludo =  lsHi + str(psSender) + ", "
			else:
				lsSaludo =  " " + str(psSender) + ", "


			lirandAnswer = random.randint(0, len(poMessageAnswerer[psCodeName]['ANSWERS']) - 1)

			if lirandAnswer >= 0:
				randomSleep(poMessageAnswerer[psCodeName]['RNDMSLP'])
				self.irc.send(bytes(PRIV + pWhere +' :' + lsSaludo + poMessageAnswerer[psCodeName]['ANSWERS'][lirandAnswer] + '\r\n', 'utf8')  )
				hnnybtprnt("Answer sent")
				return True
			else:
				hnnybtprnt("Answer not sent")
				return False
		else:
			return False

			

	def ifAnyMsgWordInCodes(self, pWhere, psSender, psMessage, poMessageAnswerer, psCodeName):
		global PRIV
		
		self.hnnybtprntDbg('got here!! Yay!! (ianymwic.)')

		laMessages = psMessage.split(" ")


		if poMessageAnswerer[psCodeName]['EXISTS']:
			liWordMessagesCount = len(laMessages)
			liWordMatchCounter = 0
			for msgWord in laMessages:
				lbOneFound = False
				for WordIn in poMessageAnswerer[psCodeName]['WORDIN']:
					if self.removeSymbols(msgWord.lower())==self.removeSymbols(WordIn.lower()):
						liWordMatchCounter = liWordMatchCounter + 1
						print(self.removeSymbols(msgWord.lower()) + " == " + self.removeSymbols(WordIn.lower()))
						lbOneFound = True
						break
					elif self.removeSymbols(msgWord.lower())!=self.removeSymbols(WordIn.lower()):
						self.hnnybtprntDbg(self.removeSymbols(msgWord.lower()) + " != " + self.removeSymbols(WordIn.lower()))
				if lbOneFound:
					continue
				if liWordMatchCounter == liWordMessagesCount:
					break
			if not liWordMatchCounter == liWordMessagesCount:
				return
			else:
				hnnybtprnt('It\'s here (' + psCodeName + ')')
			
			for word in poMessageAnswerer[psCodeName]['WORDIN']:
				print(word)
			for word in laMessages:
				print(word)

			#hnnybtprnt(lsMessage + " in " + lsWordIn + " ? ??? It seems it's in there! :O")

				
			lsLNG = poMessageAnswerer[psCodeName]['LNG']

			lsHi = ""
			lsSaludo = ""

			liSaludo = random.randint(0, len(poMessageAnswerer['Attention'][lsLNG]) - 1)

			lbLoopIt = True
			while lbLoopIt:
				try:
					if poMessageAnswerer['Attention'][lsLNG][liSaludo] != None:
						lsHi = poMessageAnswerer['Attention'][lsLNG][liSaludo] + ", "
						break
					self.hnnybtprntDbg("Himsg: \'" + poMessageAnswerer['Attention'][lsLNG][liSaludo] + "\' isn\'t... Lets watch the next one, ")
					liSaludo = liSaludo + 1
				except KeyError:
					lbLoopIt = False
					pass
		
			if (poMessageAnswerer[psCodeName]['SAYHI']):
				lsSaludo =  lsHi + str(psSender) + ", "
			else:
				lsSaludo =  " " + str(psSender) + ", "

			try:
				lbrandAnswer = True
				lirandAnswer = random.randint(0, len(poMessageAnswerer[psCodeName]['ANSWERS']) - 1)
			except KeyError:
				lbrandAnswer = False
				pass

			try:
				if not poMessageAnswerer[psCodeName]['ANSWER2'] is None and len(poMessageAnswerer[psCodeName]['ANSWER2']) > 0 and \
						not poMessageAnswerer[psCodeName]['CMND2'] is None and len(poMessageAnswerer[psCodeName]['CMND2']) > 0 and \
						not poMessageAnswerer[psCodeName]['RNDMSLP2'] is None and poMessageAnswerer[psCodeName]['RNDMSLP2'] > 0:
					lbThereIsAnAnswer2 = True

			except KeyError:
				lbThereIsAnAnswer2 = False
				pass

			if lbrandAnswer:
				randomSleep(poMessageAnswerer[psCodeName]['RNDMSLP'])
				self.irc.send(bytes(PRIV + pWhere  +' :' + lsSaludo + poMessageAnswerer[psCodeName]['ANSWERS'][lirandAnswer] + '\r\n', 'utf8')  )
				hnnybtprnt("Answer sent")
			elif lbThereIsAnAnswer2:
				self.irc.send(bytes(poMessageAnswerer[psCodeName]['CMND'] + pWhere  +' :' + lsSaludo + str(psSender) + poMessageAnswerer[psCodeName]['ANSWER'] + ' \r\n', 'utf8'))
				randomSleep(poMessageAnswerer[psCodeName]['RNDMSLP2'])
				self.irc.send(bytes(poMessageAnswerer[psCodeName]['CMND2'] + pWhere + ' ' + str(psSender) + poMessageAnswerer[psCodeName]['ANSWER2'] + ' \r\n','utf8'))
				hnnybtprnt("Answer sent")
			else:
				hnnybtprnt("Answer not sent")


	#.........main func..................................................
	"""
		method: messagechecker
		description: This method contains all the functionality you spect it to have as we have been
		chatting. It still contains all of what you developed by yourself. I made some changes. Ask me
		any doubt you have about it.

		First.- It still has the msgLine interpretation almost like you had it since the begining (I 
		added some global reference to mantain global variable correspondences).

		Second.- I added an "if" to ignore one or two of the first messages recieved from the server
		which aren't bot's business.
		
		Three.- Added the Bot id (BOT_NICKNAME) recognition to identify if the message comes from 'here'
		and you from your computer want to send a message making ppl think the bot is telling that itself.
		
		Four.- The next four sections are your code: address, JOIN/PART, .mail and .web
		
		FIVE.- My JOIN/PART, .mute and .untalk
		
		Six.- Back to nyour code (I added two or Three questions/answers here. Feel free to remove them.)
		
	"""
	def messagechecker(self, msgLine):
		global WUNDERGROUND_KEY
		global PRIV
		global JOIN
		global chjcmd
		global chj2cmd
		global jpycmd
		global WhoseBeingTranslated
		global ANSWER_TO_ANY_OF_THE_SPECIFIED_WORDINS
		global ANSWER_TO_AN_SPECIFIC_PHRASE
		global ANSWER_TO_ANY_OF_THIS_PHRASES


		SecondMessage = "ble ah!".split(" ")[0]
		self.hnnybtprntDbg("msgLine[1:] = " + msgLine[1:])
		completeLine = str(msgLine[1:]).replace("'b",'').split(':') #, 1
		self.hnnybtprntDbg("0= " + completeLine[0])
		self.hnnybtprntDbg("1= " + completeLine[1])
		info = completeLine[0].split()
		message = (completeLine[2].split("\\r")[0]).replace("'b",'') #[1].split(":")[1]
		if len(completeLine) > 3:
			SecondMessage = completeLine[3].split(" ")[0]
		sender = completeLine[1][0:].split("!", 1)[0]
		chatroom = ""
		if any(word in str(completeLine[1][0:]) for word in ["!"]):
			other_info = completeLine[1][0:].split("!", 1)[1].split(' ')
			if any(word in PRIV for word in other_info):
				chatroom = other_info[len(other_info) - 2]
			self.hnnybtprntDbg("Other Info-->" + str(other_info) + "<--\n", 'utf8')
		self.hnnybtprntDbg("Complete Line-->" + str(completeLine) + "<--\n", 'utf8')
		self.hnnybtprntDbg("Info-->" + str(info) + "<--\n", 'utf8')
		hnnybtprnt("Message-->" + str(message) + "<--\n", 'utf8')
		hnnybtprnt("ChatRoom-->" + str(chatroom) + "<--\n", 'utf8')
		hnnybtprnt("Sender-->" + str(sender) + "<--\n", 'utf8')

		where = self.dicParams['BOT_IRC_CHANNEL']
		if chatroom != self.dicParams['BOT_IRC_CHANNEL'] and chatroom != self.dicParams['TRANSLATOR_BOT_CHANNEL']:
			where = chatroom

		if len(str(message))==0:
			hppybtprnt("recieved \':\' instruction from the other side (irc user sent : ). This tells me (to happybot) it\'s an \'empty message\'. The message interpreter thinks every \'word in\' command is true, so it starts sending each and every Answer.")
			return True

		#..............msgs...............................................................................

		if SecondMessage[0] != "Mauritius" or not str(sender[1:]).find("."): #NOTICE
	
			if (str(sender).lower() == str(self.dicParams['BOT_NICKNAME']).lower()) and self.gbEdited:
				self.irc.send(bytes(PRIV + where + ' :' + message + ' !\r\n', 'utf8'))
				hnnybtprnt("Answer sent")
				return True


			#..............msgs...............................................................................
			address=''
			#...........................bot commands...................
			if len(info) >= 2:
				if (str(info[2])!= self.dicParams['BOT_NICKNAME']):
					address=str(info[2])
				elif (str(info[2])== self.dicParams['BOT_NICKNAME']):
					address=str(sender)
			#.......................................................................................
			if any(word in sender for word in self.dicParams['BOT_OWNERS']):
				#hnnybtprnt('owwwwwner')
				if(str(message[0:4])== '.bot'):
					self.hnnybtprntDbg('.bot ok')
					#if(sender == (self.dicParams['BOT_OWNER or self.dicParams['BOT_OWNER2'])):
					bclist= str(message).split(' ')
					self.hnnybtprntDbg('split ok')
		
					if (str(bclist[1]) == 'join'):
						self.hnnybtprntDbg('join ok')
						self.irc.send(bytes(JOIN + str(bclist[2]) + '\r\n','utf8'  )  )
						hnnybtprnt("Answer sent")
		
					if (str(bclist[1]) == 'part'):
						self.irc.send(bytes('PART ' + str(bclist[2]) + ' : leaving . . .\r\n','utf8'  )  )
						hnnybtprnt("Answer sent")
		
					if (str(bclist[1]) == 'lusers'):
						self.irc.send(bytes('LUSERS \r\n','utf8')  )
						self.irc.sendall(bytes(PRIV + address+' '+str(msgLine)+'\r\n','utf8')  )
						hnnybtprnt("Answer sent")
		
					if (str(bclist[1]) == 'quit'):
						self.irc.send(bytes(PRIV + address+' :i have to go !\r\n','utf8')  )
						self.irc.send(bytes("QUIT : see you soon\r\n",'utf8')  )
						hnnybtprnt("Answer sent")

			#..............................mail.....................................................
	
			#.mail myadd youradd sub body pwd smtp smtpport ....separate all by a #
			if len(info) >= 2:
				if(info[2]==self.dicParams['BOT_NICKNAME']):
					mailcount=0
					if(str(message[0:5]).strip() =='.mail'):
						current_mute_setting = self.mute
						self.mute = True
						try:
							emsg=str(message).split('#')
				
				
							hnnybtprnt('1')
							mailcount=mailcount+1
							fromaddr=str(emsg[1])
							mailcount=mailcount+1
							toaddr=str(emsg[2])
							mailcount=mailcount+1
							thesub=str(emsg[3])
							mailcount=mailcount+1
							thebody=str(emsg[4])
							mailcount=mailcount+1
							thepassword=str(emsg[5])
							mailcount=mailcount+1
							domsmtp=str(emsg[6])
							mailcount=mailcount+1
							smtpport=int(emsg[7])
							hnnybtprnt('2')
							mailcount=mailcount+1
							msg = MIMEMultipart('kjhkjhkj')
							hnnybtprnt('3')
							mailcount=mailcount+1
							msg.set_charset('utf8')
							hnnybtprnt('4')
							mailcount=mailcount+1
							msg['From'] = fromaddr
							hnnybtprnt('5')
							mailcount=mailcount+1
							msg['To'] = toaddr
							hnnybtprnt('6')
							mailcount=mailcount+1
							#msg['Subject'] = Header(body.getAttribute('hum').encode('utf8'),'UTF8').encode()
							msg['Subject'] = Header(thesub,'utf8')
							hnnybtprnt('7')
							mailcount=mailcount+1
							_attach = MIMEText(thebody.encode('utf8'),'html','UTF-8')
							hnnybtprnt('8')
							msg.attach(_attach)
							hnnybtprnt('9')
							mailcount=mailcount+1
							server = smtplib.SMTP(domsmtp, smtpport)
							hnnybtprnt('10')
							mailcount=mailcount+1
							server.starttls()
							hnnybtprnt('11')
							mailcount=mailcount+1
							server.login(fromaddr, thepassword)
							hnnybtprnt('12')
							mailcount=mailcount+1
							text = msg.as_string()
							hnnybtprnt('13')
							mailcount=mailcount+1
							server.sendmail(fromaddr, toaddr, text)
							hnnybtprnt('14')
							mailcount=mailcount+1
							server.quit()
							hnnybtprnt('15')
							mailcount=mailcount+1
							self.irc.send(bytes(PRIV + address+' :mail sent, '+str(sender)+' with count : '+str(mailcount)+' !\r\n','utf8')  )
							hnnybtprnt(self.mute)
							hnnybtprnt("Answer sent")

							self.mute = current_mute_setting 
				
						except:
							self.irc.send(bytes(PRIV + address+' :oops mail not sent '+str(sender)+' count : '+str(mailcount)+' !\r\n','utf8')  )
							self.mute = current_mute_setting 
			
			#........................................count letters in webpages...................................................
			if(str(message[0:4])== '.web'):
				#if(str(message[6:13])== 'countlet'):
				cl=message.split(' ')
				webs=cl[2].strip()
				#re.sub(r '.*w','w',webs)
				#g=webs.find('www')
				entry=webs#input('Enter website : ')
				alph=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
				a=-1

				directory = "/tmp"
				if not os.path.exists(directory):
					os.makedirs(directory)
				filem = open(os.path.join(directory,"filea.txt"), 'w')
				try:

					b=urllib.request.urlopen('http://'+entry)#+entry
					vaaa=b.read()#.decode('utf8')

					#self.irc.send(bytes(PRIV + where + ' : ' +str(testwcl)+'\r\n','utf8'  )  )
					#hnnybtprnt(vaaa)
					#hnnybtprnt("Answer sent")
		
					while (a<len(alph)-1):
						a+=1
						wcl1=alph[a]
						wcl2=str(vaaa).count(alph[a])

						filem.write(str(wcl1)+':')
						#hnnybtprnt('...')
						filem.write(str(wcl2)+' ')
						filem.flush()
						#print(alph[a],str(vaaa).count(alph[a]),sep='',end=' ')
			
			
			

				except:
					hnnybtprnt(entry+' not found')
					self.irc.send(bytes(PRIV + address+' : could not get url\r\n','utf8')  )
				filem.close()
				filen = open(os.path.join(directory,"filea.txt"), 'r')
				#time.sleep(2)
				cc=filen.read()
				msg=str(cc)
				#time.sleep(2)
				hnnybtprnt('cc: ' + cc)
				hnnybtprnt('msg: ' + msg)
				if (msg.strip() != ''):
					self.irc.send(bytes(PRIV + address+' : '+msg+'\r\n','utf8')  )
					hnnybtprnt("Answer sent")
	

			#if (str(message) == "quitplz" and sender =='appinventormu'):
	
		
	
	
			#........................................Mo4_xi1_ge1_Ren2's code...................................................

			hnnybtprnt(str("Sender -->" + sender + "<--"), "utf8")
			hnnybtprnt(str("self.dicParams['BOT_OWNERS'] -->" + str(self.dicParams['BOT_OWNERS']).lower() + "<--"), "utf8")
			hnnybtprnt("¿Sender in self.dicParams['BOT_OWNERS']? -->" + str(any(word in sender for word in self.dicParams['BOT_OWNERS'])) + "<--", "utf8")
			#if (str(sender).lower() == str(self.dicParams['BOT_OWNER).lower()):
			if any(word in sender for word in self.dicParams['BOT_OWNERS']):
				if str(message) == "quitplz\r\n" or str(message) == "quitplz" or str(message) == "!quitplz":
					randomSleep(7)
					self.irc.send(bytes("QUIT\r\n", 'utf8')  )
					hnnybtprnt("Answer sent")
					self.quitIRCClient()

				if str(message).lower() == "debug\r\n" or str(message).lower() == "debug" or str(message).lower() == "!debug" or str(message).lower() == ".debug":
					self.DEBUG = not self.DEBUG
					hnnybtprnt("DEBUG is now set to: " + str(self.DEBUG))
					return True


				self.hnnybtprntDbg("-->" + str(message[0:7]) + "<--")
				self.hnnybtprntDbg("-->" + str(message[0:5]) + "<--")
				self.hnnybtprntDbg("-->" + str(message[0:6]) + "<--")
				if str(message[0:8]) == "repeat\r\n" or str(message[0:6]) == "repeat" or str(message[0:7]) == "!repeat" or str(message[0:7]) == ".repeat":
					self.hnnybtprntDbg("got inside!! :D")
					lsMsgToRepeat = ""
					randomSleep(7)
					if str(message[0:8]) == "repeat\r\n":
						lsMsgToRepeat = str(message[9:])
						hnnybtprnt(sender + ": " + str(message[8:]))
						self.hnnybtprntDbg(sender + ": " + message[8:])
					elif str(message[0:6]) == "repeat":
						lsMsgToRepeat = str(message[7:])
						hnnybtprnt(sender + ": " + str(message[6:]))
						self.hnnybtprntDbg(sender + ": " + message[6:])
					elif str(message[0:7]) == "!repeat": 
						lsMsgToRepeat = str(message[8:])
						hnnybtprnt(sender + ": " + str(message[7:]))
						self.hnnybtprntDbg(sender + ": " + message[7:])
					elif str(message[0:7]) == ".repeat":
						lsMsgToRepeat = str(message[8:])
						hnnybtprnt(sender + ": " + str(message[7:]))
						self.hnnybtprntDbg(sender + ": " + message[7:])
					self.irc.send(bytes(PRIV + self.dicParams['BOT_IRC_CHANNEL'] + " :" + str(lsMsgToRepeat) + "\r\n", 'utf8')  )
					hnnybtprnt("Answer sent")
					return True


				if all(word in str(message) for word in chjcmd ):
					randomSleep(4)
					self.irc.send(bytes(JOIN + self.dicParams['BOT_IRC_CHANNEL2'] + '\r\n','utf8'))
					randomSleep(6)
					self.irc.send(bytes('PART ' + self.dicParams['BOT_IRC_CHANNEL'] + '\r\n', 'utf8'))
					self.dicParams['BOT_IRC_CHANNEL'] = self.dicParams['BOT_IRC_CHANNEL2']
					hnnybtprnt(self.dicParams['BOT_IRC_CHANNEL'] + " joined")
					hnnybtprnt("Answer sent")
					return True

				if all(word in str(message) for word in chj2cmd ):
					theIRCClientToClose.irc.send(bytes(PRIV + ldicParams['BOT_IRC_CHANNEL'] + ' :' + "I have to go." + ' !\r\n', 'utf8'))
					randomSleep(6)
					self.irc.send(bytes(JOIN + str(message.split(" ")[1]) + '\r\n', 'utf8'))
					randomSleep(4)
					self.irc.send(bytes('PART ' + self.dicParams['BOT_IRC_CHANNEL'] + '\r\n', 'utf8'))
					self.dicParams['BOT_IRC_CHANNEL'] = str(message.split(" ")[1])
					hnnybtprnt(str(message.split(" ")[1]) + " joined")
					hnnybtprnt("Answer sent")
					return True

				if len(str(message))>1:
					self.hnnybtprntDbg (str(message[0]), 'utf8')
					self.hnnybtprntDbg (str(message[1]), 'utf8')
					randomSleep(3)
					if message[0] == '.' or message[1] == '.' or message[0] == '!' or message[1] == '!':
						hnnybtprnt (str(message[1:]), 'utf8')
						hnnybtprnt (str(message[1:]), 'utf8')
						if str(message[1:]).lower() == "mute" or str(message[1:]).lower() == "shutupplz" or str(message[1:]).lower() == "shutuplz" or str(message[1:]).lower() == "shut up" or str(message[1:]).lower() == "shut up!" or str(message[1:]).lower() == "shutup" or str(message[1:]).lower() == "shut up, please!" or str(message[1:]).lower() == "shutup, plz!":
							self.irc.send(bytes(PRIV + self.dicParams['BOT_IRC_CHANNEL'] + ' :ok, Fine !\r\n', 'utf8'))
							self.mute = True
							hnnybtprnt ("I have been MUTED!!!")
							hnnybtprnt("Answer sent")
							return True

						if str(message[1:]).lower() == "untalk" or str(message[1:]).lower() == "unmute" or str(message[1:]).lower() == "talkplz" or str(message[1:]).lower() == "talk again" or str(message[1:]).lower() == "talk again!" or str(message[1:]).lower() == "talkagain" or str(message[1:]).lower() == "talk, please!" or str(message[1:]).lower() == "talk again, plz!":
							self.irc.send(bytes(PRIV + self.dicParams['BOT_IRC_CHANNEL'] + ' :Ok, Yay !\r\n', 'utf8'))
							self.mute = False
							hnnybtprnt ("I am unmuted now. I can chat now :D !!!")
							hnnybtprnt("Answer sent")
							return True
					self.hnnybtprntDbg ("Not an owner command... lets see if it\'s not muted and if it\'s a common user command or msg: ")			
		
		
			#........................................back to your code...................................................

			if self.mute:
				return True
		
			self.hnnybtprntDbg("len(TRANSLATOR_BOT) = " + str(len(self.dicParams['TRANSLATOR_BOT'])))
			if len(self.dicParams['TRANSLATOR_BOT']) > 0:
				self.hnnybtprntDbg("str(message[0:3] -->" + str(message[0:3]) + "<--")
				if(str(message[0:3]) == '.tr'):
					self.hnnybtprntDbg("len(message.split(' '))==2 = " + str(len(message.split(' '))==2))
					if(len(message.split(' '))==2):
						WhoseBeingTranslated = sender
						ttxt = str(".tr ->es " + message.split(' ')[0])
						self.hnnybtprntDbg("0 -->" + ttxt + "<--")
						ttxt = str(".tr ->es " + message.split(' ')[1])
						self.hnnybtprntDbg("1 -->" + ttxt + "<--")
						randomSleep(7)
						self.irc.send(bytes(PRIV + self.dicParams['TRANSLATOR_BOT'] + " :" + str(ttxt) + " \r\n"  , 'utf8'))
						#self.irc.send(bytes(PRIV + self.dicParams['BOT_OWNERS'][0] + " :" + str(ttxt) + " \r\n"  , 'utf8'))
						self.hnnybtprntDbg("Question sent to Translator")
						return True
				
				self.hnnybtprntDbg("sender == self.dicParams['TRANSLATOR_BOT'] = " + str(sender == self.dicParams['TRANSLATOR_BOT']))
				if (sender == self.dicParams['TRANSLATOR_BOT'] and WhoseBeingTranslated != None): 
					ttr = str(message).split(':')[1]
					self.hnnybtprntDbg("ttr = " + ttr)
					if len(str(ttr)) > 0:
						ttl = str(ttr).split("(")[0]
						self.hnnybtprntDbg("ttl = " + ttl)
						if len(str(ttl)) > 0:
							randomSleep(10)
							self.irc.send(bytes(PRIV + where + ' :Hey, ' + str(WhoseBeingTranslated) + ', what you\'ve just said is really \'' + ttl + '\' around here.\r\n', 'utf8'  )  )
							WhoseBeingTranslated = None
							self.hnnybtprntDbg("Answer sent")
							return True
				
				
			if (sender != self.dicParams['BOT_NICKNAME']): 
				hnnybtprnt ("sender -->" + sender + "<---")

				if (str(message[0:4]) == '.wea'):
						hnnybtprnt("getting weather")
						try:
							hnnybtprnt("getting weather for " + str(message[5:len(message)].strip(), 'utf8'))
							data= message[5:len(message)].strip()
							dsplit = data.split(' ',1)
							if(' ' in str(dsplit[1])):
								stri=dsplit[1]
								strok=stri.replace(' ','_')
								dp2=str(strok)
							else:
								dp2=str(dsplit[1])
							dp1 = str(dsplit[0].strip())
							hnnybtprnt("Getting weather for: " + dp1 + ", " + dp2)
							f=urllib.request.urlopen('http://api.wunderground.com/api/'+WUNDERGROUND_KEY+'/geolookup/conditions/q/'+dp1+'/'+dp2+'.json').read().decode('utf8')
							json_string = f
							parsed_json = json.loads(json_string)
							location = parsed_json['location']['city']
							temp_f = parsed_json['current_observation']['temp_f']
							loca = str(location)
							tampint = float(temp_f)
							convfc1 = tampint - 32
							convfc2 = 0.5556
							convfc3 = math.floor(convfc1 * convfc2)
							tamp =str(convfc3)
							#self.irc.send(bytes(PRIV + where +' '+ "Current temperature in %s is: %s" % (location, temp_f)+ ' \r\n', 'utf8'))
							randomSleep(14)
							self.irc.send(bytes(PRIV + where +" :Current temperature in "+loca+' is '+tamp+ ' C\r\n', 'utf8')  )
							hnnybtprnt("Answer sent")
							f.close()
							return True
						except:
							#hnnybtprnt(dp1)
							#hnnybtprnt(dp2)
							#self.irc.send(bytes(PRIV + where + ' :Hey, ' + str(sender) + ' opps something is bad!\r\n', 'utf8'  )  )
							pass
		
				if(str(message[0:5]) == '.rand'):
					randdata = (message[6:len(message)])
					rdata = randdata.split()
					try:
						inte1 = int(rdata[0])
						inte2 = int(rdata[1])
						randinteg = random.randint(inte1,inte2)
						randst = str(randinteg)
						randomSleep(4)
						self.irc.send(bytes(PRIV + where + ' :Hey, ' + str(sender) +' the random num is ' +randst+' !\r\n', 'utf8'  )  )
						hnnybtprnt("Answer sent")
						return True
					except:
						randomSleep(4)
						self.irc.send(bytes(PRIV + where + ' :Hey, ' + str(sender) +' could not perform the rand operation !\r\n', 'utf8'  )  )
						hnnybtprnt("Answer sent")
						pass
			
				if(str(message[0:4]) == '.sin'):
					sindata = (message[5:len(message)])
					try:
						sdata = math.sin(float(sindata))
						sdatastr = str(sdata)
						randomSleep(4)
						self.irc.send(bytes(PRIV + where + ' :Hey, ' + str(sender) +' the sine of '+sindata+' is ' +sdatastr+' !\r\n','utf8'  )  )
						hnnybtprnt("Answer sent")
						return True
					except:
						randomSleep(4)
						self.irc.send(bytes(PRIV + where + ' :Hey, ' + str(sender) +' could not perform the sine operation !\r\n','utf8'  )  )
						hnnybtprnt("Answer sent")
						return True
						pass
			
				if(str(message[0:4]) == '.cos'):
					cosdata = (message[5:len(message)])
					try:
						cdata = math.cos(float(cosdata))
						cdatastr = str(cdata)
						randomSleep(4)
						self.irc.send(bytes(PRIV + where + ' :Hey, ' + str(sender) +' the cosine of '+cosdata+' is ' +cdatastr+' !\r\n','utf8'  )  )
						hnnybtprnt("Answer sent")
						return True
					except:
						randomSleep(4)
						self.irc.send(bytes(PRIV + where + ' :Hey, ' + str(sender) +' could not perform the cosine operation !\r\n','utf8'  )  )
						hnnybtprnt("Answer sent")
						return True
						pass
			
				if(str(message[0:4]) == '.sqr'):
					sqrdata = (message[5:len(message)])
					try:
						sqdata = math.sqrt(float(sqrdata))
						sqdatastr = str(sqdata)
						randomSleep(4)
						self.irc.send(bytes(PRIV + where + ' :Hey, ' + str(sender) +' the square root of '+sqrdata+' is ' +sqdatastr+' !\r\n','utf8'  )  )
						hnnybtprnt("Answer sent")
						return True
					except:
						randomSleep(4)
						self.irc.send(bytes(PRIV + where + ' :Hey, ' + str(sender) +' could not perform the square root operation !\r\n','utf8'  )  )
						hnnybtprnt("Answer sent")
						return True
						pass


				prhouse1 = " _______________________ "
				prhouse2 = "/                       \\"
				prhouse3 = "-------------------------"
				prhouse4 = " |                     | "
				prhouse5 = " |                     | "
				prhouse6 = " |                     | "
				prhouse7 = " |_____________________| "
				prhousem = '.pr house™'
				if(str(message[0:3]) == '.pr'):
					if(message[4:len(message)] == 'house'):
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prhouse1+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prhouse2+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prhouse3+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prhouse4+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prhouse5+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prhouse6+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prhouse7+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prhousem+'\r\n','utf8'  )  )
						hnnybtprnt("Answer sent")
						return True

				prcar1='   ____________      '
				prcar2='  |            |     '
				prcar3=' __________________  '
				prcar4='|                  \\   '
				prcar5=' --/   \-----/   \---'
				prcar6='    \_/       \_/    '
				prcarm = '.pr car™'
				if(str(message[0:3]) == '.pr'):
					if(message[4:len(message)] == 'car'):
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prcar1+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prcar2+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prcar3+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prcar4+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prcar5+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prcar6+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prcarm+'\r\n','utf8'  )  )
						hnnybtprnt("Answer sent")
						return True

				prchboard1='▒▒▒▒▒▒▒▒▒▒'
				prchboard2='▒▀▄▀▄▀▄▀▄▒'
				prchboard3='▒▀▄▀▄▀▄▀▄▒'
				prchboard4='▒▀▄▀▄▀▄▀▄▒'
				prchboard5='▒▀▄▀▄▀▄▀▄▒'
				prchboard6='▒▒▒▒▒▒▒▒▒▒'
				prchboardm='.pr chequered™'
				if(str(message[0:3]) == '.pr'):
					if(message[4:len(message)] == 'chequered'):
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prchboard1+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prchboard2+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prchboard3+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prchboard4+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prchboard5+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prchboard6+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prchboardm+'\r\n','utf8'  )  )
						hnnybtprnt("Answer sent")
						return True

				prrail1= '║▒▒██▒▒▒██▒▒║'
				prrail2= '║▒█████████▒║'
				prrail3= '║▒▒██▒▒▒██▒▒║'
				prrail4= '║▒█████████▒║'
				prrail5= '║▒▒██▒▒▒██▒▒║'
				prrail6= '║▒█████████▒║'
				prrail7= '║▒▒██▒▒▒██▒▒║'
				prrail8= '║▒█████████▒║'
				prrail9= '║▒▒██▒▒▒██▒▒║'
				prrail10='║▒█████████▒║'
				prrail11='║▒▒██▒▒▒██▒▒║'
				prrail12='║▒█████████▒║'
				prrail13='║▒▒██▒▒▒██▒▒║'
				prrailm= '.pr railway™'
				if(str(message[0:3]) == '.pr'):
					if(message[4:len(message)] == 'railway'):
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prrail1+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prrail2+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prrail3+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prrail4+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prrail5+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prrail6+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prrail7+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prrail8+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prrail9+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prrail10+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prrail11+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prrail12+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prrail13+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prrailm+'\r\n','utf8'  )  )
						hnnybtprnt("Answer sent")
						return True

				prcoffee1= '▒▒▓░▓▒░▓░▒▒▒▒▒▒▒'
				prcoffee2= '▒░▒▓░▓▓░▒░▒▒▒▒▒▒'
				prcoffee3= '▒▒▒▒▓▒▓▒▒▒▒▒▒▒▒▒'
				prcoffee4= '▒█▓▓▓▓▓▓▓▓▓█▒▒▒▒'
				prcoffee5= '▒█▓▓▓▓▓▓▓▓▓████▒'
				prcoffee6= '▒█▓▓▓▓▓▓▓▓▓█▒▒█▒'
				prcoffee7= '▒█▓▓▓▓▓▓▓▓▓█▒▒█▒'
				prcoffee8= '▒█▓▓▓▓▓▓▓▓▓█▒▒█▒'
				prcoffee9= '▒█▓▓▓▓▓▓▓▓▓████▒'
				prcoffee10='▒███████████▒▒▒▒'
				prcoffee11='▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒'
				prcoffeem= '.pr coffee™'
				if(str(message[0:3]) == '.pr'):
					if(message[4:len(message)] == 'coffee'):
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prcoffee1+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prcoffee2+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prcoffee3+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prcoffee4+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prcoffee5+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prcoffee6+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prcoffee7+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prcoffee8+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prcoffee9+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prcoffee10+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prcoffee11+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prcoffeem+'\r\n','utf8'  )  )
						hnnybtprnt("Answer sent")
						return True

				prstop1= ' ╔═════════════════╗'
				prstop2= ' ║            ██████            '
				prstop3= ' ║      ██                 ██'
				prstop4= ' ║██                             ██'
				prstop5= ' ║██    STOP   ██'
				prstop6= ' ║██                             ██'
				prstop7= ' ║      ██                 ██'
				prstop8= ' ║            ██████'
				prstop9= ' ║                  ██                ║'
				prstop10=' ║                  ██                ║'
				prstop11=' ║                  ██                '
				prstop12=' ╚═══════════             ╝'
				prstopm='.pr stop™'
				if(str(message[0:3]) == '.pr'):
					if(message[4:len(message)] == 'stop'):
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prstop1+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prstop2+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prstop3+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prstop4+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prstop5+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prstop6+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prstop7+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prstop8+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prstop9+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prstop10+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prstop11+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prstop12+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prstopm+'\r\n','utf8'  )  )
						hnnybtprnt("Answer sent")
						return True

				prbar1='↑'
				prbar2='|░░|░░|░░|██|░░'
				prbar3='|░░|░░|░░|██|░░'
				prbar4='|░░|░░|░░|██|██'
				prbar5='|░░|██|░░|██|██'
				prbar6='|░░|██|██|██|██'
				prbar7='|██|██|██|██|██'
				prbar8='----------------------->'
				prbarm='.pr barchart™'
				if(str(message[0:3]) == '.pr'):
					if(message[4:len(message)] == 'barchart'):
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prbar1+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prbar2+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prbar3+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prbar4+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prbar5+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prbar6+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prbar7+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prbar8+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prbarm+'\r\n','utf8'  )  )
						hnnybtprnt("Answer sent")
						return True

				prvehicle1='┌──┐'
				prvehicle2='└⊙─⊙┘'
				prvehiclem='.pr vehicle™'
				if(str(message[0:3]) == '.pr'):
					if(message[4:len(message)] == 'vehicle'):
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prvehicle1+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prvehicle2+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prvehiclem+'\r\n','utf8'  )  )
						hnnybtprnt("Answer sent")

				prcake1='░░░░░░♡'
				prcake= '░░▓▓▓▓▓▓▓▓▓'
				prcake2='░████████████'
				prcake3='°°°°°°°°°°°°°°°°°°°°°°°'
				prcakem='.pr cake™'
				if(str(message[0:3]) == '.pr'):
					if(message[4:len(message)] == 'cake'):
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prcake1+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prcake2+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prcake3+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prcakem+'\r\n','utf8'  )  )
						hnnybtprnt("Answer sent")
						return True

				prtank1='  ┏┓━━━━━'
				prtank2='╔╗╔╗╔╗'
				prtank3='▄▄▄▄▄▄▄▄▄▄▄▄→'
				prtank4='_________'
				prtank5='▼⊙▲⊙▲⊙▼'
				prtankm='.pr tank™'
				if(str(message[0:3]) == '.pr'):
					if(message[4:len(message)] == 'tank'):
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prtank1+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prtank2+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prtank3+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prtank4+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prtank5+'\r\n','utf8'  )  )
						ircSendWithRandomSleep(bytes(PRIV  + where + ' : ' +prtankm+'\r\n','utf8'  )  )
						hnnybtprnt("Answer sent")
						return True
				
				self.hnnybtprntDbg('got here!! Yay!! (ifAllMsgWord secuence.)')

				if self.ifAllMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_AN_SPECIFIC_PHRASE, 'hate'): return True
				if self.ifAllMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_AN_SPECIFIC_PHRASE, 'odio'): return True
				if self.ifAllMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_AN_SPECIFIC_PHRASE, 'missya'): return True
				if self.ifAllMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_AN_SPECIFIC_PHRASE, 'wdul'): return True
				if self.ifAllMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_AN_SPECIFIC_PHRASE, 'rufrmmrs'): return True
				if self.ifAllMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_AN_SPECIFIC_PHRASE, 'marciano'): return True
				if self.ifAllMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_AN_SPECIFIC_PHRASE, 'ddonde'): return True
				if self.ifAllMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_AN_SPECIFIC_PHRASE, 'rualive'): return True
				if self.ifAllMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_AN_SPECIFIC_PHRASE, 'hru'): return True
				if self.ifAllMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_AN_SPECIFIC_PHRASE, 'wrudoing'): return True
				if self.ifAllMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_AN_SPECIFIC_PHRASE, 'ruslp'): return True
				if self.ifAllMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_AN_SPECIFIC_PHRASE, 'aslm'): return True
				if self.ifAllMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_AN_SPECIFIC_PHRASE, 'aslamkm'): return True
				if self.ifAllMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_AN_SPECIFIC_PHRASE, 'alhamd'): return True

				if self.ifAllMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_ANY_OF_THIS_PHRASES, 'wisuagain'): return True
				if self.ifAllMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_ANY_OF_THIS_PHRASES, 'ddndrs'): return True
				if self.ifAllMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_ANY_OF_THIS_PHRASES, 'dndvvs'): return True
				if self.ifAllMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_ANY_OF_THIS_PHRASES, 'stsvv'): return True
				if self.ifAllMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_ANY_OF_THIS_PHRASES, 'cmsts'): return True
				if self.ifAllMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_ANY_OF_THIS_PHRASES, 'qstshcnd'): return True
				if self.ifAllMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_ANY_OF_THIS_PHRASES, 'stsdrmd'): return True
				if self.ifAllMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_ANY_OF_THIS_PHRASES, 'bot'): return True
				if self.ifAllMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_ANY_OF_THIS_PHRASES, 'botica'): return True
			

				self.hnnybtprntDbg('got here!! Yay!! (ifAnyMsgWord secuence.)')

				if self.ifAnyMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_ANY_OF_THE_SPECIFIED_WORDINS, 'lovelist'): return True
				if self.ifAnyMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_ANY_OF_THE_SPECIFIED_WORDINS, 'listaamorosa'): return True
				if self.ifAnyMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_ANY_OF_THE_SPECIFIED_WORDINS, 'oi'): return True
				if self.ifAnyMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_ANY_OF_THE_SPECIFIED_WORDINS, 'hi'): return True
				if self.ifAnyMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_ANY_OF_THE_SPECIFIED_WORDINS, 'hola'): return True
				if self.ifAnyMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_ANY_OF_THE_SPECIFIED_WORDINS, 'horse'): return True
				if self.ifAnyMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_ANY_OF_THE_SPECIFIED_WORDINS, 'good'): return True
				if self.ifAnyMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_ANY_OF_THE_SPECIFIED_WORDINS, 'bien'): return True
				if self.ifAnyMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_ANY_OF_THE_SPECIFIED_WORDINS, 'swear'): return True
				if self.ifAnyMsgWordInCodes(where, str(sender), str(message), ANSWER_TO_ANY_OF_THE_SPECIFIED_WORDINS, 'maldice'): return True


		
#......connect................................................................

"""
	method: quitApp
	description: This global method (outside oop) is called when you want to get out of this program 
	closing each and every Window/IRC Connection/etc.
"""
def quitApp():
	global gbRunning
	gbRunning = False
	for liInt in range(0, len(sys.argv)):
		if str(sys.argv[liInt]).lower() == "-fn" or str(sys.argv[liInt]).lower() == "-un" or str(sys.argv[liInt]).lower() == "-in":
			client[liInt].quitIRCClient()
	root.destroy()
	sys.exit(1)

"""
	method: ToCreateCnx
	description: Used To instantiate each and every IRCClient you wanted to open from the begining.
	Note.- Each IRC Network you spect to connect should open a separate Window for it.
"""
def ToCreateCnx(poWindow=None, poParams=None, poTitle=None): #run(self)
	"""
	This is where we handle the asynchronous I/O. For example, it may be
	a 'select()'.
	One important thing to remember is that the thread has to yield
	control.
	"""
	hnnybtprnt("/*starting: " + poParams['BOT_IRC_CHANNEL'] + "  @" + poParams['IRC_NETWORK'] + " */")
	#time.sleep(.4)

	loircClient = IRCClient(master=poWindow, pdicParams=poParams)
	loircClient.master.title(poTitle)
	#tkinter.Label(window, text=self.title).pack()		
	
	#self.ircClient.mainloop()
	hnnybtprnt("/* " + poParams['BOT_IRC_CHANNEL'] + "  @" + poParams['IRC_NETWORK'] + " must have been started by now. */")
	#time.sleep(.4)
	return loircClient

	


root = tkinter.Tk()

hnnybtprnt(str(sys.argv))

client = [None, None, None]

"""
	method: ConnectFreenode
	description: used to call ToCreateCnx to create a connection/window/etc. for the Freenode Network as
	described in FreenodeParams (uphere at the top of this doc.)
"""
def ConnectFreenode():
	global client
	global fnWindow
	if client[1] != None:
		hnnybtprnt('Object already exists!')
		return client[1]
	fnWindow = tkinter.Toplevel()
	return ToCreateCnx(poWindow=fnWindow, poParams=FreenodeParams, poTitle='@Freenode')

"""
	method: ConnectUndernet
	description: used to call ToCreateCnx to create a connection/window/etc. for the Undernet Network as
	described in FreenodeParams (uphere at the top of this doc.)
"""
def ConnectUndernet():
	global client
	global unWindow
	if client[2] != None:
		hnnybtprnt('Object already exists!')
		return client[2]
	unWindow = tkinter.Toplevel()
	return ToCreateCnx(poWindow=unWindow, poParams=UndernetParams, poTitle='@Undernet')

"""
	method: ConnectIRCNET
	description: used to call ToCreateCnx to create a connection/window/etc. for the IRC-NET Network as
	described in FreenodeParams (uphere at the top of this doc.)
"""
def ConnectIRCNET():
	global client
	global inWindow
	if client[3] != None:
		hnnybtprnt('Object already exists!')
		return client[3]
	inWindow = tkinter.Toplevel()
	return ToCreateCnx(poWindow=inWindow, poParams=IRCNetParams, poTitle='@IRC Net')


"""
	Main cycle which starts the process of instantiating each IRCClient from the begining, i mean
	if you told honeybot to open Freenode (-fn) and Undernet (-un) then here it will start each, one by one.
	
	Note.- To start a network you've got to call honeybot like this: 
	
	To open one of this use:

	$python3 honeybot.py -fn #For Freenode
	$python3 honeybot.py -un #For Undernet
	$python3 honeybot.py -in #For IRC-NET
	
	$python3 honeybot.py -fn -un #For Freenode + Undernet (Two Windows are created)

	Note 2.- When you close One of the Network Windows you can reopen it by going to the "Master Window" and
	click on "Re-Connect <Network-Name>"

	Note 3.- To close it all just go there again "Master Window" and click "Close" button.

"""
for liInt in range(0,len(sys.argv)):
	if str(sys.argv[liInt]).lower() == "-fn":
		hnnybtprnt("Opening Freenode Connection...")
		client[1] = ConnectFreenode() #Threader2CreateCnx
	elif str(sys.argv[liInt]).lower() == "-un":
		hnnybtprnt("Opening Undernet Connection...")
		client[2] = ConnectUndernet() #Threader2CreateCnx
	elif str(sys.argv[liInt]).lower() == "-in":
		hnnybtprnt("Opening IRC-NET Connection...")
		client[3] = ConnectIRCNET() #Threader2CreateCnx

for liInt in range(0,len(gbPARAMS)):
	if gbPARAMS[liInt]['IRC_NETWORK'] == "freenode":
		btnopnfn = tkinter.Button( root, text='Open ' + gbPARAMS[liInt]['IRC_NETWORK'], command=ConnectFreenode)
		btnopnfn.grid()
	elif gbPARAMS[liInt]['IRC_NETWORK'] == "undernet":
		btnopnfn = tkinter.Button( root, text='Open ' + gbPARAMS[liInt]['IRC_NETWORK'], command=ConnectUndernet)
		btnopnfn.grid()
	elif gbPARAMS[liInt]['IRC_NETWORK'] == "ircnet":
		btnopnfn = tkinter.Button( root, text='Open ' + gbPARAMS[liInt]['IRC_NETWORK'], command=ConnectIRCNET)
		btnopnfn.grid()

root.title('Master Window')
console = tkinter.Button( root, text='Close', command=quitApp)
console.grid()

root.protocol("WM_DELETE_WINDOW", quitApp)

gbRunning = True
#root.mainloop()
while gbRunning:
	root.update_idletasks()
	root.update()


