****
Main
****

.. automodule:: main

Bot_core
--------

.. currentmodule:: main
.. autoclass:: Bot_core

Command String Output
^^^^^^^^^^^^^^^^^^^^^

   The section inhabits the functions of the Bot_core class which are responsible
   for generating the command string and returning it to the function that actually
   executes the command.

   .. currentmodule:: main.Bot_core

   .. automethod:: main.Bot_core.set_nick_command

   .. automethod:: main.Bot_core.present_command

   .. automethod:: main.Bot_core.identify_command

   .. automethod:: main.Bot_core.join_channel_command

   .. automethod:: main.Bot_core.specific_send_command

   .. automethod:: main.Bot_core.pong_return

Message Validation
^^^^^^^^^^^^^^^^^^

   Description of message validation section

   .. automethod:: main.Bot_core.message_info

   .. autofunction:: main.Bot_core.bot_info

Message util
^^^^^^^^^^^^

   Message util Description

   .. automethod:: main.Bot_core.send

   .. automethod:: main.Bot_core.send_target

   .. automethod:: main.Bot_core.join

Bot util
^^^^^^^^

   Bot util Description

   .. automethod:: main.Bot_core.load_plugins

   .. automethod:: main.Bot_core.configfile_to_list

   .. automethod:: main.Bot_core.methods

   .. automethod:: main.Bot_core.run_plugins

Setup requirements
^^^^^^^^^^^^^^^^^^

   Setup requirements Description

   .. automethod:: main.Bot_core.requirements

   .. automethod:: main.Bot_core.memory_add_value

   .. automethod:: main.Bot_core.memory_remove_value

   .. automethod:: main.Bot_core.memory_fetch_value

Message parsing
^^^^^^^^^^^^^^^

   Message parsing Description

   .. automethod:: main.Bot_core.core_commands_parse

Bot IRC Functions
^^^^^^^^^^^^^^^^^

   Bot IRC Functions Description

   .. automethod:: main.Bot_core.connect

   .. automethod:: main.Bot_core.identify

   .. automethod:: main.Bot_core.greet

   .. automethod:: main.Bot_core.pull

Ongoing requirement/s
^^^^^^^^^^^^^^^^^^^^^

   Ongoing requirement/s Description

   .. automethod:: main.Bot_core.stay_alive

   .. automethod:: main.Bot_core.registered_run

   .. automethod:: main.Bot_core.unregistered_run
