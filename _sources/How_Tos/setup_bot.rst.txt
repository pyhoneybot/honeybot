***************
Running the bot
***************

This How To will cover how to get our instance of the bot running in order to
test it's behaviour and functions.

Building Docker image
^^^^^^^^^^^^^^^^^^^^^

Change SERVER, PORT and NICKNAME variables to match your preferences

.. code-block::

   docker build -t "honeybot/honeybot:6.0.2" .

Running Docker image

.. code-block::

   docker run -d --name=honeybot honeybot/honeybot:v6.0.2 honeybot run

Quickstart
^^^^^^^^^^

    specify your details in CONNECT.conf (already included)

[INFO]

server_url = chat.freenode.net
port = 6667
name = appinventormuBot

    run run.py

Seeing The Bot In Action
^^^^^^^^^^^^^^^^^^^^^^^^

Get an IRC client

    Web: Kiwiirc (easy)
    Desktop: Hexchat
    Android: Revolution IRC

configure

port: 6667
url: chat.freenode.net

then join channel #ltch

you should see the bot as hbot ... or as it's name is in settings
