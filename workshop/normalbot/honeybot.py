

#.################################################################################
#.                                 AUTHORS AND CONTRIBUTORS                      
#. --original basecode / template : 
#. 		jeoreng
#. --person who showed me the template :
#. 		ismed from channel #python of freenode (chat.freenode.net)
#. --kick starter,  the person who worked with me to troubleshoot the template:
#. 		EagleAngelo from channel #bottesting on freenode (chat.freenode.net)
#. --*active development and tkinter (python's in-built gui) support :
#. 		David Salinas / mo4_xi1_gen1_ren2 of #Mandarin on freenode 
#. 		(chat.freenode.net)
#. --bot testing support and founder of ##bottestingmu :
#. 		Yash Paupia / Haruno on freenode (chat.freenode.net)
#. --awesome suggestions:
#.              rus2 of #Mandarin on freenode (chat.freenode.net)
#. --organisation suggestions :
#. 		keiserr
#. --further support:
#. 		loganad1
#. >> disclaimer : if you find anything of poor quality or non-pythonic, don't 
#.    blame any contributor for it. I am fully responsible . . .
#.################################################################################

#.################################################################################
#.                                 RECOMMENDATIONS                               
#. >> sublime text recommended to use as editor as it can hide block of codes.   
#.    enable white spaces : preferences .. settings .. user ..                   
#.    {                                                                          
#.      "draw_white_space" : "all"                                               
#.    }                                                                          
#. >> notepad ++ also not bad
#.################################################################################

#.################################################################################
#.                                      INDEX                                     
#. 0  *imports*
#. 1  *configurations*
#. 2  *life sign / ping checker function*
#. 3  *main function*  
#. 4   ,...address deciding
#. 5   ,...bot owner commands
#.     ,...,...join
#.     ,...,...part
#.     ,...,...quit
#.     ,...,...announce
#. 6   ,...mail
#. 7   ,...counts letters in webpage
#. 8   ,...questions, answers
#. 9   ,...states and feelings
#. 10  ,...weather
#. 11  ,...functional maths commands part sin cos etc
#. 12  ,...graphical part
#. 13 *connection*
#. 14 *log*
#. 15 *message checking*
#. 16 some explanations
#.
#.################################################################################

__author__ = 'Abdur-Rahmaan Janhangeer'

#My first messing-up with python. Code in progress. Here only for checking. use at your own risk (those indents)!
#Honeybot's disparities in code style is because of a trying out of Python
#see the features in the honeybotfeatures.txt 

#.################################################################################
#.                                    imports                                    #
#.################################################################################

from tkinter import*

import re

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

import _thread#unused
import socket
import time
import os

import urllib.request
import json

import random
import math

#from wordpress_xmlrpc import Client, WordPressPost
#from wordpress_xmlrpc.methods import posts # NewPost

#import struct

#import calendar

#.################################################################################
#.                               configurations                                  #
#.################################################################################

#wordpress_lib_installed = True

localtime = time.asctime( time.localtime(time.time()) )
key='65d4b4eabf8b06d5'

global BOT_IRC_CHANNEL

BOT_IRC_SERVER ="chat.freenode.net"
BOT_IRC_CHANNEL = "##bottestingmu"
#BOT_IRC_CHANNEL = "#python"
BOT_IRC_PORT = 6667
BOT_NICKNAME = "appinventormuBot"

BOT_OWNER1 = "appinventormu"
BOT_OWNER2 = "appinv"

BOT_OWNERS =[BOT_OWNER1,BOT_OWNER2]
BOT_PASSWORD = ""

#BOT_IRC_CHANNEL2 = "#python"

CHANNELN = "##bottestingmu"
CHANNELPY = "##bottestingmu"

global PRIV
PRIV = 'PRIVMSG '

#.################################################################################
#.                 *life sign / ping checker function*                           #
#.################################################################################

def pingChecker(pingLine):
    if pingLine.find(bytes('PING'  ,'utf8')) != -1:
        pingLine = pingLine.rstrip().split()
        if pingLine[0] == bytes("PING"  ,'utf8'):
            irc.send(bytes("PONG "  ,'utf8') + pingLine[1] + bytes("\r\n"  ,'utf8')  )
            
#.################################################################################
#.                                 *main func*                                   #
#.################################################################################

def messagechecker(msgLine):
	sendvar=''
	global mute
	mute=False
	completeLine = str(msgLine[1:]).replace("'b",'').split(':', 1)
	info = completeLine[0].split()
	message = (completeLine[1].split("\\r")[0]).replace("'b",'')
	sender = info[0][2:].split("!", 1)[0]
	refinedmsg = str(message.lower())
	refinedmsgl = len(refinedmsg)
	
	print("Complete Line-->" + str(completeLine))
	print("Info-->" + str(info))
	print("Message-->" + str(message))
	print("Sender-->" + str(sender) + "\n")
	

#...################################################################################
#.                             address deciding                                   #
#...################################################################################

	address=''
	if (len(info)>=2):
		if ( str(info[2])!= BOT_NICKNAME ):
			address=str(info[2])
		elif ( str(info[2]) == BOT_NICKNAME):
			address=str(sender)

#...################################################################################
#                               bot commands                                      #
#...################################################################################

	if any(word in str(sender) for word in BOT_OWNERS):
		#print('owwwwwner')
		if(str(message[0:4])== '.bot'):
			#print('.bot ok')
			#if(sender == (BOT_OWNER or BOT_OWNER2)):
			bclist= refinedmsg.split(' ')
			#print('split ok')
			
			if (str(bclist[1]) == 'join'):
				#print('join ok')
				irc.send(bytes('JOIN ' + str(bclist[2]) + '\r\n','utf8'  )  )
			
			if (str(bclist[1]) == 'part'):
				irc.send(bytes('PART ' + str(bclist[2]) + ' : leaving . . .\r\n','utf8'  )  )
			
			if (str(bclist[1]) == 'quit'):
				irc.send(bytes(PRIV + address+' :i have to go !\r\n','utf8')  )
				irc.send(bytes("QUIT : see you soon\r\n",'utf8')  )
#   .bot-announce i am me-##channel
			
			if ( refinedmsg[5:13] =='announce' ) :
				try:
					bclist2 = refinedmsg.split('-')
					print(bclist2)
					annceraw = bclist2[1].split(' ',1)
					print(annceraw)
					lengthlist=[]
					phraselist = annceraw[1].split('.')
					if ( annceraw[0]=='announce' ):
							x=0
							y=-1
							#lengthlist=[]
							while x < len(phraselist):
								x += 1
								y += 1
								lengthlist.append(len(phraselist[y]))
							lengthlist.sort()
							an = 'announcement'
							highestnum = lengthlist[len(lengthlist)-1]
							dec = '*' * highestnum
							paddr = bclist2[2]
							irc.send(bytes(PRIV + paddr + ' :' + dec + '\r\n','utf8'  )  )
							irc.send(bytes(PRIV + paddr + ' :' + an + '\r\n','utf8'  )  )
							irc.send(bytes(PRIV + paddr + ' :' + dec + '\r\n','utf8'  )  )
							a = 0
							b = -1
							while a < len(phraselist): 
								a += 1
								b += 1
								irc.send(bytes(PRIV + paddr + ' :' + phraselist[b]+ '\r\n','utf8'  )  )
							irc.send(bytes(PRIV + paddr + ' :' + dec  + '\r\n','utf8'  )  )
				except:
					irc.send(bytes(PRIV + address + ' : could not announce\r\n','utf8'  )  )


#...################################################################################
#.                                    mail                                       #
#...################################################################################

	
	#  .mail myadd youradd sub body pwd smtp smtpport ....separate all by a #
	if (len(info)>=2):
		if(info[2]==BOT_NICKNAME ):
			mailcount=0
			if(str(message[0:5]).strip() =='.mail'):
				mute = True
				try:
					emsg=refinedmsg.split('#')
					
					
					print('1')
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
					print('2')
					mailcount=mailcount+1
					msg = MIMEMultipart('kjhkjhkj')
					print('3')
					mailcount=mailcount+1
					msg.set_charset('utf8')
					print('4')
					mailcount=mailcount+1
					msg['From'] = fromaddr
					print('5')
					mailcount=mailcount+1
					msg['To'] = toaddr
					print('6')
					mailcount=mailcount+1
					#msg['Subject'] = Header(body.getAttribute('hum').encode('utf8'),'UTF8').encode()
					msg['Subject'] = Header(thesub,'utf8')
					print('7')
					mailcount=mailcount+1
					_attach = MIMEText(thebody.encode('utf8'),'html','UTF-8')
					print('8')
					msg.attach(_attach)
					print('9')
					mailcount=mailcount+1
					server = smtplib.SMTP(domsmtp, smtpport)
					print('10')
					mailcount=mailcount+1
					server.starttls()
					print('11')
					mailcount=mailcount+1
					server.login(fromaddr, thepassword)
					print('12')
					mailcount=mailcount+1
					text = msg.as_string()
					print('13')
					mailcount=mailcount+1
					server.sendmail(fromaddr, toaddr, text)
					print('14')
					mailcount=mailcount+1
					server.quit()
					print('15')
					mailcount=mailcount+1
					irc.send(bytes(PRIV + address+' :mail sent, '+str(sender)+' with count : '+str(mailcount)+' !\r\n','utf8')  )
					print(mute)
					
					
				except:
					irc.send(bytes(PRIV + address+' :oops mail not sent '+str(sender)+' count : '+str(mailcount)+' !\r\n','utf8')  )

#...################################################################################
#.                       counts letters in webpage                               #
#...################################################################################

	if(str(message[0:4])== '.web'):
		#if(str(message[6:13])== 'countlet'):
		cl=message.split(' ')
		webs=cl[2].strip()
		#re.sub(r '.*w','w',webs)
		#g=webs.find('www')
		entry=webs#input('Enter website : ')
		alph=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
		a=-1

		directory = "C:\\irc"
		if not os.path.exists(directory):
			os.makedirs(directory)
		filem = open(os.path.join(directory,"filea.txt"), 'w')
		try:

			b=urllib.request.urlopen('http://'+entry)#+entry
			vaaa=b.read()#.decode('utf8')

			#irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +str(testwcl)+'\r\n','utf8'  )  )
			#print(vaaa)
			
			while (a<len(alph)-1):
				a+=1
				wcl1=alph[a]
				wcl2=str(vaaa).count(alph[a])

				filem.write(str(wcl1)+':')
				#print('...')
				filem.write(str(wcl2)+' ')
				filem.flush()
				#print(alph[a],str(vaaa).count(alph[a]),sep='',end=' ')
				
				
				

		except:
			print(entry+' not found')
			irc.send(bytes(PRIV + address+' : could not get url\r\n','utf8')  )
		filem.close()
		filen = open(os.path.join(directory,"filea.txt"), 'r')
		#time.sleep(2)
		cc=filen.read()
		msg=str(cc)
		#time.sleep(2)
		print('cc:',cc)
		print('msg:',msg)
		if (msg.strip() != ''):
			irc.send(bytes(PRIV + address+' : '+msg+'\r\n','utf8')  )

#...################################################################################
#.                               questions, answers                              #
#...##############################################################################

	himsg = ['hi','bot']
	himsgr = ' peace be unto you ... '
	if all(word in refinedmsg for word in himsg):
		irc.send(bytes(PRIV + address + ' :Hey, ' + str(sender) + himsgr+ ' \r\n','utf8'  )  )

	
	swearlist = []
	swearlist2 = []
	swearlists= swearlist + swearlist2
	swearlistr = ' dont swear'
	if any(word in refinedmsg for word in swearlists):
		irc.send(bytes('PRIVMSG ' + address + ' :Hey, ' + str(sender) + ' dont swear!\r\n','utf8'  )  )
		time.sleep(2)
		irc.send(bytes('KICK ' + address + ' ' + str(sender) +swearlistr+ ' \r\n','utf8'  )  )
	
	hatemsg = ['i','hate','you']
	hatemsgr = ' mind yourself next time!'
	if all(word in refinedmsg for word in hatemsg ):
		irc.send(bytes(PRIV + address + ' :Hey, ' + str(sender) + hatemsgr+ ' \r\n','utf8'  )  )
	
	addrmsg = ['where','do','you','live','bot']
	addrmsgr = ' i live in my house . . .'
	if all(word in refinedmsg for word in addrmsg):
		irc.send(bytes(PRIV + address + ' :Hey, ' + str(sender) + addrmsgr+ ' \r\n','utf8'  )  )
	
	howhmsg = ['how','are','you','bot']
	howhmsgr = ' fine and you? . . .'
	if all(word in refinedmsg for word in howhmsg):
		irc.send(bytes(PRIV + address + ' :Hey, ' + str(sender) + howhmsgr+ ' \r\n','utf8'  )  )
	
	statmsg = ['what','are','you','doing','bot']
	statmsgr = ' oh i\'m talking to you . . .'
	if all(word in refinedmsg for word in statmsg):
		irc.send(bytes(PRIV + address + ' :Hey, ' + str(sender) + statmsgr+ ' \r\n','utf8'  )  )
	
	sleepmsg = ['are','you','sleeping','bot']
	sleepmsgr = ' if i\'m responding to you. no . . .'
	if all(word in refinedmsg for word in sleepmsg):
		irc.send(bytes(PRIV + address + ' :Hey, ' + str(sender) + sleepmsgr+ ' \r\n','utf8'  )  )
	
	aslmmsg = ['aslm','bot']
	aslmmsgr = ' wslm'
	if all(word in refinedmsg for word in aslmmsg):
		irc.send(bytes(PRIV + address + ' :Hey, ' + str(sender) + aslmmsgr+ ' \r\n','utf8'  )  )
	
	aslm2msg = ['assala','bot']
	aslm2msgr = ' wa alaikumus salaam'
	if all(word in refinedmsg for word in aslm2msg):
		irc.send(bytes(PRIV + address + ' :Hey, ' + str(sender) + aslm2msgr+ ' \r\n','utf8'  )  )
	
	okmsg = ['ok','fine','bot']
	okmsgr = ' good '
	if all(word in refinedmsg for word in okmsg):
		irc.send(bytes(PRIV + address + ' : ' + okmsgr+ ' \r\n','utf8'  )  )
	
	alhmsg = ['alhamdulillah']
	alhmsgr = ' yes indeed praise be to allah . . . الحمد لله '
	if all(word in refinedmsg for word in alhmsg):
		irc.send(bytes(PRIV + address + ' :Hey, ' + str(sender) + alhmsgr+ ' \r\n','utf8'  )  )

#...################################################################################
#.                          states and feelings                                  #
#...################################################################################

	lovelist = ['love','sexy','marry','woman']
	lovelistr = ' feels that he is hearing love too often'
	if any(word in refinedmsg for word in lovelist):
		irc.send(bytes(PRIV+' '+address+' :\x01ACTION '+lovelistr+'\x01\r\n','utf8')  )
	
	horsemanlist = ['sword','shield','horse']
	horsemanlistm  = ' salutes the spirit of horsemanship'
	horsemanlistm2 = ' is longing to be a horseman'
	horsemanlistr=''
	if any(word in refinedmsg for word in horsemanlist):
		hsrand = random.randint(1,2)
		if(hsrand==1):
			horsemanlistr = horsemanlistm
		if(hsrand==2):
			horsemanlistr = horsemanlistm2
		irc.send(bytes(PRIV+' '+address+' :\x01ACTION '+horsemanlistr+'\x01\r\n','utf8')  )

#...################################################################################
#.                                  weather                                      #
#...################################################################################

	
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
			#irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL +' '+ "Current temperature in %s is: %s" % (location, temp_f)+ ' \r\n','utf8'))
			irc.send(bytes('PRIVMSG ' + address +" :Current temperature in "+loca+' is '+tamp+ ' C\r\n','utf8')  )
			f.close()
		except:
			#print(dp1)
			#print(dp2)
			#irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + ' unable to fetch weather!\r\n','utf8'  )  )
			pass

#...################################################################################
#.                               wordpress posts                                  #
#...################################################################################


#...################################################################################
#.                functional maths commands part sin cos etc                     #
#...################################################################################

	if(str(message[0:5]) == '.rand'):
		randdata = (message[6:len(message)])
		rdata = randdata.split()
		try:
			inte1 = int(rdata[0])
			inte2 = int(rdata[1])
			randinteg = random.randint(inte1,inte2)
			randst = str(randinteg)
			irc.send(bytes('PRIVMSG ' + address + ' :Hey, ' + str(sender) +' the random num is ' +randst+' !\r\n','utf8'  )  )
		except:
			irc.send(bytes('PRIVMSG ' + address + ' :Hey, ' + str(sender) +' could not perform the rand operation !\r\n','utf8'  )  )
			pass
			
	if(str(message[0:4]) == '.sin'):
		sindata = (message[5:len(message)])
		try:
			sdata = math.sin(float(sindata))
			sdatastr = str(sdata)
			irc.send(bytes('PRIVMSG ' + address + ' :Hey, ' + str(sender) +' the sine of '+sindata+' is ' +sdatastr+' !\r\n','utf8'  )  )
		except:
			irc.send(bytes('PRIVMSG ' + address + ' :Hey, ' + str(sender) +' could not perform the sine operation !\r\n','utf8'  )  )
			pass
			
	if(str(message[0:4]) == '.cos'):
		cosdata = (message[5:len(message)])
		try:
			cdata = math.cos(float(cosdata))
			cdatastr = str(cdata)
			irc.send(bytes('PRIVMSG ' + address + ' :Hey, ' + str(sender) +' the cosine of '+cosdata+' is ' +cdatastr+' !\r\n','utf8'  )  )
		except:
			irc.send(bytes('PRIVMSG ' + address + ' :Hey, ' + str(sender) +' could not perform the cosine operation !\r\n','utf8'  )  )
			pass
			
	if(str(message[0:4]) == '.sqr'):
		sqrdata = (message[5:len(message)])
		try:
			sqdata = math.sqrt(float(sqrdata))
			sqdatastr = str(sqdata)
			irc.send(bytes('PRIVMSG ' + address + ' :Hey, ' + str(sender) +' the square root of '+sqrdata+' is ' +sqdatastr+' !\r\n','utf8'  )  )
		except:
			irc.send(bytes('PRIVMSG ' + address + ' :Hey, ' + str(sender) +' could not perform the square root operation !\r\n','utf8'  )  )
			pass
	
	if (refinedmsg[0:6] == '.table'):
		try:
			tabllist = refinedmsg.split()
			table=int( tabllist[1] )
			upto=int ( tabllist[2] )
			if (table < 10000 and upto < 10000):
				i1 = 0
				i2 = 0
				directory = "C:\\irc"
				if not os.path.exists(directory):
					os.makedirs(directory)
				filem = open(os.path.join(directory,"filetab.txt"), 'w')
				while i1 < upto :
					i1 += 1
					i2 += 1
					data = 1 * table * i1
					#sdata ='for {} : {} '.format(i2,data)
					filem.write(str(i2)+'>'+str(data)+' ')
					filem.flush()

					#irc.send(bytes('PRIVMSG ' + address + ' :  ' +sdata+' \r\n','utf8'  )  )
				filem.close()
				filen=open(os.path.join(directory,"filetab.txt"), 'r')
				cc=filen.read(8192)
				dd=filen.read(8192)
				msg=str(cc+dd)
				irc.send(bytes('PRIVMSG ' + address + ' : '+msg+ '\r\n','utf8'  )  )
		except:
			irc.send(bytes('PRIVMSG ' + address + ' : could not get table\r\n','utf8'  )  )


#...################################################################################
#.                                graphical part                                 #
#...################################################################################


	
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
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prhouse1+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prhouse2+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prhouse3+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prhouse4+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prhouse5+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prhouse6+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prhouse7+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prhousem+'\r\n','utf8'  )  )
			
	prcar1='   ____________      '
	prcar2='  |            |     '
	prcar3=' __________________  '
	prcar4='|                  \\   '
	prcar5=' --/   \-----/   \---'
	prcar6='    \_/       \_/    '
	prcarm = '.pr car™'
	if(str(message[0:3]) == '.pr'):
		if(message[4:len(message)] == 'car'):
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prcar1+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prcar2+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prcar3+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prcar4+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prcar5+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prcar6+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prcarm+'\r\n','utf8'  )  )

		if(message[4:len(message)] == 'chequered'):
			prchboard1='▒▒▒▒▒▒▒▒▒▒'
			prchboard2='▒▀▄▀▄▀▄▀▄▒'
			prchboard3='▒▀▄▀▄▀▄▀▄▒'
			prchboard4='▒▀▄▀▄▀▄▀▄▒'
			prchboard5='▒▀▄▀▄▀▄▀▄▒'
			prchboard6='▒▒▒▒▒▒▒▒▒▒'
			prchboardm='.pr chequered™'
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prchboard1+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prchboard2+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prchboard3+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prchboard4+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prchboard5+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prchboard6+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prchboardm+'\r\n','utf8'  )  )
		
		if(message[4:len(message)] == 'railway'):
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
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prrail1+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prrail2+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prrail3+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prrail4+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prrail5+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prrail6+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prrail7+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prrail8+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prrail9+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prrail10+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prrail11+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prrail12+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prrail13+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prrailm+'\r\n','utf8'  )  )
		
		if(message[4:len(message)] == 'coffee'):
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
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prcoffee1+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prcoffee2+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prcoffee3+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prcoffee4+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prcoffee5+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prcoffee6+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prcoffee7+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prcoffee8+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prcoffee9+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prcoffee10+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prcoffee11+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prcoffeem+'\r\n','utf8'  )  )
		
		if(message[4:len(message)] == 'stop'):
			prstop1= ' ╔═════════════════╗'
			prstop2= ' ║            ██████            '
			prstop3= ' ║      ██                 ██'
			prstop4= ' ║██                       ██'
			prstop5= ' ║██    STOP   ██'
			prstop6= ' ║██                       ██'
			prstop7= ' ║      ██                 ██'
			prstop8= ' ║            ██████'
			prstop9= ' ║                ██                ║'
			prstop10=' ║                ██                ║'
			prstop11=' ║                ██                '
			prstop12=' ╚═══════════             ╝'
			prstopm='.pr stop™'
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prstop1+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prstop2+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prstop3+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prstop4+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prstop5+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prstop6+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prstop7+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prstop8+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prstop9+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prstop10+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prstop11+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prstop12+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prstopm+'\r\n','utf8'  )  )
			
		if(message[4:len(message)] == 'barchart'):
			prbar1='↑'
			prbar2='|░░|░░|░░|██|░░'
			prbar3='|░░|░░|░░|██|░░'
			prbar4='|░░|░░|░░|██|██'
			prbar5='|░░|██|░░|██|██'
			prbar6='|░░|██|██|██|██'
			prbar7='|██|██|██|██|██'
			prbar8='----------------------->'
			prbarm='.pr barchart™'
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prbar1+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prbar2+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prbar3+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prbar4+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prbar5+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prbar6+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prbar7+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prbar8+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prbarm+'\r\n','utf8'  )  )
		
		if(message[4:len(message)] == 'vehicle'):
			prvehicle1='┌──┐'
			prvehicle2='└⊙─⊙┘'
			prvehiclem='.pr vehicle™'
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prvehicle1+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prvehicle2+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prvehiclem+'\r\n','utf8'  )  )
			
		if(message[4:len(message)] == 'cake'):
			prcake1='░░░░░░♡'
			prcake= '░░▓▓▓▓▓▓▓▓▓'
			prcake2='░████████████'
			prcake3='°°°°°°°°°°°°°°°°°°°°°°°'
			prcakem='.pr cake™'
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prcake1+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prcake2+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prcake3+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prcakem+'\r\n','utf8'  )  )
			
		if(message[4:len(message)] == 'tank'):
			prtank1='  ┏┓━━━━━'
			prtank2='╔╗╔╗╔╗'
			prtank3='▄▄▄▄▄▄▄▄▄▄▄▄→'
			prtank4='_________'
			prtank5='▼⊙▲⊙▲⊙▼'
			prtankm='.pr tank™'
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prtank1+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prtank2+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prtank3+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prtank4+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prtank5+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + address + ' : ' +prtankm+'\r\n','utf8'  )  )
			

#.################################################################################
#.                            *connection*                                       #
#.################################################################################

global irc
irc = socket.socket()

irc.connect((BOT_IRC_SERVER, BOT_IRC_PORT))
irc.recv(4096)
irc.send(bytes('NICK ' + BOT_NICKNAME + '\r\n','utf8'  )  )
pingChecker(irc.recv(4096))
irc.send(bytes('USER appinventormuBot appinventormuBot appinventormuBot : appinventormuBot IRC\r\n','utf8'  )  )
pingChecker(irc.recv(4096))
irc.send(bytes('msg NickServ identify ' + BOT_PASSWORD + " \r\n"  ,'utf8')  )
pingChecker(irc.recv(4096))
irc.send(bytes('NICKSERV  identify ' + BOT_NICKNAME+' '+BOT_PASSWORD+ '\r\n','utf8'  )  )
pingChecker(irc.recv(4096))
time.sleep(3)
irc.send(bytes('JOIN ' + BOT_IRC_CHANNEL + '\r\n','utf8'  )  )



#.################################################################################
#.                                  *log*                                        #
#.################################################################################

directory = "C:\\irc"
if not os.path.exists(directory):
	os.makedirs(directory)
target = open(os.path.join(directory,"file.txt"), 'w')
#/sdcar/folder/file.py for android remove the join etc

#.################################################################################
#.                         *message checking loop*                               #
#.################################################################################

while 1:
	pass
	line = irc.recv(4096)
	print(line)
	pingChecker(line)
	if line.find(bytes('PRIVMSG' ,'utf8')) != -1 or line.find(bytes('NOTICE'  ,'utf8')) != -1 :
		messagechecker(line)
		target.write(str(line))
		target.flush()

#.################################################################################
#.                              some explanations                                #
#.################################################################################

#.find -1 means no find
#.rstrip() removes all chars at the end
#.rstr('x') removes all x at end
#.split() splits at white space 
#.split(' ',1) 1 splits at first occurance of ' '
#.count(thing) returns how many times thing occurs in list
