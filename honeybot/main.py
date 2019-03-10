
# -*- coding: utf-8 -*-

import configparser
import importlib
import socket

config = configparser.ConfigParser()
config.read('CONNECT.conf')
plugins = []


class Bot_core(object):
    def __init__(self,
                 server_url=config['INFO']['server_url'],
                 port=int(config['INFO']['port']),
                 name=config['INFO']['name'],
                 owners=['appinventorMu', 'appinv'],
                 password='',
                 friends=['haruno', 'keiserr', 'loganaden'],
                 autojoin_channels=['##bottestingmu', '#bottest']
                 ):
        self.server_url = server_url
        self.port = port
        self.name = name
        self.owners = owners
        self.password = password
        self.autojoin_channels = autojoin_channels
        self.friends = friends

        '''
        NORMAL ATTRIBUTES
        '''
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.isListenOn = 1
        dom = self.server_url.split('.')
        self.domain = '.'.join(dom[-2:])
        self.sp_command = 'hbot'
        self.plugins = []

    '''
    STRINGS
    '''
    def set_nick_command(self):
        return 'NICK ' + self.name + '\r\n'

    def present_command(self):
        return 'USER ' + self.name + ' ' + self.name + ' ' +\
        self.name + ' : ' + self.name + ' IRC\r\n'

    def identify_command(self):
        return 'msg NickServ identify ' + self.password + ' \r\n'

    def join_channel_command(self, channel):
        return 'JOIN ' + channel + ' \r\n'

    def specific_send_command(self, target, msg):
        return "PRIVMSG " + target + " :" + msg + "\r\n"

    def pong_return(self):
        return 'PONG \r\n'

    def info(self, s):
        def return_it(x):
            if x is None:
                return ''
            else:
                return x
        try:
            prefix = ''
            trailing = []
            address = ''
            if not s:
                print("Empty line.")
            if s[0] == ':':
                prefix, s = s[1:].split(' ', 1)
            if s.find(' :') != -1:
                s, trailing = s.split(' :', 1)
                args = s.split()
                args.append(trailing)
            else:
                args = s.split()
            command = args.pop(0)
            if '#' in args[0]:
                address = args[0]
            else:
                address = prefix.split('!~')[0]
            # return prefix, command, args, address
            return {
                    'prefix': return_it(prefix),
                    'command': return_it(command),
                    'args': ['' if e is None else e for e in args],
                    'address': return_it(address)
                    }
        except Exception as e:
            print('woops', e)

    '''
    MESSAGE UTIL
    '''
    def send(self, msg):
        self.irc.send(bytes(msg, "UTF-8"))

    def send_target(self, target, msg):
        self.send(self.specific_send_command(target, msg))

    def join(self, channel):
        self.send(self.join_channel_command(channel))

    '''
    BOT UTIL
    '''

    def load_plugins(self, list_to_add):
        try:
            to_load = []
            with open('PLUGINS.conf', 'r') as f:
                to_load = f.read().split('\n')
                to_load = list(filter(lambda x: x != '', to_load))
            for file in to_load:
                module = importlib.import_module('plugins.'+file)
                Plugin = getattr(module, 'Plugin')
                obj = Plugin()
                list_to_add.append(obj)
        except ModuleNotFoundError as e:
            print('module not found', e)

    def methods(self):
        return {
                'send_raw': self.send,
                'send': self.send_target,
                'join': self.join
                }

    def run_plugins(self, listfrom, incoming):
        '''
        incoming is the unparsed string. refer to test.py
        '''
        for plugin in listfrom:
            plugin.run(incoming, self.methods(), self.info(incoming))

    '''
    MESSAGE PARSING
    '''
    def core_commands_parse(self, incoming):

        '''
        PLUGINS
        '''
        self.run_plugins(self.plugins, incoming)

    '''
    BOT IRC FUNCTIONS
    '''
    def connect(self):
            self.irc.connect((self.server_url, self.port))

    def identify(self):
        self.send(self.identify_command())

    def greet(self):
        self.send(self.set_nick_command())
        self.send(self.present_command())
        for channel in self.autojoin_channels:
            self.send(self.join_channel_command(channel))

    def pull(self):
        while self.isListenOn:
            try:
                data = self.irc.recv(2048)
                raw_msg = data.decode("UTF-8")
                msg = raw_msg.strip('\n\r')
                self.stay_alive(msg)
                self.core_commands_parse(msg)
                print(
                """***
{}
                   """.format(msg))
                if len(data) == 0:
                    try:
                        print('<must handle reconnection>')
                    except Exception as e:
                        print(e)
            except Exception as e:
                print(e)

    # all in one for registered bot
    def registered_run(self):
        self.connect()
        self.identify()
        self.greet()
        self.load_plugins(self.plugins)
        self.pull()

    def unregistered_run(self):
        self.connect()
        self.greet()
        self.load_plugins(plugins)
        self.pull()

    '''
    ONGOING REQUIREMENT/S
    '''
    def stay_alive(self, incoming):
        if 'ping' in incoming.lower():
            part = incoming.split(':')
            if self.domain in part[1]:
                self.send(self.pong_return())
                print('''
                      ***** message *****
                      ping detected from
                      {}
                      *******************
                      '''.format(part[1]))
                self.irc.recv(2048).decode("UTF-8")

if __name__ == '__main__':
    x = Bot_core()
    x.registered_run()
