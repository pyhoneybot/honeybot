# -*- coding: utf-8 -*-
"""
[quote.py]
Quotes Plugin

[Author]
German Corpaz

[About]
Sends a random quote on request

[Commands]
>>> .quote
returns a random quote
"""
import random


class Plugin:
    def __init__(self):
        pass

    def quote(self):
        quotes = [
            "You know you’re in love when you can’t fall asleep because reality is finally better than your dreams.",
            "Life is what happens when you’re busy making other plans.",
            "Get busy living or get busy dying.",
            "Twenty years from now you will be more disappointed by the things that you didn’t do than by the ones you did do.",
            "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart.",
            "Great minds discuss ideas; average minds discuss events; small minds discuss people.",
            "Keep love in your heart. A life without it is like a sunless garden when the flowers are dead.",
            "A successful man is one who can lay a firm foundation with the bricks others have thrown at him.",
            "It is during our darkest moments that we must focus to see the light.",
            "Those who dare to fail miserably can achieve greatly.",
            "Try to be a rainbow in someone's cloud.",
            "I can’t give you a sure-fire formula for success, but I can give you a formula for failure: try to please everybody all the time.",
            "Find a place inside where there's joy, and the joy will burn out the pain.",
            "He that falls in love with himself will have no rivals.",
            "Nothing is impossible, the word itself says 'I'm possible'!",
            "It is hard to fail, but it is worse never to have tried to succeed.",
            "Don't judge each day by the harvest you reap but by the seeds that you plant.",
            "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment.",
            "I’m a success today because I had a friend who believed in me and I didn’t have the heart to let him down.",
            "The only thing necessary for the triumph of evil is for good men to do nothing.",
            "Love yourself first and everything else falls into line. You really have to love yourself to get anything done in this world.",
            "One of the most beautiful qualities of true friendship is to understand and to be understood.",
            "Let us always meet each other with smile, for the smile is the beginning of love.",
            "Where there is love there is life.",
            "Challenges are what make life interesting and overcoming them is what makes life meaningful.",
            "Love is composed of a single soul inhabiting two bodies.",
            "Love is a serious mental disease.",
            "Do not go where the path may lead, go instead where there is no path and leave a trail.",
            "Our greatest fear should not be of failure… but of succeeding at things in life that don’t really matter.",
            "Success is not final, failure is not fatal: it is the courage to continue that counts.",
            "Remember that the happiest people are not those getting more, but those giving more.",
            "Do all things with love.",
            "The only impossible journey is the one you never begin.",
            "Blessed are the hearts that can bend; they shall never be broken.",
            "It is our choices, that show what we truly are, far more than our abilities.",
            "Love isn't something you find. Love is something that finds you.",
            "Only put off until tomorrow what you are willing to die having left undone.",
            "In three words I can sum up everything I've learned about life: it goes on.",
            "If you want to be happy, be.",
            "Change your thoughts and you change your world.",
            "Education is the most powerful weapon which you can use to change the world.",
            "Today you are you! That is truer than true! There is no one alive who is you-er than you!",
            "The future belongs to those who believe in the beauty of their dreams.",
        ]

        return "{}".format(random.choice(quotes))

    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info["args"][1:]
            if info["command"] == "PRIVMSG" and msgs[0] == ".quote":
                methods["send"](info["address"], Plugin.quote(self))
        except Exception as e:
            print("error quote plugin", e)
