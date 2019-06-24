# -*- coding: utf-8 -*-

import configparser
import importlib
import logging
import socket
import sys
import time

connect_config = configparser.ConfigParser()
connect_config.read('settings/CONNECT.conf')

memory_reader = configparser.ConfigParser()

plugins = []

# Start logger
logger = logging.getLogger('bot_core')

'''
BOT CONNECTION SETUP
'''


class Bot_core(object):
    def __init__(self, password=''):

        self.server_url = connect_config['INFO']['server_url']
        self.port = int(connect_config['INFO']['port'])
        self.name = connect_config['INFO']['name']
        self.owners = self.configfile_to_list('OWNERS')
        self.password = password
        self.friends = self.configfile_to_list('FRIENDS')
        self.autojoin_channels = self.configfile_to_list('AUTOJOIN_CHANNELS')
        self.required_modules = self.requirements()
        self.time = time.time()

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
        return 'USER ' + self.name + ' ' + self.name + ' ' + \
               self.name + ' : ' + self.name + ' IRC\r\n'

    def identify_command(self):
        return 'msg NickServ identify ' + self.password + ' \r\n'

    def join_channel_command(self, channel):
        return 'JOIN ' + channel + ' \r\n'

    def specific_send_command(self, target, msg):
        return "PRIVMSG " + target + " :" + msg + "\r\n"

    def pong_return(self, domain):
        return 'PONG :{}\r\n'.format(domain)

    '''
    MESSAGE VALIDATION
    '''

    def message_info(self, s):
        def prevent_none(x):
            if x is None:
                return ''
            else:
                return x

        try:
            prefix = ''
            trailing = []
            address = ''
            if not s:
                pass
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
            user = prefix.split('!')[0]
            # return prefix, command, args, address
            return {
                'prefix': prevent_none(prefix),
                'command': prevent_none(command),
                'args': ['' if e is None else e for e in args],
                'address': prevent_none(address),
                'user': prevent_none(user)
            }
        except Exception as e:
            logger.error(e)

    def bot_info(self):
        return {
            'name': self.name,
            'special_command': self.sp_command,
            'required_modules': self.required_modules,
            'owners': self.owners,
            'time': self.time,
            'friends': self.friends
        }

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
        logger.info('Loading plugins...')

        to_load = []
        plugs = 'settings/{}.conf'.format(plugins_to_load)
        with open(plugs) as f:
            to_load = f.read().split('\n')
            to_load = list(filter(lambda x: x != '', to_load))
        for file in to_load:
            try:
                module = importlib.import_module('plugins.' + file)
            except ModuleNotFoundError as e:
                logger.warning(f"module import error, skipped' {e} in {file}")
            obj = module.Plugin
            list_to_add.append(obj)

        self.plugins = list_to_add
        logger.info('Loaded plugins...')

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
            'join': self.join,
            'mem_add': self.memory_add_value,
            'mem_rem': self.memory_remove_value,
            'mem_fetch': self.memory_fetch_value
        }

    def run_plugins(self, listfrom, incoming):
        '''
        incoming is the unparsed string. refer to test.py
        '''
        # if self.message_info(incoming)['args'][1][0] == ".":
        # print("\033[0;32mReceived!\033[0;0m")

        for plugin in listfrom:
            # print(f"\033[0;33mTrying {plugin}\033[0;0m")
            plugin.run(self, incoming, self.methods(), self.message_info(incoming), self.bot_info())

    '''
    SETUP REQUIREMENTS
    '''

    def requirements(self):
        reqs = []
        with open('../requirements.txt') as f:
            reqs = f.read().split('\n')
        reqs = [m.split('==')[0] for m in reqs if m]
        return reqs

    # TODO: classify methods according to APIs and have
    # a memory API
    def memory_add_value(self, memfile, section, key, value):
        memory_reader.read('memory/{}.txt'.format(memfile))
        memory_reader[section][key] = value
        with open('memory/{}.txt'.format(memfile), 'w') as file:
            memory_reader.write(file)

    def memory_remove_value(self, memfile, section, key):
        memory_reader.read('memory/{}.txt'.format(memfile))
        memory_reader.remove_option(section, key)
        with open('memory/{}.txt'.format(memfile), 'w') as file:
            memory_reader.write(file)

    def memory_fetch_value(self, memfile, section, key):
        memory_reader.read('memory/{}.txt'.format(memfile))
        return memory_reader[section][key]

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
                logger.info(msg)

                if len(data) == 0:
                    try:
                        logger.critical(f'<must handle reconnection - {len(data)}==0>')
                        sys.exit()
                    except Exception as e:
                        logger.info(e)
            except Exception as e:
                logger.info(e)

    # all in one for registered bot
    def registered_run(self):
        self.connect()
        self.identify()
        self.greet()
        self.load_plugins('PLUGINS')
        self.pull()

    def unregistered_run(self):
        self.connect()
        self.greet()
        self.load_plugins('PLUGINS')
        self.pull()

    '''
    ONGOING REQUIREMENT/S
    '''

    def stay_alive(self, incoming):
        if not incoming:
            logger.critical('<must handle reconnection - incoming is not True>')
            sys.exit()
        parts = incoming.split(':')
        if parts[0].strip().lower() == 'ping':
            # if self.domain in parts[1]:
            logger.warning(parts[1])
            self.send(self.pong_return(self.domain))
            self.send(self.pong_return(parts[1]))
