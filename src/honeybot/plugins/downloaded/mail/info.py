
NAME = 'mail.py'
ORIGINAL_AUTHORS = [
    'Tanner Fry'
]

ABOUT = '''
Will allow the user to send an email while in the chat
with the bot. The text send will be interpreted as html
so you can use formatting such as <br> to make new lines,
and any other html formatting commands in the text of the
body of the email. No additional libraries need to be installed.
Make sure that you configure the email_config.conf file with your
email, your email password, SMTP server, and SMTP server port.
See that document for more information.
'''

COMMANDS = '''
.mail <To email address> .body <Text for the body of your email>
 .subject <Text of subject for email>
EX:// ".mail test@email.com .body testing body for honeybot email
 .subject testing subject"
'''

WEBSITE = ''
