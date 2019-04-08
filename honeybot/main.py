
# -*- coding: utf-8 -*-

import configparser
import importlib
import socket
import sys

connect_config = configparser.ConfigParser()
connect_config.read('settings/CONNECT.conf')
plugins = []


class Bot_core(object):
    def __init__(self, password=''):

        self.server_url = connect_config['INFO']['server_url']
        self.port = int(connect_config['INFO']['port'])
        self.name = connect_config['INFO']['name']
        self.owners = self.configfile_to_list('OWNERS')
        self.password = password
        self.friends = self.configfile_to_list('FRIENDS')

        '''
        NORMAL ATTRIBUTES
        '''
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.isListenOn = 1
        dom = self.server_url.split('.')
        self.domain = '.'.join(dom[-2:])
        self.sp_command = 'hbot'
        self.plugins = []

        self.autojoin_channels = self.configfile_to_list('AUTOJOIN_CHANNELS')

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

    def pong_return(self, domain):
        return 'PONG :{}\r\n'.format(domain)

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
                    'address': return_it(address),
                    'bot_special_command': self.sp_command
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

    def load_plugins(self, plugins_to_load):
        list_to_add = self.plugins
        print("\033[0;36mLoading plugins...\033[0;0m")

        to_load = []
        plugs = 'settings/{}.conf'.format(plugins_to_load)
        with open(plugs) as f:
            to_load = f.read().split('\n')
            to_load = list(filter(lambda x: x != '', to_load))
        for file in to_load:
            try:
                module = importlib.import_module('plugins.'+file)
            except ModuleNotFoundError as e:
                print('module import error, skipped', e, 'in', file)
            obj = module.Plugin
            list_to_add.append(obj)

        self.plugins = list_to_add
        print("\033[0;32mLoaded plugins...\033[0;0m")

    def configfile_to_list(self, filename):
        elements = []
        with open('settings/{}.conf'.format(filename)) as f:
            elements = f.read().split('\n')
            elements = list(filter(lambda x: x != '', elements))
        return elements

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
        #if self.info(incoming)['args'][1][0] == ".":
            #print("\033[0;32mReceived!\033[0;0m")

        for plugin in listfrom:
            #print(f"\033[0;33mTrying {plugin}\033[0;0m")
            plugin.run(self, incoming, self.methods(), self.info(incoming))

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
                        print('<must handle reconnection - len(data)==0>')
                        sys.exit()
                    except Exception as e:
                        print(e)
            except Exception as e:
                print(e)


    # all in one for registered bot
    def registered_run(self):
        self.connect()
        self.identify()
        self.greet()
        self.load_plugins('STD_PLUGINS')
        self.load_plugins('USER_PLUGINS')
        self.pull()

    def unregistered_run(self):
        self.connect()
        self.greet()
        self.load_plugins('STD_PLUGINS')
        self.load_plugins('USER_PLUGINS')
        self.pull()

    '''
    ONGOING REQUIREMENT/S
    '''
    def stay_alive(self, incoming):
        if not incoming:
            print('<must handle reconnection - incoming is not True>')
            sys.exit()
        parts = incoming.split(':')
        if parts[0].strip().lower() == 'ping':
            # if self.domain in parts[1]:
            self.send(self.pong_return(self.domain))
            print('''
                  ***** message *****
                  ping detected from
                  {}
                  *******************
                  '''.format(parts[1]))
            self.send(self.pong_return(parts[1]))
            self.irc.recv(2048).decode("UTF-8")

if __name__ == '__main__':
    x = Bot_core()
    x.unregistered_run()




