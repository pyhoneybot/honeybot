## 📃 Quickstart

fork repo, run run.py in /honeybot/run.py 


## 📃 Full Contributing Guide

- Don't forget to add your country flag ro the README.md after accepted PR. I'll have to hunt it down on your profile if you don't.
- Make sure to follow PEP8

**about PR**

First clone the project

```
git clone https://github.com/pyhoneybot/honeybot.git
```

cd into the project

```
cd honeybot
```

different changes to different files. For example, for someone making a weather plugin, first he creates a new branch
```
git checkout -b "weather-plugin"
```
then he commits
```
git add *
git commit -m "added weather plugin"


or


git commit -a -m "did this"
```

then he push to create a PR with the branch
```
git push origin head


or


git push origin weather-plugin
```

Now let us say he wants to work on another issue, such as adding a joke in the jokes plugin. He creates another branch
```
git checkout -b "add-jokes"
```
then, after writing the code, follow the same steps as before
```
git add *
git commit -m "added some jokes"
git push origin head
```
Now he wants to go back to fixing his weather plugin, he changes branch
```
git checkout weather-plugin
```
works, then commit
```
git add *
git commit -m "fixed <issue>"
```
then a PR
```
git push origin head
```

**Why all these?**

So as not to reject a whole PR just because of some oddities. Reject only unneeded part.

**Updating the Documentation**

If you created a new plugin you should add your plugin to the documentation.
To do this, go into your cloned honeybot repo and then into the directory *docs/source/Plugins* .
Depending on the type of plugin write this into the development, fun, miscellaneous or utility RST file:

```rst
   
   <Plugin-Name>
   ^^^^^^^^^^^^^
   .. automodule:: plugins.<your-plugin-filename>
      :members:
```
	  
This allows sphinx to automatically pull the docstrings from the code of your plugin and parse them accordingly.

A small guide on how to further contribute to the documentation of the project can be found [here](https://pyhoneybot.github.io/honeybot/How_Tos/documentation.html)

## 🥄 Updating fork

Now, other changes are ongoing, what if you need the latest changes?
```
git pull origin master
```
helps if you cloned your own repo. What if you want to update your local copy of someone else's repo that you forked?
You do it like that

```
cd <your/local/cloned/repo/path/here>
git remote add upstream https://github.com/pyhoneybot/honeybot.git
git fetch upstream
git pull upstream master
```