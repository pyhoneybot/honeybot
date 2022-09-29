*************************
Setting up Documentation
*************************

This How To focuses on setting up **Sphinx** in order to edit the HoneyBot documentation.
You *don't* need to do this if you're simply adding a plugin.
If you should have **any** questions feel free to ask on our discord_!

For documentation HoneyBot uses a tool named sphinx_. Sphinx reads in
the docstrings of functions, methods and classes and automatically parses
them as you can see in the actual documentation.

Requirements
^^^^^^^^^^^^

To generate the documentation you will need to have sphinx installed,
click here_ for a quick installation guide. **Make sure you've installed the
python 3 (new) version of sphinx and Read The Docs theme!**.

**'pip install sphinx sphinx_rtd_theme'**.

There's no need to set up this tool with **'sphinx-quickstart'** command, once there is a configuration already.

Create a fork of our honeybot project and clone this:

**'git clone https://github.com/<YOU>/honeybot.git'**

Then change the path `honeybot/docs/source/`_ and edit the *.rst* files there.
These *.rst* files they are too on following paths: `honeybot/docs/source/How_Tos/`_ and `honeybot/docs/source/Plugins/`_.

Next you’ll need to have the **gh-pages** branch from your fork cloned as a directory named **‘html’**, into your cloned repo:

**'cd honeybot'**

**'git clone -b gh-pages https://github.com/<YOU>/honeybot.git html'**

Your folder structure needs to look as follows:

+----------+----------------------------------+
| honeybot/|          <==== master fork repo  |
+==========+==================================+
| ├── docs |                                  |
+----------+----------------------------------+
| |        |└── source                        |
+----------+----------------------------------+
| ├── html |         <==== gh-pages fork repo |
+----------+----------------------------------+
| ├── src  |                                  |
+----------+----------------------------------+
|          |└── honeybot                      |
+----------+----------------------------------+

Generating docs
^^^^^^^^^^^^^^^

Once you’re set up you can test if sphinx works properly in `honeybot/docs/`_ directory, by changing to 'html' folder, opening a terminal and typing **'sphinx-build ../docs/source/ .'**. This will take the *.rst* files in 
`honeybot/docs/source/`_ and ‘make’ them into html in 'html/' folder that contains the 'gh-pages' branch. If it shows any warning you’ll have to fix them before committing, otherwise the documentation wont be automatically build once you push your changes to Github.
Next you can 'add' and 'commit' these changes into your fork by typing:

**git add \***

**git commit -m "Commit message"**

Finally, you can make a pull request by typing:

**git push origin gh-pages:gh-pages**

And this'll create a PR in the **gh-pages** branch that'll be analysed by someone in project.

Later do you still need to push the master branch too. Because the *.rst* files are on this branch and were not go to the previus PR:

**git add docs/source \***

**git commit -m "Commit message"**

**git push origin master**

Since I won't provide a full tutorial on how to write *.rst* files here is a useful
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
