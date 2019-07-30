# -*- coding: utf-8 -*-
"""
[fact.py]
Fact Plugin

[Author]
Justin Walker

[About]
Returns a random fact.
Facts sourced from Mental Floss 
http://mentalfloss.com/article/55443/101-amazing-facts

[Commands]
>>> .fact
returns random fact
"""

import random


class Plugin:
    def __init__(self):
        pass

    def __fact():
        return random.choice(FACT_LIST)

    def run(self, incoming, methods, info, bot_info):
        try:
            if info['command'] == 'PRIVMSG' and info['args'][1] == '.fact':
                methods['send'](info['address'], Plugin.__fact())
        except Exception as e:
            print('woops plugin error: ', e)


FACT_LIST = [
    "In 2006, an Australian man tried to sell New Zealand on Ebay. The " + \
        "price reached $3,000 before it was shut down.",
    "In Japan, letting a sumo wrestler make your baby cry is considered " + \
        "good luck.",
    "When three-letter airport codes became a standard, airports that " + \
        "been using two letters simply added an X.",
    "The actor who was inside R2-D2 hated the guy who played C-3PO, " + \
        "calling him the 'The rudest man I've ever met.'",
    "At one point in the 1990's, 50% of all CD's produced worldwide" + \
        "were for AOL.",
    "Toy companies failed to duplicate the success of Theodore " + \
        "Roosevelt's Teddy Bear with William Taft's 'Billy Possum.'",
    "Nutella was invented during WWII, when an Italian pastry maker " + \
        "mixed hazelnuts into chocolate to extend his chocolate ration.",
    "In response to 'The Lorax', the forest products industry published " + \
        "'Truax' to teach kids the importance of logging.",
    "Tsutomu Yamaguchi was in Hiroshima for work when the first A-Bomb " + \
        "hit, make it home to Nagasaki for the second, and lived to be 93.",
    "A British man changed his name to Tim PPPPPPPPPPrice to make it " + \
        "harder for telemarketers to pronounce.",
    "J.P. Morgan once offered $100,000 to anyone who could figure out why" + \
        "his face was so red. No one solved the mystery.",
    "Prairie dogs say hello with kisses.",
    "Before settling on the Seven Dwarfs we know today, Disney " + \
        "considered Chesty, Tubby, Burpy, Deafy, Hickey, Wheezy, and Awful.",
    "New Mexico State's first graduating class in 1893 had only one " + \
        "student - and he was shot and killed before graduation.",
    "Jonas Salk declined to patent his Polio Vaccine. 'There is no " + \
        "patent,' he said. 'Could you patent the sun?'",
    "The 50-star American Flag was designed by and Ohio High School " + \
        "student for a class project. His teacher originally gave him " + \
        "a B-.",
    "Sean Connery turned down the Gandalf role in 'The Lord of the " + \
        "Rings'. 'I read the book. I read the script. I saw the movie. " + \
        "I still don't understand it.",
    "Chock Full O'Nuts Coffee does not contain nuts. It's named for a " + \
        "chain of nut stores that the founder converted into coffee shops.",
    "12+1 = 11+2, and 'Twelve plus one' is an anagram of 'eleven plus " + \
        "two'.",
    "At the height of Rin Tin Tin's fame, a chef prepared him a daily " + \
        "steak lunch. Classical musicians played to aid his digestion.",
    "The Arkansas school for the Deaf's nickname is the Leopards. The " + \
        "Deaf Leopards.",
    "If your dog's feet smell like corn chips, you're not alone. The term" + \
        "'Frito feet' was coined to describe the scent.",
    "Barry Manilow did not write his hit 'I Write the Songs'.",
    "Barry Manilow wrote State Farm's 'Like a Good Neighbor' jingle.",
    "Winston Churchill's mother was born in Brooklyn.",
    "Officials in Portland, OR, drained 8 million gallons of water from " + \
        "a resevoir in 2011 because a buzzed 21-year-old peed in it.",
    "There's a basketball court above the supreme court. It's known as " + \
        "the highest court in the land.",
    "The medical term for ice cream headaches is Sphenopalatine " + \
        "Ganglioneuralgia.",
    "After Leonardo Da Vinci's death, King Francis I of France hung " + \
        "the 'Mona Lisa' in his bathroom.",
    "Redondo Beach, CA adopted the Goodyear Blimp as the cit's official " + \
        "bird in 1983.",
    "In 2001, Beaver College changed its name to Arcadia in part because " + \
        "anti-porn filters blocked access to the school's website.",
    "Quentin Tarantino played an Elvis impersonator on 'The Golden Girls'.",
    "Wendy's founder Dave Thomas dropped out of high school but picked " + \
        "up his GED in 1993. His GED class voted him most likely to succeed.",
    "Sleeping through winter is hibernation, while sleeping through " + \
        "summer is estivation.",
    "In Qaddafi's compound, Libyan rebels found a photo album filled " + \
        "with pictures of Condoleezza Rice.",
    "Marie Curie's notebooks are still radioactive. Researchers hoping " + \
        "to view them must sign a disclaimer.",
    "William McKinley was on the $500 bill, Grover Cleveland was on the " + \
        "$1,000, and James Madison was on the $5,000.",
    "In 1999, the U.S. government paid the Zapruder family $16 million " + \
        "for the film of JFK's assassination.",
    "Janis Joplin left $2,500 in her will for her friends to 'Have a " + \
        "ball after I'm gone.",
    "In the mid-1960's, Slumber Party Barbie came with a book called " + \
        "'How to Lose Weight.' One of the tips was 'Don't Eat.'",
    "Ben & Jerry originally considered getting into the bagel business, " + \
        "but the equipment was too expensive.",
    "The first webcam watched a coffee pot. It allowed researchers at " + \
        "Cambridge to monitor the coffee situation without leaving their " + \
        "desks.",
    "The last time a Republican was elected President without a Nixon or " + \
        "Bush on the ticket was 1928.",
    "In 1979, Japan offered new British PM Margaret Thatcher 20 'Karate " + \
        "Ladies' for protection at an economic summit. She declined.",
    "Before Google launched Gmail, 'G-Mail' was the name of a free email " + \
        "service offered by Garfield's website.",
    "The final speech by Gregory Peck in 'To Kill a Mockingbird' was " + \
        "done in one take.",
    "In 1980, Detroit presented Saddam Hussein with a key to the city.",
    "Crayola means 'oily chalk.' The name combines 'craie' (French for " + \
        "'chalk') and 'ola'(short for 'oleaginous,' or 'oily').",
    "Bob Ross on his Air Force career. 'I was the guy who makes you " + \
        "scrub the latrine... Who screams at you for being late to work.",
    "In 1973, Mao Zedong told Henry Kissinger that China had an excess " + \
        "of females and offered the U.S. 10 million Chinese woman."
]