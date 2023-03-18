*******************
Contributing
*******************

This page will explain how to contribute to the project properly.
   
Pull Requests
^^^^^^^^^^^^^

first clone the project

.. code-block::

   git clone https://github.com/pyhoneybot/honeybot.git

cd into the project

.. code-block::

   cd honeybot

create a virtualenv to work with different python \ libs versions

.. code-block::
   
   python -m venv venv
   source venv/bin/activate

install the tools needed to make the constraint checks

.. code-block::

   pip install black isort bandit pre-commit
   pre-commit install

different changes to different files. for example, someone making a weather plugin first he creates a new branch

.. code-block::

   git checkout -b "weather-plugin"

test if all files are well formatted, complying with style and security rules, before send the PR

.. code-block::

    black --config ./pyproject.toml src/honeybot/plugins/downloaded/weather/main.py
    isort --settings-path ./pyproject.toml src/honeybot/plugins/downloaded/weather/main.py
    bandit -ll -c ./pyproject.toml -r src/honeybot/plugins/downloaded/weather/main.py     


then he commits

.. code-block::

   git add *
   git commit -m "added weather plugin"

or

.. code-block::

   git commit -a -m "did this"

then he push to create a PR with the branch

.. code-block::

   git push origin head

or

.. code-block::

   git push origin weather-plugin

now let us say he wants to work on another issue, adding a joke in the jokes plugin, he creates another branch

.. code-block::

   git checkout -b "add-jokes"

after, same as before

.. code-block::

   git add *
   git commit -m "added some jokes"
   git push origin head

now he wants to fix his weather plugin, he changes branch

.. code-block::

   git checkout weather-plugin

works, then commit

.. code-block::

   git add *
   git commit -m "fixed <issue>"

then a PR

.. code-block::

   git push origin head

.. rubric:: parameter2: Why all these?

So as not to reject a whole PR just because of some oddities. Reject only unneeded part.

Updating fork
^^^^^^^^^^^^^

Now, other changes are ongoing, what if you need the latest changes?

git pull origin master

helps if you cloned your own repo. What if you want to update your local copy of someone else's repo that you forked? You do it like that

cd <your/local/cloned/repo/path/here>
git remote add upstream https://github.com/pyhoneybot/honeybot.git
git fetch upstream
git pull upstream master

Updating the Docs
^^^^^^^^^^^^^^^^^

If you created a new plugin you should add your plugin to the documentation.
To do this, go into your cloned honeybot repo and then into the directory *docs/source/Plugins* .
Depending on the type of plugin write this into the development, fun, miscellaneous or utility file:

.. code-block::
   
   <Plugin-Name>
   ^^^^^^^^^^^^^
   
   .. automodule:: plugins.<your-plugin-filename>
      :members:
	  
This allows sphinx to automatically pull the docstrings from the code of your plugin and parse them accordingly.
