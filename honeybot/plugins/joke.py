# -*- coding: utf-8 -*-
"""
[joke.py]
Joke Plugin

[Author]
Abdur-Rahmaan Janhangeer, pythonmembers.club

[About]
sends a random joke on request

[Commands]
>>> .joke
returns a random joke
"""
import random


class Plugin:
    def __init__(self):
        pass

    def joke(self):
        jokes = [
'Why did the physics teacher break up with the biology teacher? There was no \
    chemistry.',
'I asked my daughter if she’d seen my newspaper. She told me that newspapers \
    are old school.She said that people use tablets nowadays and handed me her \
    iPad. The fly didn’t stand a chance',
'A recent scientific study showed that out of 2,293,618,367 people, 94% are \
    too lazy to actually read that number.',
'Why is it a bad idea to insult an octopus? because it is well armed',
'Two cannibals are eating a clown, one looks to the other and asks "Does this \
    taste funny to you?"',
'What is red and smells like blue paint? Red Paint.',
'How many South Americans does it take to change a lightbulb? A Brazilian!',
'I have just invented a new word. Plagiarism.',
'Why should you never trust an atom? Because they make up everything.',
'What is brown and sticky? A stick!',
'I tried to take a bite out of the fog, but I mist.',
'What did the bodybuilder say when he ran out of protein powder? No whey.',
'What do you call a fake noodle? An Impasta.',
'Did you hear about the restaurant on the moon? It had great food but no \
    atmosphere.',
'Why do the put fences around grave yards? Because people are dying to get in.',
'How do you organize a party on Mars? You planet.',
'Why do crabs never give to charity? Because they are shellfish.',
'What is the difference between an African and Indian Elephant? About 5000 miles.',
'I don\'t like to play soccer for money. I play it just for kicks.',
'How many apples grow on a tree? All of them!',
'Did you hear the rumor about the butter? Well, I\'m not going to spread it...',
'How does a penguin build his home? Igloos it together!',
'How to make a tissue dance? Put a little boogie in it!',
'If you saw a robbery at the Apple store, would you be an iWitness?',
'Why did the blind man turn down the job? He couldn\'t see himself doing it.',
'Want to hear a joke about construction? We\'re still working on it.',
'As I handed my dad his 50th birthday card, he looked at me with tears in his \
    eyes and said, "You know, one would have been enough."',
'I caught my wife yelling at the TV saying, "Don\'t go into the church you idiot!", \
    She was watching our wedding video again.',
'When a woman is giving birth, she is literally kidding.',
'My wife yelled at me agai for having no sense of direction. So I packed up my stuff and right.',
'My son asked, "Can I have a book mark?" and I burst into tears. 11 years old and he still doesn\'t \
    know my name in Brian.',
'If a child refuses to sleep during nap time, are they guilty of resisting a rest?',
'Geology rocks, but Geography is where it\'s at.',
'Scientists were starting to get bored watching the Earth turn, and so after 24 hours, they \
    called it a day.',
'My wife yelled at me an said, "You haven\'t listened to anything I\'ve said!", which \
    I thought was an interesting way to start a conversation.',
'I’d tell you a Fibonacci joke, but’s it’s probably as bad as the last two you’ve heard combined.',
'What did the pirate say on his 80th birthday? AYE MATEY.'
]

        return '{}'.format(random.choice(jokes))

    def run(self, incoming, methods, info, bot_info):
        try:
            # if '!~' in info['prefix']:
                # print(info)
            msgs = info['args'][1:]
            if info['command'] == 'PRIVMSG' and msgs[0] == '.joke':
                methods['send'](info['address'], Plugin.joke(self))
        except Exception as e:
            print('woops plug', e)
