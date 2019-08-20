*******************
Plugin Development
*******************

.. toctree::
   :maxdepth: 1
   
This How To should give you enough informations to be able to develop a plugin for HoneyBot.
First of, we'll take a look at the structure of a plugin:

.. literalinclude:: Examples/plugin_structure.py
   :language: python

we see four parameters being passed to the run method , incoming, methods, info, bot_info)


.. rubric:: parameter1: incoming

incoming is the raw line and is not used except if you are not satisfied with the already provided methods

.. rubric:: parameter2: methods

methods is a dictionary of methods to ease your life. a quick look at main.py reveals

.. code-block:: python

	def methods(self):
			return {
					'send_raw': self.send,
					'send': self.send_target,
					'join': self.join
					}

where send_raw allows you to send in any string you want, thereby allowing you to implement any irc protocol from scratch

but, for most uses, send allows you to send a message to an address *methods['send']('<address>', '<message>')*. using it in conjunction with info parameter allows you to send messages where it came from, in pm to the bot or in a channel. you can however hardcode the address.

join allows you to join a channel by *methods['join']('<channel name>')*

.. rubric:: parameter3: info

for a normal run, info produces

.. code-block:: python

	{
	'prefix': 'appinv!c5e342c5@gateway/web/cgi-irc/kiwiirc.com/ip.200.200.22.200',
	'command': 'PRIVMSG',
	'address': '##bottestingmu',
	'args': ['##bottestingmu', 'ef']
	}

hence if you want messages, *messages = info['args'][1:]* or the first word if you want to check for command will be info['args'][1]

.. rubric:: use example

the command info is used in the join channel plugin to detect a join command and greet the user who just joined

.. rubric:: bot info

bot_info returns info about the bot

.. code-block:: python

	return {
		'name': self.name,
		'special_command': self.sp_command,
		'required_modules': self.required_modules,
		'owners': self.owners,
		'time': self.time,
		'friends': self.friends
	}

so that in run method you can access those.

.. rubric:: use example

For example, the time info is used in the uptime plugin by minussing it from the current time to get time bot has been running.
The required modules is used in the installed plugin to determine what required plugin the bot runner did not install

.. rubric:: wrapping up

hence

.. code-block:: python

	if info['command'] == 'PRIVMSG' and info['args'][1] == '.hi':
		methods['send'](info['address'], 'hooo')

from above means

.. code-block:: python

	if message received == .hi:
		send(address, message)

.. _sphinx: https://www.sphinx-doc.org/en/1.5/index.html_
.. _here: https://www.sphinx-doc.org/en/master/usage/installation.html/en/1.5/index.html
.. _discord: discord <https://discordapp.com/invite/E6zD4XT
.. _rst: http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html#
