"""
[birthparadox.py]
Bithday Paradox Plugin

[Author]
Paulo Ferraz

[About]
show the probability that two or more people
have the same birthday in the given group.

[Commands]
>>> .birth <<number>>
returns the birthday matches and probability in % of a group.
"""
import datetime
import random


class Plugin:
    """
    Show the high probability that two or more people
    have the same birthday, even in a small group!
    """

    def __init__(self):
        pass

    """
    AUXILIARY FUNCTIONS
    """

    def calc_probability(self, num):
        """
        Calculate the match probability in %
        """
        soma = 366
        ano = 366
        for i in range(num - 1):
            soma *= ano - (i + 1)
        perc = round((1 - (soma / 366**num)) * 100, 2)
        return perc

    def create_birthdays(self, num_people):
        """
        Simulate some birthdays in a group
        """
        start_date = datetime.date(1970, 1, 1)
        birthday_group = []
        while True:
            birthday_group.clear()
            for i in range(num_people):
                birth = start_date + datetime.timedelta(random.randint(0, 366))
                birthday_group.append(birth.strftime("%B, %d"))
            if len(birthday_group) != len(set(birthday_group)):
                break
        return birthday_group

    def find_match(self, birthday_group):
        """
        Try to to find a match in a group
        """
        matches = []
        dates = ()
        for i, first in enumerate(birthday_group):
            for j, second in enumerate(birthday_group[i + 1 :]):
                if first == second:
                    matches.append(first)
        dates = set(matches)
        return dates

    def help(self, methods, info):
        """
        Presentation and guidance function
        """
        title = "THE BIRTHDAY PARADOX"
        statement = (
            "It's the high probability that two or more people have the same birthday, even in a"
            " small group!"
        )
        use = (
            "Use: .birth <num>, where num is the size of the group of people to calculate"
            " probability."
        )
        methods["send"](info["address"], title)
        methods["send"](info["address"], statement)
        methods["send"](info["address"], use)

    def run(self, incoming, methods, info, bot_info):
        """
        Main function
        """
        try:
            params = info["args"][1:][0].split()
            if len(params) <= 1:
                if info["command"] == "PRIVMSG" and params[0] == ".birth":
                    Plugin.help(self, methods, info)
            if info["command"] == "PRIVMSG" and params[1]:
                if params[1].isdecimal() and int(params[1]) >= 5:
                    num = int(params[1])
                    perc = Plugin.calc_probability(self, num)
                    group = Plugin.create_birthdays(self, num)
                    dates = "; ".join(Plugin.find_match(self, group))
                    methods["send"](
                        info["address"],
                        "In this simulation, we found these [{}] matches, but on average, ".format(
                            dates
                        ),
                    )
                    methods["send"](
                        info["address"],
                        "this group has {} % of probability of having one or more people "
                        "with the same birthday!".format(perc),
                    )
                else:
                    methods["send"](info["address"], "Please, inform integer value >= 5 only!")
        except Exception as e:
            print("woops!! birthparadox plugin error ", e)
