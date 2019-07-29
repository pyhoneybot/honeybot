# -*- coding: utf-8 -*-
"""
Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

    Section breaks are created by resuming unindented text. Section breaks
    are also implicitly created anytime a new section starts.

Attributes:
    connect_config (ConfigParser): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.
    memory_reader (ConfigParser): TODO.
    pluggins (List): TODO.
    logger (Logger): TODO.

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html
"""
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

"""
BOT CONNECTION SETUP
"""

class Bot_core(object):
    """
    Core of the bot.

    Detailed Description.

    Args:
        password (str): Password for the bot, defaults to ''

    Attributes:
        server_url (str): String for the IRC Server.
        port (int): Port for the IRC Server.
        name (str): Name of the bot.
        owners (list of str): String list of owners.
        password (str): Password of the bot.
        friends (list of str): String list of friends.
        autojoin_channels (list of str): String list of autojoin_channels.
        required_modules (list of str): String list of required modules.
        time (time): Get the current time.
        irc (socket): socket for the IRC server.
        isListenOn (int): TODO.
        domain (str): Server domain.
        sp_command (str): command string of the bot.
        plugins (lsit of str): List of plugins.
    """

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

    """
    STRINGS
    """

    def set_nick_command(self):
        """
        Get string for set nickname command.

        Returns:
            str: String for the set nick command.

        Examples:
            bot_core = Bot_core()
			bot_core.set_nick_command()
        """
        return 'NICK ' + self.name + '\r\n'

    def present_command(self):
        """
        Get string for present command.

        Returns:
            str: String for the present command.

        Examples:
            TODO
        """
        return 'USER ' + self.name + ' ' + self.name + ' ' + \
               self.name + ' : ' + self.name + ' IRC\r\n'

    def identify_command(self):
        """
        Get string for identify command.

        Returns:
            str: Command for the identify command.

        Examples:
            TODO
        """
        return 'msg NickServ identify ' + self.password + ' \r\n'

    def join_channel_command(self, channel):
        """
        Get string for join channel command.

        Args:
            channel (str): String of the channelname command.

        Returns:
            str: Command to join Channel.

        Examples:
            TODO
        """
        return 'JOIN ' + channel + ' \r\n'

    def specific_send_command(self, target, msg):
        """
        Get string for specific send command.

        Args:
            target (str): String of the target that should receive the message.
            msg (str): String of the Message that's to be sent to target.

        Returns:
            str: Command for messaging specific user.

        Examples:
            TODO
        """
        return "PRIVMSG " + target + " :" + msg + "\r\n"

    def pong_return(self, domain):
        """
        Get string for Pong command.

        Args:
            domain(str): String of the current domain.

        Returns:
            str: Command for Pong.

        Examples:
            TODO
        """
        return 'PONG :{}\r\n'.format(domain)

    """
    MESSAGE VALIDATION
    """

    def message_info(self, s):
        """
        Get info of a message.

        Args:
            s(str): TODO

        Returns:
            dict of {str: str}: TODO

        Examples:
            TODO
        """
        def prevent_none(x):
            """
            TODO

            Args:
                x(any or None): TODO

            Returns:
                Union of [x,''](any or str): returns x if x is not None else ''.

            Examples:
                TODO
            """
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
        """
        Get bot info.

        Returns:
            dict of {str: str}: TODO.

        Examples:
            TODO
        """
        return {
            'name': self.name,
            'special_command': self.sp_command,
            'required_modules': self.required_modules,
            'owners': self.owners,
            'time': self.time,
            'friends': self.friends
        }

    """
    MESSAGE UTIL
    """

    def send(self, msg):
        """
        Send a message.

        Args:
            msg (str): The message that's to be sent.

        Examples:
            TODO
        """
        self.irc.send(bytes(msg, "UTF-8"))

    def send_target(self, target, msg):
        """
        Send a specific message to target.

        Args:
            target (str): The target that's to be messaged.
            msg (str): The message that's to be sent.

        Examples:
            TODO
        """
        self.send(self.specific_send_command(target, msg))

    def join(self, channel):
        """
        Join a specific channel.

        Args:
            channel (str): The channel the bot should join.

        Examples:
            TODO
        """
        self.send(self.join_channel_command(channel))

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
        """
        Turn specified configfile to a list.

        Args:
            filenamae (str): Name of the file that should be converted.

        Returns:
            elements (list of str): Elements of the configfile as strings.

        Examples:
            TODO
        """
        elements = []
        with open('settings/{}.conf'.format(filename)) as f:
            elements = f.read().split('\n')
            elements = list(filter(lambda x: x != '', elements))
        return elements

    def methods(self):
        """
        Return methods of the bot.

        Returns:
            dict of {str:str}: Dictionary of command names and strings.

        Examples:
            TODO
        """
        return {
            'send_raw': self.send,
            'send': self.send_target,
            'join': self.join,
            'mem_add': self.memory_add_value,
            'mem_rem': self.memory_remove_value,
            'mem_fetch': self.memory_fetch_value
        }

    def run_plugins(self, listfrom, incoming):
        """
        Runs the plugins.

        Args:
            listfrom (TODO): TODO
            incoming (TODO): TODO

        Examples:
            TODO
        """

        '''
        incoming is the unparsed string. refer to test.py
        '''
        # if self.message_info(incoming)['args'][1][0] == ".":
        # print("\033[0;32mReceived!\033[0;0m")

        for plugin in listfrom:
            # print(f"\033[0;33mTrying {plugin}\033[0;0m")
            plugin.run(self, incoming, self.methods(), self.message_info(incoming), self.bot_info())

    """
    SETUP REQUIREMENTS
    """

    def requirements(self):
        """
        Return requirements of the bot.

        Returns:
            reqs (list of str): List of the requirements.

        Examples:
            TODO
        """
        reqs = []
        with open('../requirements.txt') as f:
            reqs = f.read().split('\n')
        reqs = [m.split('==')[0] for m in reqs if m]
        return reqs

    # TODO: classify methods according to APIs and have
    # a memory API
    def memory_add_value(self, memfile, section, key, value):
        """
        add value into memory.

        Args:
            memfile (TODO): TODO
            section (TODO): TODO
            key (TODO): TODO
            value (TODO): TODO

        Examples:
            TODO
        """
        memory_reader.read('memory/{}.txt'.format(memfile))
        memory_reader[section][key] = value
        with open('memory/{}.txt'.format(memfile), 'w') as file:
            memory_reader.write(file)

    def memory_remove_value(self, memfile, section, key):
        """
        remove value from memory.

        Args:
            memfile (TODO): TODO
            section (TODO): TODO
            key (TODO): TODO

        Examples:
            TODO
        """
        memory_reader.read('memory/{}.txt'.format(memfile))
        memory_reader.remove_option(section, key)
        with open('memory/{}.txt'.format(memfile), 'w') as file:
            memory_reader.write(file)

    def memory_fetch_value(self, memfile, section, key):
        """
        fetches value from memory.

        Args:
            memfile (TODO): TODO
            section (TODO): TODO
            key (TODO): TODO

        Returns:
            (str): Value of the key as a string.

        Examples:
            TODO
        """
        memory_reader.read('memory/{}.txt'.format(memfile))
        return memory_reader[section][key]

    """
    MESSAGE PARSING
    """
    def core_commands_parse(self, incoming):
        """
        parse core commands.

        Args:
            incoming (TODO): TODO

        Examples:
            TODO
        """
        '''
        PLUGINS
        '''
        self.run_plugins(self.plugins, incoming)

    '''
    BOT IRC FUNCTIONS
    '''
    def connect(self):
        """
        Connect to the IRC

        Examples:
            TODO
        """
        self.irc.connect((self.server_url, self.port))

    def identify(self):
        """
        Identifies command.

        Examples:
            TODO
        """
        self.send(self.identify_command())

    def greet(self):
        """
        Greet the channel ? (TODO).

        Examples:
            TODO
        """
        self.send(self.set_nick_command())
        self.send(self.present_command())
        for channel in self.autojoin_channels:
            self.send(self.join_channel_command(channel))

    def pull(self):
        """
        TODO

        Examples:
            TODO
        """
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
        """
        TODO

        Args:
            incoming (TODO): TODO

        Examples:
            TODO
        """
        if not incoming:
            logger.critical('<must handle reconnection - incoming is not True>')
            sys.exit()
        parts = incoming.split(':')
        if parts[0].strip().lower() == 'ping':
            logger.warning(parts[1])
            self.send(self.pong_return(self.domain))
            self.send(self.pong_return(parts[1]))

    # all in one for registered bot
    def registered_run(self):
        """
        TODO

        Examples:
            TODO
        """
        self.connect()
        self.identify()
        self.greet()
        self.load_plugins('PLUGINS')
        self.pull()

    def unregistered_run(self):
        """
        TODO

        Examples:
            TODO
        """
        self.connect()
        self.greet()
        self.load_plugins('PLUGINS')
        self.pull()
