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
>>> .send #channel hi all
Checks if user online first and says "User not online."
"""


class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info):
        try:
            print(info)
            msgs = info['args'][1:][0].split()
            if info['command'] == 'PRIVMSG' and msgs[0] == '.send':
                if len(msgs) >= 3:

                    channel_destination = msgs[1]
                    bang = info['prefix'].find('!')
                    sender = info['prefix'][0:bang]
                    sender_channel = '#'+info['address']
                    message = ''

                    if msgs[2][0] != '.':
                        for word in msgs[2:]:
                            message += word
                        complete_message = sender+' from '+sender_channel+' says: '+message
                        methods['send'](channel_destination, complete_message)
                    elif len(msgs) >= 6 and msgs[2] == '.u' and msgs[4] == '.m':
                        user_recipient = msgs[3]
                        for word in msgs[5:]:
                            message += word
                        complete_message = sender+' from '+sender_channel+' says to '+user_recipient+': '+message
                        methods['send'](channel_destination, complete_message)

                else:
                    methods['send'](info['address'], 'Command input error.')
        except Exception as e:
            print('woops plugin error: ', e)


def send(info, message):
    print(message)


def test_them(plugin, msg):

    methods = {"send":send,
               "send_raw":send}
    msg = msg
    info = {'args':[None,msg],
            'command':'PRIVMSG',
            'address':'That place',
            'prefix':'IronPenguin!4b717577@gateway/web/cgi-irc/kiwiirc.com/ip.75.113.117.119'}
    plug.run("",methods,info)


plug = Plugin()

test_them(plug, ".send #start .u IronPenguin .m Aurene Lives")