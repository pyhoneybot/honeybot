#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'me'

#me and david salinas #irc clent / tkinter dev is moxi

import socket
import tkinter
from tkinter import *
import time
import os

import urllib.request
import json

import threading
import random
import multiprocessing
from multiprocessing import Queue
import queue

import math

localtime = time.asctime( time.localtime(time.time()) )
key='put here your code'


BOT_IRC_SERVER ="chat.freenode.net"
BOT_IRC_CHANNEL = "##bottestingmu"
BOT_IRC_PORT = 6667
BOT_NICKNAME = "appinventormuBot"
BOT_OWNER = "appinventormu"
BOT_PASSWORD = ""

BOT_IRC_CHANNEL2 = "#python"

TEXT_HERE = "<TEXTHERE>"

CHANNELN = "##bottestingmu"
CHANNELPY = "##bottestingmu"

gbShuttingUp = False

class GuiPart:
    def __init__(self, master, queue, endCommand):
        self.queue = queue
        # Set up the GUI
        console = tkinter.Button(master, text='Done', command=endCommand)
        console.grid() # console.pack()
        # Add more GUI stuff here

    def processIncoming(self):
        """
        Handle all the messages currently in the queue (if any).
        """
        while self.queue.qsize():
            try:
                msg = self.queue.get(0)
                ## Check contents of message and do what it says
                ## As a test, we simply print it
                print ("Sending Message from queue (" + str(msg) + ") to Message Checker... ")
                messagechecker(str(msg))
            except queue.Empty:
                pass

class Threader(threading.Thread):
	def __init__(self, queue, *args, **kwargs):
		self.queue = queue
		threading.Thread.__init__(self, *args, **kwargs)
		self.daemon = True
		self._stop = threading.Event()
		self.start()

	def run(self):
		while True:
			#print("Look a while true loop that doesn't block the GUI!")
			#print("Current Thread: %s" % self.name)

			"""
			This is where we handle the asynchronous I/O. For example, it may be
			a 'select()'.
			One important thing to remember is that the thread has to yield
			control.
			"""
			print("/*running*/")
			line = irc.recv(4096)
			print(line)
			pingChecker(line)
			if line.find(bytes('PRIVMSG', 'utf8')) != -1 or line.find(bytes('NOTICE', 'utf8')) != -1:
				self.queue.put(str(line))
				print(str(self.queue.qsize()))
			time.sleep(1)

	def stop(self):
		self._stop.set()

	def stopped(self):
		return self._stop.isSet()


class ThreadedClient:
	"""
	Launch the main part of the GUI and the worker thread. periodicCall and
	endApplication could reside in the GUI part, but putting them here
	means that you have all the thread controls in a single place.
	"""
	def __init__(self, master):
		"""
		Start the GUI and the asynchronous threads. We are in the main
		(original) thread of the application, which will later be used by
		the GUI. We spawn a new thread for the worker.
		"""
		self.master = master

		# Create the queue
		self.queue = Queue() #Queue.Queue()

		# Set up the GUI part
		self.gui = GuiPart(master, self.queue, self.endApplication)

		# Set up the thread to do asynchronous I/O
		# More can be made if necessary
		self.running = 1
		self.thread1 = Threader(queue=self.queue) #, target=self.workerThread1

		# Start the periodic call in the GUI to check if the queue contains
		# anything
		print ("Periodic Call about to start")
		self.periodicCall()
		print ("Periodic Call STARTED!!!")

	def periodicCall(self):
		"""
		Check every 100 ms if there is something new in the queue.
		"""
		self.gui.processIncoming()
		"""
		Check If the program is still running: self.running == True
		"""
		if not self.running:
			# This is the brutal stop of the system. You may want to do
			# some cleanup before actually shutting it down.
			print("GOING AWAY!!!")
			self.thread1.stop()
			import sys
			sys.exit(1)
		#else:
		#	print(".")
		self.master.after(100, self.periodicCall)

#	def workerThread1(self):
#		"""
#		This is where we handle the asynchronous I/O. For example, it may be
#		a 'select()'.
#		One important thing to remember is that the thread has to yield
#		control.
#		"""
#		print("-")
#		while self.running:
#			#time.sleep(rand.random() * 0.3)
#			#msg = rand.random()
#			line = irc.recv(4096)
#			print(line)
#			pingChecker(line)
#			if line.find(bytes('PRIVMSG', 'utf8')) != -1 or line.find(bytes('NOTICE', 'utf8')) != -1:
#				#messagechecker(line)
#				self.queue.put(str(line))
#				print(str(self.queue.qsize()))
#			else:
#				print("line.find(bytes('PRIVMSG', 'utf8')) == -1 and line.find(bytes('NOTICE', 'utf8')) == -1")

	def endApplication(self):
		self.running = 0

def pingChecker(pingLine):
    if pingLine.find(bytes('PING'  ,'utf8')) != -1:
        pingLine = pingLine.rstrip().split()
        if pingLine[0] == bytes("PING"  ,'utf8'):
            irc.send(bytes("PONG "  ,'utf8') + pingLine[1] + bytes("\r\n"  ,'utf8')  )
            
#................................................................
            

chjcmd = ['joinpy']

brandf = ['.rand']

jpycmd = 'mmm'

PRIV = 'PRIVMSG '

#.........main func..................................................
def messagechecker(msgLine):
	global gbEdited
	global gbShuttingUp 
	SecondMessage = "ble ah!".split(" ")[0]
	print("msgLine[1:] = " + msgLine[1:])
	completeLine = str(msgLine[1:]).replace("'b",'').split(':') #, 1
	print("0= ", completeLine[0])
	print("1= ", completeLine[1])
	print("2= ", completeLine[2])
	info = completeLine[0].split()
	message = (completeLine[2].split("\\r")[0]).replace("'b",'') #[1].split(":")[1]
	if len(completeLine) > 3:
		SecondMessage = completeLine[3].split(" ")[0]
	sender = completeLine[1][0:].split("!", 1)[0]
	print("Complete Line-->" + str(completeLine))
	print("Info-->" + str(info))
	print("Message-->" + str(message))
	print("Sender-->" + str(sender) + "\n")

#..............msgs...............................................................................

	if SecondMessage[0] != "Mauritius":
		
		if (sender == BOT_NICKNAME) and gbEdited:
			irc.send(bytes(PRIV + BOT_IRC_CHANNEL + ' :' + message + ' !\r\n', 'utf8'))
			return True

		if (sender == BOT_OWNER):
			if str(message) == "quitplz\r\n" or str(message) == "quitplz" or str(message) == "!quitplz":
				irc.send(bytes("QUIT\r\n", 'utf8')  )
				quitIRCClient()

			if str(message) == "shut up\r\n" or str(message) == "shut up!" or str(message) == "shut up" or str(message) == "shut up, please!" or str(message) == "shutup, plz!" or str(message) == "!shutupplz":
				irc.send(bytes(PRIV + BOT_IRC_CHANNEL + ' :ok, Fine !\r\n', 'utf8'))
				gbShuttingUp = True

			if str(message) == "talk again\r\n" or str(message) == "talk again!" or str(message) == "talk again" or str(message) == "talk, please!" or str(message) == "talk again, plz!" or str(message) == "!talkplz":
				irc.send(bytes(PRIV + BOT_IRC_CHANNEL + ' :Ok, Yay !\r\n', 'utf8'))
				gbShuttingUp = False
			
		
		if gbShuttingUp:
			return True
		
		if (sender != BOT_NICKNAME): 
		
			if(str(message)=='hi'):
				irc.send(bytes(PRIV + BOT_IRC_CHANNEL+' :Hi there, '+str(sender)+' !\r\n', 'utf8')  )
		
			if(str(message) =='whereDoYouLive?'):
				irc.send(bytes(PRIV + BOT_IRC_CHANNEL+' :Hi there, '+str(sender)+'i live in my house !\r\n', 'utf8')  )
		
			if ( str(message) == jpycmd):
				irc.send(bytes(PRIV + BOT_IRC_CHANNEL + ' :nnn nnn, ' + str(sender) + '!\r\n', 'utf8'  )  )
		
			swearlist = ['fuck','faggot','fool','sex','buck' ,'shit','dick','ggt','falourmama','liki','zako','pilon','pilnn']
			swearlistr = ' dont swear'
			if any(word in str(message) for word in swearlist):
				irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + ' dont swear!\r\n', 'utf8'  )  )
				irc.send(bytes('KICK ' + BOT_IRC_CHANNEL + ' ' + str(sender) +swearlistr+ ' \r\n','utf8'  )  )
		
			lovelist = ['love','sexy','marry']
			lovelistr = ' love that what they think of'
			if any(word in str(message) for word in lovelist):
				irc.send(bytes(PRIV + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + lovelistr+ ' \r\n', 'utf8'  )  )
		
			horsemanlist = ['sword','shield','horse']
			horsemanlistm  = ' yes a spirit of horsemanship is needed'
			horsemanlistm2 = ' ah the feeling of a horse'
			horsemanlistr=''
			if any(word in str(message) for word in horsemanlist):
				hsrand = random.randint(1,2)
				if(hsrand==1):
					horsemanlistr = horsemanlistm
				if(hsrand==2):
					horsemanlistr = horsemanlistm2
				irc.send(bytes(PRIV + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + ', ' + horsemanlistr + ' \r\n', 'utf8'  )  )
		
			robotlist = ['bot','robotic','artificial intelligence']
			robotlistm  = ' i heard you talking about me and my cousins'
			robotlistm2 = ' seems that me and my cousins interest you'
			robotlistr=''
			if any(word in str(message) for word in robotlist):
				robotrand = random.randint(1,2)
				if(robotrand==1):
					robotlistr = robotlistm
				if(robotrand==2):
					robotlistr = robotlistm2
				irc.send(bytes(PRIV + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + ', ' + robotlistr + ' \r\n', 'utf8'  )  )
		
			hatemsg = ['i','hate','you']
			hatemsgr = ' mind yourself next time!'
			if all(word in str(message) for word in hatemsg):
				irc.send(bytes(PRIV + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + ', ' + hatemsgr+ ' \r\n', 'utf8'  )  )
		
			addrmsg = ['where','do','you','live']
			addrmsgr = ' i live in my house . . .'
			if all(word in str(message) for word in addrmsg):
				irc.send(bytes(PRIV + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + ', ' + addrmsgr+ ' \r\n', 'utf8'  )  )
		
			howhmsg = ['how','are','you']
			howhmsgr = ' fine, and you? . . .'
			if all(word in str(message) for word in howhmsg):
				irc.send(bytes(PRIV + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + ', ' + howhmsgr+ ' \r\n', 'utf8'  )  )
		
			statmsg = ['what','are','you','doing']
			statmsgr = ' oh, i\'m talking to you . . .'
			if all(word in str(message) for word in statmsg):
				irc.send(bytes(PRIV + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + ', ' + statmsgr+ ' \r\n', 'utf8'  )  )
		
			sleepmsg = ['are','you','sleeping']
			sleepmsgr = ' if i\'m responding to you. Then no . . .'
			if all(word in str(message) for word in sleepmsg):
				irc.send(bytes(PRIV + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + ', ' + sleepmsgr+ ' \r\n', 'utf8'  )  )
		
			aslmmsg = ['aslm']
			aslmmsgr = ' wslm'
			if all(word in str(message) for word in aslmmsg):
				irc.send(bytes(PRIV + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + ', ' + aslmmsgr+ ' \r\n', 'utf8'  )  )
		
			aslm2msg = ['as','la','m','k']
			aslm2msgr = ' wa alaikumus salaam'
			if all(word in str(message) for word in aslm2msg):
				irc.send(bytes(PRIV + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + ', ' + aslm2msgr+ ' \r\n', 'utf8'  )  )
		
			okmsg = ['ok','fine']
			okmsgr = ' good '
			if any(word in str(message) for word in okmsg):
				irc.send(bytes(PRIV + BOT_IRC_CHANNEL + ' : ' + okmsgr+ ' \r\n', 'utf8'  )  )
		
			if len(str(message)) < 20:
				alhmsg = ['a','l','ha','m','d']
				alhmsgr = ' yes indeed, praise be to allah (الحَمْد لله) . . .'
				if all(word in str(message) for word in alhmsg):
					irc.send(bytes(PRIV + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + ', ' + alhmsgr+ ' \r\n', 'utf8'  )  )
		
			if(sender == BOT_OWNER):
				if all(word in str(message) for word in chjcmd ):
					irc.send(bytes('JOIN ' + BOT_IRC_CHANNEL2 + '\r\n','utf8'  )  )
		
			if (str(message[0:4]) == '.wea'):
					try:
						data= message[5:len(message)].strip()
						dsplit = data.split(' ',1)
						if(' ' in str(dsplit[1])):
							stri=dsplit[1]
							strok=stri.replace(' ','_')
							dp2=str(strok)
						else:
							dp2=str(dsplit[1])
						dp1 = str(dsplit[0].strip())
						f=urllib.request.urlopen('http://api.wunderground.com/api/'+key+'/geolookup/conditions/q/'+dp1+'/'+dp2+'.json').read().decode('utf8')
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
						#irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL +' '+ "Current temperature in %s is: %s" % (location, temp_f)+ ' \r\n', 'utf8'))
						irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL +" :Current temperature in "+loca+' is '+tamp+ ' C\r\n', 'utf8')  )
						f.close()
					except:
						#print(dp1)
						#print(dp2)
						#irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + ' opps something is bad!\r\n', 'utf8'  )  )
						pass
		
			if(str(message[0:5]) == '.rand'):
				randdata = (message[6:len(message)])
				rdata = randdata.split()
				try:
					inte1 = int(rdata[0])
					inte2 = int(rdata[1])
					randinteg = random.randint(inte1,inte2)
					randst = str(randinteg)
					irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) +' the random num is ' +randst+' !\r\n', 'utf8'  )  )
				except:
					irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) +' could not perform the rand operation !\r\n', 'utf8'  )  )
					pass
			
			if(str(message[0:4]) == '.sin'):
				sindata = (message[5:len(message)])
				try:
					sdata = math.sin(float(sindata))
					sdatastr = str(sdata)
					irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) +' the sine of '+sindata+' is ' +sdatastr+' !\r\n','utf8'  )  )
				except:
					irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) +' could not perform the sine operation !\r\n','utf8'  )  )
					pass
			
			if(str(message[0:4]) == '.cos'):
				cosdata = (message[5:len(message)])
				try:
					cdata = math.cos(float(cosdata))
					cdatastr = str(cdata)
					irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) +' the cosine of '+cosdata+' is ' +cdatastr+' !\r\n','utf8'  )  )
				except:
					irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) +' could not perform the cosine operation !\r\n','utf8'  )  )
					pass
			
			if(str(message[0:4]) == '.sqr'):
				sqrdata = (message[5:len(message)])
				try:
					sqdata = math.sqrt(float(sqrdata))
					sqdatastr = str(sqdata)
					irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) +' the square root of '+sqrdata+' is ' +sqdatastr+' !\r\n','utf8'  )  )
				except:
					irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) +' could not perform the square root operation !\r\n','utf8'  )  )
					pass

		
#......connect................................................................
irc = socket.socket()

irc.connect((BOT_IRC_SERVER, BOT_IRC_PORT))
irc.recv(4096)
irc.send(bytes('NICK ' + BOT_NICKNAME + '\r\n', 'utf8'  )  )
pingChecker(irc.recv(4096))
irc.send(bytes('USER ' + BOT_OWNER + 'Bot ' + BOT_NICKNAME + ' ' + BOT_NICKNAME + ' : ' + BOT_NICKNAME + ' IRC\r\n', 'utf8'  )  )
pingChecker(irc.recv(4096))
irc.send(bytes('msg NickServ identify ' + BOT_PASSWORD + " \r\n"  , 'utf8')  )
pingChecker(irc.recv(4096))
irc.send(bytes('JOIN ' + BOT_IRC_CHANNEL + '\r\n','utf8'  )  )
pingChecker(irc.recv(4096))
irc.send(bytes('NICKSERV  identify ' + BOT_NICKNAME+' '+BOT_PASSWORD+ '\r\n', 'utf8'  )  )

#......file..................................................
directory = "C:\\irc"
if not os.path.exists(directory):
	os.makedirs(directory)
target = open(os.path.join(directory,"file.txt"), 'w')
#/sdcar/folder/file.py for android remove the join etc


def quitIRCClient():
	client.running = 0
	client.periodicCall()
        
rand = random.Random()
root = tkinter.Tk()
app = Frame(root)
app.grid()

client = ThreadedClient(root)

gbEdited = False
TEXT_TO_SEND = "b':" + BOT_NICKNAME  + "!~abcdefg@192.168.1.1 PRIVMSG " + BOT_IRC_CHANNEL + " :" + TEXT_HERE + "\r\n'"


textvariable = None
try:
	textvariable = StringVar()
except KeyError:
	textvariable = None

#if (textvariable is not None):
#	if not ( isinstance( textvariable, tkinter.Variable ) ):
#		raise TypeError("tkinter.Variable type expected, {} given.".format(type(textvariable)))
#	else:
#		print("textvariable IS NOT a tkinter.Variable instance!!! ")
#	textvariable.get = GetText
#	textvariable.set = SetText
#else:
#	print("textvariable is NONE!!!")

#def GetText():
#	text = playTextArea.get( 1.0, tkinter.END )
#	if ( text is not None ):
#		text = text.strip()
#	if ( text == "" ):
#		text = None
#	return text

#def SetText(value ):
#    self.Clear()
#    if ( value is not None ):
#        playTextArea.insert( tkinter.END, value.strip() )

def textChanged(event):
	global gbEdited
	print(event.char)
	gbEdited = True

gsTextToSend = TEXT_TO_SEND

def callMessageChecker():
	global gbEdited
	global gsTextToSend
	if not gbEdited:
		print("It's not allowed to send a message more than once.")
	else:
		print(gsTextToSend) 
		print(TEXT_HERE)
		print(playTextArea.get( 1.0, tkinter.END ))
		gsTextToSend = gsTextToSend.replace(TEXT_HERE, playTextArea.get( 1.0, tkinter.END )) 
		if messagechecker(gsTextToSend):
			gsTextToSend = TEXT_TO_SEND
			gbEdited = False
			playTextArea.insert( tkinter.END, "" )
		else:
			print("Hasn't got back!!")


playTextArea = tkinter.Text(root, bg="white", fg="black", cursor="xterm", height=3, 
						undo=True, maxundo=-1, state=tkinter.NORMAL, width=47, wrap=tkinter.WORD)
playTextArea.grid()
playTextArea.bind("<Key>", textChanged)
playTextArea.bind("<Return>", lambda e: "break")

playTextArea.grid()
stopButton = tkinter.Button(root, text='Enviar', fg="red", command=callMessageChecker )
stopButton.grid()

#playButton.pack(side=TOP)
#stopButton.pack(side=BOTTOM)

root.protocol("WM_DELETE_WINDOW", quitIRCClient)
root.mainloop()



