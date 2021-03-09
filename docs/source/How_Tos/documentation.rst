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
python 3 (new) version of sphinx!**

Furthermore you'll need to have the **gh-pages** branch cloned as a directory
named **'html'** and a new branch from master, the name should match the
contribution (for example *'Docs_how_to'*).

Your folder structure needs to look as follows:

::
  <any_folder>
    ├── honeybot-docs
    │   ├── html <--- gh-pages repo
    │
    ├── honeybot <---- Docs_how_to repo

Generating docs
^^^^^^^^^^^^^^^

Once you're set up you can test if sphinx works properly by going to
*<any_folder>/honeybot/docs*, opening a terminal and typing **'make html'**.
This will take the rst files in *<any_folder>/honeybot/docs/source* and 'make'
them into html in your html folder.
If it shows any warning you'll have to fix them before committing, otherwise the documentation
wont be automatically build once you push your changes to Github.

Since I won't provide a full tutorial on how to write rst files here is a useful
link:
rst_


.. _sphinx: https://www.sphinx-doc.org/en/master/index.html
.. _here: https://www.sphinx-doc.org/en/master/usage/installation.html#overview
.. _discord: discord <https://discordapp.com/invite/E6zD4XT
.. _rst: http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html#
