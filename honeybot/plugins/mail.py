# -*- coding: utf-8 -*-
"""
[mail.py]


[Author: Tanner Fry]


[About]


[Commands]

"""
import smtplib
import string
from email.mime.text import MIMEText

#open config file for user credentials to email
f = open("email_config.conf")
str = f.read()
f.close()

#split the read in words into a list, and pop them into their respective
#variables
test    = str.rsplit()
USER    = test[test.index("Email:")+1]
PASS    = test[test.index("Password:")+1]
HOST    = test[test.index("Server:")+1]
PORT    = test[test.index("Port:")+1]

#used to tie into the body of what the user sends, if this is not at the
#front of the message then the message will not appear in the email
text = "\n"

class Plugin:
    def __init__(self):
        pass

    def __email(HOST, PORT, USER, PASS, TO, MSG):
        server = smtplib.SMTP(HOST, int(PORT))
        server.connect(HOST, int(PORT))
        server.starttls()
        server.login(USER, PASS)
        server.sendmail(USER, TO, MSG.as_string())
        server.quit()

    def body(BODY_INDEX,SUBJECT_INDEX, msgs):
        i = BODY_INDEX+1
        while  i < SUBJECT_INDEX:
            if i == BODY_INDEX + 1:
                if msgs[i] == "\n":
                    Body = msgs[i]
                BODY = msgs[i] +  " "
            elif i == SUBJECT_INDEX - 1:
                BODY = BODY + msgs[i]
            else:
                if msgs[i] == "\n":
                    Body = BODY + msgs[i]
                BODY = BODY + msgs[i] +  " "
            i = i+1
        return (BODY)

    def subject(SUBJECT_INDEX, MAX_INDEX, msgs):
        i = SUBJECT_INDEX + 1
        while  i < MAX_INDEX:
            if i == SUBJECT_INDEX + 1:
                SUBJECT = msgs[i] + " "
            elif i == MAX_INDEX - 1:
                SUBJECT = SUBJECT + msgs[i]
            else:
                SUBJECT = SUBJECT + msgs[i] + " "
            i = i+1
        return (SUBJECT)

    def run(self, incoming, methods, info):
        try:
            # if '!~' in info['prefix']:
                # print(info)
            msgs = info['args'][1:][0].split()
            if info['command'] == 'PRIVMSG':
                if msgs[0] == '.mail':
                    TO              = msgs[1]
                    BODY_INDEX      = msgs.index(".body")
                    SUBJECT_INDEX   = msgs.index(".subject")
                    MAX_INDEX       = len(msgs)

                    BODY            = Plugin.body(BODY_INDEX,SUBJECT_INDEX, msgs)
                    SUBJECT         = Plugin.subject(SUBJECT_INDEX, MAX_INDEX, msgs)

                    MSG             = MIMEText(text + BODY, 'html')
                    MSG["Subject"]  = SUBJECT
                    MSG["From"]     = USER
                    MSG["To"]       = TO
                    Plugin.__email(HOST, PORT, USER, PASS, TO, MSG)

        except Exception as e:
            print('\n*error*\nwoops plugin', __file__, e, '\n')
