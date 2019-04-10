# -*- coding: utf-8 -*-
"""
[greet.py]
Greet Plugin

[Author]
Abdur-Rahmaan Janhangeer, pythonmembers.club

[About]
responds to .hi, demo of a basic plugin

[Commands]
>>> .send #channel .u riceabove .m how are you?
Sends a message to #channel like
'IronPenguin from #channel says to riceabove: how are you?'

>>> .send #channel hi all
Sends a message to #channel like
'IronPenguin from #channel says: hi all'

Checks if user online first and says "User not online."
"""


class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info):
        try:
            msgs = info['args'][1:][0].split()
            if info['command'] == 'PRIVMSG' and msgs[0] == '.send':
                if len(msgs) >= 3:
                    bang = info['prefix'].find('!')
                    message = ''

                    channel_destination = msgs[1]
                    sender = info['prefix'][0:bang]
                    sender_channel = '#'+info['address']

                    if msgs[2][0] != '.':
                        for word in msgs[2:]:
                            message += word + ' '
                        complete_message = ('{0} from {1} says: '
                                            .format(sender,sender_channel,
                                            message.rstrip()))

                    elif (len(msgs) >= 6 and 
                          msgs[2] == '.u' and
                          msgs[4] == '.m'):
                        user_recipient = msgs[3]
                        for word in msgs[5:]:
                            message += word + ' '
                        complete_message = ('{0} from {1} says to {2}: {3}'
                                           .format(sender,sender_channel,
                                           user_recipient,message.rstrip()))
                    
                    methods['send'](channel_destination, complete_message)
                else:
                    methods['send'](info['address'], 'Command input error.')
        except Exception as e:
            print('woops plugin error: ', e)