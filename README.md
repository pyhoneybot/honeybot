[![first-timers-only](https://img.shields.io/badge/first--timers--only-friendly-blue.svg?style=flat-square)](https://www.firsttimersonly.com/)
![Open Source Love](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-pink.svg) 
![MadeinMoris](https://img.shields.io/badge/Made%20in-Moris-green.svg)

# 🍯 honeybot py 

## 📮 About
HoneyBot is a python-based IRC bot. (**python3**)

Feel free to contribute to the project!
#
![alt text](honeybot_real.png "honeybot logo")

## 🕹 Project Motivation
Implementing the project in Java was weird, py's connect was sleek. Thus, the project stack was shifted over to Python.
If you can think of any features, plugins, or functionality you wish to see in the project. Feel free to add it yourself, or create an issue detailing your ideas. We highly recommend you attempt to implement it yourself first and ask for help in our slack page!

Psst. since i learnt py through this bot, we decided to keep a new-comers friendly policy. Feeling lost? Just ping.

## 📌 Contributing Countries

🇲🇺 🇺🇸 🇨🇦 🇦🇷 🇮🇳

## 📨 Follow the project on CodeTriage for updates!

get issues delivered in your inbox.

[![Open Source Helpers](https://www.codetriage.com/abdur-rahmaanj/honeybot/badges/users.svg)](https://www.codetriage.com/abdur-rahmaanj/honeybot)

## ✂ Current Features
 * 🍬 OOP architecture
 * 🛰️ keyword parameters
 * 🌵 password security with config file [disabled for now]
 * 🔌 now with plugins
 
## ⌚ Current Plugins

- 💎 bitcoin by [@Macr0Nerd](https://github.com/Macr0Nerd) - get price of bitcoin
- ⏲ caesar cipher by [@kylegalloway](https://github.com/kylegalloway) - encode your text
- 🔢 calc by [@Abdur-rahmaanJ](https://github.com/Abdur-rahmaanJ) - evaluates maths expressions
- 📐 maths by [@Abdur-rahmaanJ](https://github.com/Abdur-rahmaanJ) - sin cos and the like
- 🍃 conv sniff by [@Abdur-rahmaanJ](https://github.com/Abdur-rahmaanJ) - set triggers like how many times a word occur for one or more words and send response
- ❄ greet by [@Abdur-rahmaanJ](https://github.com/Abdur-rahmaanJ) - demo plugin
- 🕶 joke by [@Abdur-rahmaanJ](https://github.com/Abdur-rahmaanJ), [@colbyjayallen](https://github.com/colbyjayallen) - get random joke
- ❓ self Trivia by [@ajimenezUCLA](https://github.com/ajimenezUCLA) - random trivia
- 💢 username by [@Abdur-rahmaanJ](https://github.com/Abdur-rahmaanJ), [@sseryani](https://github.com/sseryani) - username generator
- 📜 quotes by [@German-Corpaz](https://github.com/German-Corpaz) - inspirational quotes
- 📖 dictionary by [@iamnishant14](https://github.com/iamnishant14) - returns meaning of word
- 🔣 password generator by [@iamnishant14](https://github.com/iamnishant14) - the name tells it all
- 🐜 debug by [@Abdur-rahmaanJ](https://github.com/Abdur-rahmaanJ) - prints all parameters passed to bot
- 📚 wikipedia by [@Macr0Nerd](https://github.com/Macr0Nerd) - returns a wikipedia article
- 🗿 translate by Ahmed Deeb - google translate plugin
- 📑 test by [@Abdur-rahmaanJ](https://github.com/Abdur-rahmaanJ) - runs tests
- ⛅️ weather by [@Macr0Nerd](https://github.com/Macr0Nerd) - returns weather info for a given location

## 📃 Contributing Guide

- don't forget to add your country flag here after accepted PR. i'll have to hunt it down on your profile if not.
- make sure to follow PEP8
- different changes to different files. for example, someone making a weather plugin first he creates a new branch
```
git checkout -b "weather-plugin" 
```
then he commits
```
git add *
git commit -m "added weather plugin"
```
then he push to create a PR with the branch
```
git push origin head
```
now let us say he wants to work on another issue, adding a joke in the jokes plugin, he creates another branch
```
git checkout -b "add-jokes" 
```
after, same as before
```
git add *
git commit -m "added some jokes"
git push origin head
```
now he wants to fix his weather plugin, he changes branch
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

## 🥄 Updating fork

Now, other changes are ongoing, what if you need the latest changes?

```
git pull origin master
```
helps if you cloned your own repo. What is you want to update your local copy of someone else repo?
you do it like that 

```
cd <your/local/cloned/repo/path/here>
git remote add upstream git://github.com/Abdur-rahmaanJ/honeybot.git
git fetch upstream
git pull upstream master
```

## 🔧 Plugins Development

including it here. let's begin

a plugin has the following structure:

```python
# -*- coding: utf-8 -*-
"""
[greet.py]
Greet Plugin
[Author]
Abdur-Rahmaan Janhangeer, pythonmembers.club
[About]
responds to .hi, demo of a basic plugin
[Commands]
>>> .hi
returns hoo
"""


class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info):
        try:
            if info['command'] == 'PRIVMSG' and info['args'][1] == '.hi':
                methods['send'](info['address'], 'hooo')
        except Exception as e:
            print('woops plugin error ', e)
```
we see three parameters being passed to the run method ```, incoming, methods, info)```

#### parameter1: incoming

```incoming``` is the raw line and is not used except if you are not satisfied with the already provided methods

#### parameter2: methods

```methods``` is a dictionary of methods to ease your life. a quick look at [main.py](honeybot/main.py) reveals

```python
def methods(self):
        return {
                'send_raw': self.send,
                'send': self.send_target,
                'join': self.join
                }
```
where ```send_raw``` allows you to send in any string you want, thereby allowing you to implement any irc protocol from scratch

but, for most uses, ```send``` allows you to send a message to an address ```methods['send']('<address>', '<message>')```. using it in conjunction with info parameter allows you to send messages where it came from, in pm to the bot or in a channel. you can however hardcode the address.

```join``` allows you to join a channel by ```methods['join']('<channel name>')```

#### parameter3: info

for a normal run, info produces
```python
{
'prefix': 'appinv!c5e342c5@gateway/web/cgi-irc/kiwiirc.com/ip.200.200.22.200',
'command': 'PRIVMSG',
'address': '##bottestingmu',
'args': ['##bottestingmu', 'ef']
}
```
hence if you want messages, ```messages = info['args'][1:]``` or the first word if you want to check for command will be ```info['args'][1]```

#### wrapping up

hence
```python
if info['command'] == 'PRIVMSG' and info['args'][1] == '.hi':
    methods['send'](info['address'], 'hooo')
```
from above means 
```
if message received == .hi:
    send(address, message)
```

#

## ⚡ Quickstart

- specify your details in CONNECT.conf (already included)
~~~
[INFO]

server_url = chat.freenode.net
port = 6667
name = appinventormuBot
~~~
- run main.py

## 🔌 Todo Plugins
- [x] 💐 humour
- [x] 🌨️ weather
- [ ] ✉️ mail
- [x] 🎛️ maths
- [ ] 📥 pm when user online

## ☑ Allowing Plugins
in PLUGINS.conf, add the plugin to allow on a new line !
~~~
calc
username
~~~

## 📧 Contact
### Email
- Abdur-Rahmaan Janhangeer | arj.python@gmail.com
### Discord
https://discord.gg/E6zD4XT

## 🖊 Credits
[@arwinneil](https://github.com/arwinneil) for opensource and madeinmoris badges

