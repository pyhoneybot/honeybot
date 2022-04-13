*************************
Setting up Documentation
*************************

This How To focuses on setting up Sphinx in order to edit the HoneyBot documentation.
You *don't* need to do this if you're simply adding a plugin.
If you should have **any** questions feel free to ask on our discord_!

For documentation HoneyBot uses a tool named sphinx_. Sphinx reads in
the docstrings of functions, methods and classes and automatically parses
them as you can see in the actual documentation.

Requirements
^^^^^^^^^^^^

To generate the documentation you will need to have sphinx installed,
click here_ for a quick installation guide. **Make sure you've installed the
python 3 (new) version of sphinx!**.
There's no need to set up this tool with **'sphinx-quickstart'** command, once there is a configuration already.

Furthermore you'll need to have the **master** branch cloned from honeybot
repo and a new branch from this master clone.
Then change the path `honeybot/docs/source/`_ and edit the *.rst* files there.
These *.rst* files they are too on following paths: `honeybot/docs/source/How_Tos/`_ and `honeybot/docs/source/Plugins/`_.

Generating docs
^^^^^^^^^^^^^^^

Once you're set up you can test if sphinx works properly by going to
`honeybot/docs/`_, opening a terminal and typing **'make html'**.
This will take the rst files in `honeybot/docs/source*`_
and 'make' them into html in the *../../honeybot-docs/html* folder.
If it shows any warning you'll have to fix them before committing, otherwise the documentation
wont be automatically build once you push your changes to Github.

Since I won't provide a full tutorial on how to write rst files here is a useful
link:
rst_


.. _sphinx: https://www.sphinx-doc.org/en/master/
.. _here: https://www.sphinx-doc.org/en/master/usage/quickstart.html
.. _discord: https://discordapp.com/invite/E6zD4XT
.. _rst: https://packagecontrol.io/packages/Restructured%20Text%20%28RST%29%20Snippets
.. _honeybot/docs/source/: https://github.com/pyhoneybot/honeybot/tree/master/docs/source
.. _honeybot/docs/source/How_Tos/: https://github.com/pyhoneybot/honeybot/tree/master/docs/source/How_Tos
.. _honeybot/docs/source/Plugins/: https://github.com/pyhoneybot/honeybot/tree/master/docs/source/Plugins
.. _honeybot/docs/: https://github.com/pyhoneybot/honeybot/tree/master/docs
.. _honeybot/docs/source*: https://github.com/pyhoneybot/honeybot/tree/master/docs/source