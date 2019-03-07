[![first-timers-only](https://img.shields.io/badge/first--timers--only-friendly-blue.svg?style=flat-square)](https://www.firsttimersonly.com/)
![Open Source Love](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-pink.svg) 
![MadeinMoris](https://img.shields.io/badge/Made%20in-Moris-green.svg)

# 🍯 honeybot py 

## about
honeybot: the bot to learn python. feel free to pr.
#
![alt text](honeybot_real.png "honeybot logo")

## don't miss updates, follow on
[![Open Source Helpers](https://www.codetriage.com/abdur-rahmaanj/honeybot/badges/users.svg)](https://www.codetriage.com/abdur-rahmaanj/honeybot)

## some history
i actually started learning python through that bot. java was too much a pain for a simple connection. learnt some new py tricks? create a plugin that uses it ^^

## contributing countries

🇲🇺 🇺🇸 🇨🇦 🇦🇷 

## ✂ some features

 * 🍬 OOP architecture
 * 🛰️ keyword parameters
 * 🌵 password security with config file [disabled for now]
 * 🔌 now with plugins
 
## 📚 more info
[[ wiki ]](https://github.com/Abdur-rahmaanJ/honeybot/wiki)

## contributing guide

- don't forget to add your country flag here after accepted PR. i'll have to hunt it down on your profile if not.

## plugins devlopment

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

## quickstart

- specify your details in CONNECT.conf (already included)
~~~
[INFO]

server_url = chat.freenode.net
port = 6667
name = appinventormuBot
~~~
- run main.py

## todo 🔌 plugins
- [x] 💐 humour
- [ ] 🌨️ weather
- [ ] ✉️ mail
- [x] 🎛️ maths
- [ ] 📥 pm when user online

## allow plugins
in PLUGINS.conf, add the plugin to allow on a new line !
~~~
calc
username
~~~

## contact
### Email
- Abdur-Rahmaan Janhangeer | 📧 arj.python@gmail.com
### Slack
https://honeybotworkspace.slack.com/messages/CGQLHMNCE/

## credits
[@arwinneil](https://github.com/arwinneil) for opensource and madeinmoris badges
 



