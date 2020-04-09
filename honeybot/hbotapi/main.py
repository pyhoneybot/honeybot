# -*- coding: utf-8 -*-

import configparser
import importlib
import logging
import socket
import sys
import time

from hbotapi import commands
from hbotapi.utils import prevent_none
from hbotapi.utils import configfile_to_list
from hbotapi.utils import get_requirements
from hbotapi import memory

connect_config = configparser.ConfigParser()
connect_config.read('settings/CONNECT.conf')

memory_reader = configparser.ConfigParser()

plugins = []

# Start logger
logger = logging.getLogger('bot_core')

"""
BOT CONNECTION SETUP
"""

class Bot_core(object):

    def __init__(self, password=''):

        self.server_url = connect_config['INFO']['server_url']
        self.port = int(connect_config['INFO']['port'])
        self.name = connect_config['INFO']['name']
        self.owners = configfile_to_list('OWNERS')
        self.password = password
        self.friends = configfile_to_list('FRIENDS')
        self.autojoin_channels = configfile_to_list('AUTOJOIN_CHANNELS')
        self.required_modules = get_requirements()
        self.time = time.time()

        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.isListenOn = 1
        dom = self.server_url.split('.')
        self.domain = '.'.join(dom[-2:])
        self.sp_command = 'hbot'
        self.plugins = []
    """
    MESSAGE VALIDATION
    """

    def message_info(self, s):
        '''
        s : incoming
        '''
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
            address = args[0] if '#' in args[0] else prefix.split('!~')[0]
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

    def methods(self):
        return {
            'send_raw': self.send,
            'send': self.send_target,
            'join': self.join,
            'mem_add': memory.add_value,
            'mem_rem': memory.remove_value,
            'mem_fetch': memory.fetch_value
        }

    """
    MESSAGE UTIL
    """

    def send(self, msg):
        self.irc.send(bytes(msg, "UTF-8"))

    def send_target(self, target, msg):
        self.send(commands.specific_send(target, msg))

    def join(self, channel):
        self.send(commands.join_channel(channel))

    """
    BOT UTIL
    """

    def load_plugins(self, plugins_to_load):
        """
        Load plugins that are specified in the plugins list.

        Args:
            plugins_to_load (list of str): List of plugins to load.

        Examples:
            TODO
        """

        logger.info('Loading plugins...')

        to_load = []
        plugs = 'settings/{}.conf'.format(plugins_to_load)
        with open(plugs) as f:
            to_load = f.read().split('\n')
            to_load = list(filter(lambda x: x != '', to_load))
        for file in to_load:
            print('loading plugin:', file)
            try:
                module = importlib.import_module('plugins.{}.main'.format(file))
            except ModuleNotFoundError as e:
                logger.warning(f"{file}: module import error, skipped' {e}")
            obj = module
            self.plugins.append(obj)

        logger.info('Loaded plugins...')

    

    def run_plugins(self, incoming):
        '''
        incoming is the unparsed string. refer to test.py
        '''

        for plugin in self.plugins:
            P = getattr(plugin, 'Plugin')
            # print(f"\033[0;33mTrying {plugin}\033[0;0m")
            # print(self.plugins)
            incoming = incoming
            methods = self.methods()
            info = self.message_info(incoming)
            bot_info = self.bot_info()
            hbot_plugin = P()
            hbot_plugin.run(incoming, methods, info, bot_info)

    """
    MESSAGE PARSING
    """
    def core_commands_parse(self, incoming):
        self.run_plugins(incoming)

    '''
    BOT IRC FUNCTIONS
    '''
    def connect(self):
        self.irc.connect((self.server_url, self.port))

    def identify(self):
        self.send(commands.identify(self.password))

    def greet(self):
        self.send(commands.set_nick(self.name))
        self.send(commands.present(self.name))
        for channel in self.autojoin_channels:
            self.send(commands.join_channel(channel))

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

    """
    ONGOING REQUIREMENT/S
    """
    def stay_alive(self, incoming):
        if not incoming:
            logger.critical('<must handle reconnection - incoming is not True>')
            sys.exit()
        parts = incoming.split(':')
        if parts[0].strip().lower() == 'ping':
            logger.warning('ping detected from: {}'.format(parts[1]))
            self.send(commands.pong_return(self.domain))
            self.send(commands.pong_return(parts[1]))

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
