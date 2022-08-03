# -*- coding: utf-8 -*-
"""
[mail.py]
Email plugin

[Author]
Tanner Fry

[About]
Will allow the user to send an email while in the chat
with the bot. The text send will be interpreted as html
so you can use formatting such as <br> to make new lines,
and any other html formatting commands in the text of the
body of the email. No additional libraries need to be installed.
Make sure that you configure the email_config.conf file with your
email, your email password, SMTP server, and SMTP server port.
See that document for more information.

[Commands]
.mail <To email address> .body <Text for the body of your email>
 .subject <Text of subject for email>
EX:// ".mail test@email.com .body testing body for honeybot email
 .subject testing subject"

"""
import configparser
import smtplib
from email.mime.text import MIMEText

# open config file for user credentials to email
email_config = configparser.ConfigParser()
email_config.read("settings/email_config.conf")

# save the read values into their respective variables
USER = email_config["Email"]
PASS = email_config["Password"]
HOST = email_config["SMTP Server"]
PORT = email_config["SMTP Server Port"]

# used to tie into the body of what the user sends, if this is not at the
# front of the message then the message will not appear in the email
text = "\n"


class Plugin:
    def __init__(self):
        pass

    # __email will take 6 parameters to setup the email reconnection
    # and send the message.
    def __email(HOST, PORT, USER, PASS, TO, MSG):
        server = smtplib.SMTP(HOST, int(PORT))
        server.connect(HOST, int(PORT))
        server.starttls()
        server.login(USER, PASS)
        server.sendmail(USER, TO, MSG.as_string())
        server.quit()

    # body is used to loop through the msgs list from the chat
    # and grab everything that was said after .body and before
    # .subject.
    def body(BODY_INDEX, SUBJECT_INDEX, msgs):
        i = BODY_INDEX + 1
        while i < SUBJECT_INDEX:
            if i == BODY_INDEX + 1:
                if msgs[i] == "\n":
                    Body = msgs[i]
                BODY = msgs[i] + " "
            elif i == SUBJECT_INDEX - 1:
                BODY = BODY + msgs[i]
            else:
                if msgs[i] == "\n":
                    Body = BODY + msgs[i]
                BODY = BODY + msgs[i] + " "
            i = i + 1
        return BODY

    # subject is used to loop through the msgs list from the chat
    # and grab everythin after .subject and before the end of the
    # message
    def subject(SUBJECT_INDEX, MAX_INDEX, msgs):
        i = SUBJECT_INDEX + 1
        while i < MAX_INDEX:
            if i == SUBJECT_INDEX + 1:
                SUBJECT = msgs[i] + " "
            elif i == MAX_INDEX - 1:
                SUBJECT = SUBJECT + msgs[i]
            else:
                SUBJECT = SUBJECT + msgs[i] + " "
            i = i + 1
        return SUBJECT

    def run(self, incoming, methods, info, bot_info):
        try:
            # if '!~' in info['prefix']:
            # print(info)
            msgs = info["args"][1:][0].split()
            if info["command"] == "PRIVMSG":
                # makes sure the first parameter is ".mail"
                if msgs[0] == ".mail":
                    TO = msgs[1]  # grabs the TO email provided
                    BODY_INDEX = msgs.index(
                        ".body"
                    )  # gets index for ".body", used in body function
                    SUBJECT_INDEX = msgs.index(
                        ".subject"
                    )  # gets index for ".subject" used in body, and subject functions
                    MAX_INDEX = len(msgs)  # gets max index to know the max indexing value

                    BODY = Plugin.body(
                        BODY_INDEX, SUBJECT_INDEX, msgs
                    )  # fill the BODY string using the body function to extraxt the text
                    SUBJECT = Plugin.subject(
                        SUBJECT_INDEX, MAX_INDEX, msgs
                    )  # fill the SUBJECT string using the
                    # subject function to extract the text

                    MSG = MIMEText(
                        text + BODY, "html"
                    )  # sets MSG format to html, and fills in the BODY portion
                    MSG["Subject"] = SUBJECT  # Fills the MSG's subject with SUBJECT
                    MSG["From"] = USER  # Fills the From field with USER string
                    MSG["To"] = TO  # Fills the TO field with the TO string
                    Plugin.__email(
                        HOST, PORT, USER, PASS, TO, MSG
                    )  # Passes paramters needed to __email to be able to
                    # start up connection to SMTP server and send message

        except Exception as e:
            print("\n*error*\nwoops plugin", __file__, e, "\n")
