"""
[quote.py]
Self Trivia Plugin

[Author]
Angel Jimenez

[About]
Returns a private trivia question

[Commands]
>>> .selfTrivia
returns a random question
Currently working on adding multiple choice and a timer reveal.
"""
import random


class Plugin:
    def __init__(self):
        pass

    def trivia(self):
        questions = [
            "Venetian painter Jacopo Robusti was " + "better known by what name?",  # Tintoretto
            "In what town was FDR's " + '"Little White House" located?',  # Warm Springs, Georgia
            "What is the middle color in a rainbow?",  # Green
            "Who was the legendary Benedictine monk " + "who invented champagne?",  # Dom Perignon
            "Great Whites and Hammerheads are what type of animals?",  # Sharks
            "In which year was Alaska sold " + "to the U.S.?",  # In the year 1867
            "Which famous nurse was known as “The Lady Of The Lamp”"
            + " during the crimean war?",  # Florence Nightingale
            "Where did the game of badminton originate?",  # It originated in the British
            # era in the Indian city of Pune (or Poona, as it was known back then)
            "Name the largest freshwater lake in the world?",  # Lake Superior
            "Who invented the telephone?",  # Alexander Graham Bell
            "Who invented the rabies vaccination?",  # Louis Pasteur
            "Name the world’s biggest island.",  # Greenland
            "What is the diameter of Earth?",  # 8,000 miles
            "What’s the coloured part of the human eye called?",  # The iris
            "How many holes are there on a golf course?",  # Eighteen
            "Which word goes before vest, beans and quartet?",  # String
            "Name the world’s largest ocean.",  # Pacific
            "What is the world’s longest river?",  # Amazon
            "By what name are the young of frogs and toads known?",  # Tadpoles
            "What is someone who shoes horses called?",  # A Farrier
            "Where would you find the Sea of Tranquility?",  # The Moon
            "What item of clothing was named after its " + "Scottish inventor?",  # A Mackintosh
            "Who composed the Minute Waltz?",  # Frederic Chopin
            "Who was the first actor to have played the role of James Bond "
            + "in the movie series?",  # Sir Sean Connery
            "Which is the highest mountain in Africa?",  # Mount Kilimanjaro
            "If you boil water you get?",  # Steam
            "How many grams are there in a kilogram?",  # 1,000
            "Where did the Olympic Games originate?",  # Greece
            "How many rings make up the symbol of the Olympic Games?",  # Five
            "Who is the only athlete to win the Olympic marathon twice "
            + "and in successive Olympic games?",  # Abebe Bikila.
            "Who improved the design of the modern-day "
            + "incandescent light bulb?",  # Thomas Edison.
            "By what title were the leaders of ancient Egypt known?",  # Pharoah.
            "Which was the country that first made the use of paper money?",  # China.
            "Which four British cities have underground "
            + "rail systems?",  # Liverpool, Glasgow, Newcastle and London.
            "What % of an egg’s weight is the shell?",  # 12%.
            "Who was the 16th president of the United States?",  # Abraham Lincoln.
            "What kind of weapon is a falchion?",  # A sword.
            "What is the capital city of Spain?",  # Madrid.
            "Which city is the Palace of Versailles nearest to?",  # Paris
            "What is the antonym of the word " + "‘synonym’?",  # Of course, it is ‘antonym’ itself!
            "What is the oldest film ever made, and "
            + "when was it made?",  # Roundhay Garden Scene made in 1888.
            "When was the first atomic bomb " + "dropped?",  # It was dropped on August 6, 1945.
            "Who founded the first public library in the U.S.?",  # Benjamin Franklin.
            "Who is known as the Father of the Modern Olympics?",  # Pierre de Coubertin.
            "Which country is Prague in?",  # Czech Republic.
            "Who was the first gymnast to be awarded a perfect score "
            + "of 10 at the Olympics?",  # Nadia Comaneci.
            "Where would you find the world’s most ancient "
            + "forest?",  # Daintree Forest north of Cairns, Australia.
            "If you suffer from arachnophobia, which animal " + "are you scared of?",  # Spiders.
            "Which famous ocean liner sank on her first voyage in 1912?",  # The Titanic.
            "Name the only heavyweight boxing champion to finish his career of 49 "
            + "fights without ever having been defeated?",  # Rocky Marciano.
            "What is another word for lexicon?",  # Dictionary.
            "Which actress has won the most "
            + "Oscars?",  # Katharine Hepburn, with 4 Oscars and 12 nominations.
            "What is a brontosaurus?",  # A dinosaur.
            "What is the name of the pirate in Peter Pan?",  # Captain Hook.
            "According to legend, who led a gang of merry outlaws in "
            + "Sherwood Forest in Nottingham, England?",  # Robin Hood.
            "What’s the name of the town where The Flintstones live?",  # Bedrock.
            "What is the name of Shrek’s wife?",  # Princess Fiona.
            "Things fall when you drop them because of?",  # gravity
            "Name the seventh planet from the sun.",  # Uranus.
            "Name the three primary colours.",  # Red, yellow and blue.
            "A place to see lots of animals?",  # Zoo.
            "Which English town was a forerunner of the Parks Movement and "
            + "the first city in Europe to have a street tram system?",  # Birkenhead.
            "Which planet is closest to our sun?",  # Mercury.
            "If you freeze water you get?",  # Ice
            "How many legs does a spider have?",  # Eight.
            "He’s “smarter than the average bear”, but what’s the name of "
            + "the most famous resident of Jellystone Park?",  # Yogi Bear.
            "What is the common name for calcium carbonate?",  # Chalk.
            "What holds school supplies and children also "
            + "carry them on their backs?",  # Backpacks.
            "What colour is a stop sign?",  # Red and white.
            "What vehicle runs on a track and blows a whistle?",  # A train.
            "In needlework, what does UFO refer to?",  # An unfinished object.
            "Tired people need?",  # Sleep
            "Is the planet Jupiter larger or smaller than the Earth?",  # Larger.
            "Is a dolphin a mammal?",  # Yes.
            "What do many children ride on to go to school?",  # A school bus.
            "Thirsty people need?",  # Water.
            "What do you wear on your head?",  # Hat.
            "Who painted the Mona Lisa?",  # Leonardo da Vinci.
        ]

        return f"{random.choice(questions)}"

    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info["args"][1:]
            if info["command"] == "PRIVMSG" and msgs[0] == ".selfTrivia":
                methods["send"](info["address"], Plugin.trivia(self))
        except Exception as e:
            print("Error with Self Trivia Plugin!", e)
