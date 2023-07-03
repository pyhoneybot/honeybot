import configparser
import importlib
import logging
import os
import pathlib
import socket
import subprocess
import sys
import time

import pkg_resources

from honeybot.api import commands, memory
from honeybot.api.utils import configfile_to_list, get_requirements, prevent_none
from honeybot.api import print as output

import tomli

plugins = []

# Start logger
logger = logging.getLogger("bot_core")

"""
BOT CONNECTION SETUP
"""


class BotCore:
    def __init__(self, info, password=""):
        self.info = info
        with open(info['toml_path'], 'rb') as f:
            self.configs = tomli.load(f)
        self.settings_path = self.info["settings_path"]
        self.root_path = self.info["cwd"]
        self.server_url = self.configs["INFO"]["server_url"]
        self.port = int(self.configs["INFO"]["port"])
        self.name = self.configs["INFO"]["name"]
        self.owners = self.configs["USERNAMES"]["owners"]
        self.password = password
        self.friends = self.configs["USERNAMES"]["friends"]
        self.autojoin_channels = self.configs["INFO"]["autojoin_channels"]
        self.downloaded_plugins_to_load = self.configs["PLUGINS"]["downloaded"]
        self.required_modules = get_requirements()
        self.time = time.time()

        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.is_listen_on = 1
        dom = self.server_url.split(".")
        self.domain = ".".join(dom[-2:])
        self.sp_command = "hbot"
        self.plugins = []
        self.core_plugins = []

    """
    MESSAGE VALIDATION
    """

    def message_info(self, s):
        """
        s : incoming
        """
        try:
            prefix = ""
            trailing = []
            address = ""
            if not s:
                pass
            if s[0] == ":":
                prefix, s = s[1:].split(" ", 1)
            if s.find(" :") != -1:
                s, trailing = s.split(" :", 1)
                args = s.split()
                args.append(trailing)
            else:
                args = s.split()
            command = args.pop(0)
            address = args[0] if "#" in args[0] else prefix.split("!~")[0]
            user = prefix.split("!")[0]
            # return prefix, command, args, address
            return {
                "prefix": prevent_none(prefix),
                "command": prevent_none(command),
                "args": ["" if e is None else e for e in args],
                "address": prevent_none(address),
                "user": prevent_none(user),
            }
        except Exception as e:
            # logger.error(e)
            pass

    def bot_info(self):
        return {
            "name": self.name,
            "special_command": self.sp_command,
            "required_modules": self.required_modules,
            "owners": self.owners,
            "time": self.time,
            "friends": self.friends,
        }

    def methods(self):
        return {
            "send_raw": self.send,
            "send": self.send_target,
            "join": self.join,
            "mem_add": memory.add_value,
            "mem_rem": memory.remove_value,
            "mem_fetch": memory.fetch_value,
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
    PLUGIN UTILS
    """

    def is_valid_plug_name(self, name):
        if name.startswith("__") or name == "":
            return False

        return True

    """
    BOT UTIL
    """

    def print_running_infos(self):
        print(output.status('i')+ " Run infos:")
        for key in self.info:
            print(output.tab()+' '+key, self.info[key])
        print(output.line())

    def load_plugins_from_folder(self, category_folder, from_conf=None, from_dir=None):
        if from_dir is True:
            dir_path = os.path.join(self.info["plugins_path"], "core")
            to_load = [f for f in os.listdir(dir_path) if self.is_valid_plug_name(f)]
        elif from_conf is True:
            to_load = self.configs['PLUGINS']['downloaded']

        print(output.status('i')+ " Loading from", category_folder)
        for folder in to_load:
            print(output.tab(), "loading plugin:", folder)
            try:
                sys.path.append(self.root_path)
                module = importlib.import_module(f"plugins.{category_folder}.{folder}.main")
                obj = module
                self.plugins.append(obj)
            except ModuleNotFoundError as e:
                logger.warning(f"{folder}: module import error, skipped' {e}")

            try:
                req_path = os.path.join(
                    self.info["cwd"],
                    "plugins",
                    category_folder,
                    folder,
                    "requirements.txt",
                )
                if os.path.exists(req_path):
                    with pathlib.Path(req_path).open() as requirements_txt:
                        install_requires = [
                            str(requirement)
                            for requirement in pkg_resources.parse_requirements(requirements_txt)
                        ]
                        print("installing", install_requires)
                        subprocess.check_call(
                            [sys.executable, "-m", "pip", "install", *install_requires]
                        )
            except Exception as e:
                # logger.debug(e)
                pass

    def load_plugins(self):
        """
        Load plugins that are specified in the plugins list.

        Args:
            plugins_to_load (list of str): List of plugins to load.

        Examples:
            TODO
        """

        print(output.status('i')+ " Loading plugins...")

        self.load_plugins_from_folder("downloaded", from_conf=True)
        self.load_plugins_from_folder("core", from_dir=True)

        print(output.status('x')+ " Loaded plugins")
        print(output.line())

    def run_plugins(self, incoming):
        """
        incoming is the unparsed string. refer to test.py
        """

        for plugin in self.plugins:
            P = getattr(plugin, "Plugin")
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

    """
    BOT IRC FUNCTIONS
    """

    def connect(self):
        self.irc.connect((self.server_url, self.port))

    def identify(self):
        self.send(commands.identify(self.password))

    def greet(self):
        self.send(commands.set_nick(self.name))
        self.send(commands.present(self.name))
        for channel in self.autojoin_channels:
            self.send(commands.join_channel(channel))
        print(output.status('x'), 'Joined channels:', ', '.join(self.autojoin_channels))

    def pull(self):
        print(output.status('i'), 'Listening to incoming messages')
        while self.is_listen_on:
            try:
                data = self.irc.recv(2048).decode("UTF-8", errors="replace")
                for line in data.split("\r\n"):
                    if line != "":
                        self.core_commands_parse(line)

            except KeyboardInterrupt:
                self.is_listen_on = False
                self.quit()
            except Exception as e:
                # logger.error(e)
                # print(e)
                # logger.debug("there was an error")
                # logger.debug(data)
                # logger.debug("!!")
                # logger.debug(line)
                # logger.debug("-" * 50)
                pass

    def quit(self):
        self.send(commands.quit())
        self.is_listen_on = False

    """
    ONGOING REQUIREMENT/S
    """
    def stay_alive(self, incoming):
        if not incoming:
            logger.critical("<must handle reconnection - incoming is not True>")
            sys.exit()
        parts = incoming.split(":")
        if parts[0].strip().lower() == "ping":
            logger.warning(f"ping detected from: {parts[1]}")
            self.send(commands.pong_return(self.domain))
            self.send(commands.pong_return(parts[1]))

    # all in one for registered bot
    def registered_run(self):
        self.connect()
        self.identify()
        self.greet()
        self.load_plugins()
        self.pull()

    def unregistered_run(self):
        self.print_running_infos()
        self.connect()
        self.greet()
        self.load_plugins()
        self.pull()
