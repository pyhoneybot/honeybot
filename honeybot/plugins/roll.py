# -*- coding: utf-8 -*-
"""
[roll.py]
Dice_Roll Plugin

[Author]
Glenn Toms

[About]
Will roll dice in the form of 1d4, 10d6 and return total.

[Commands]
>>> .roll <<dice>>
returns Total of dice
"""

try:
    import random
except ImportError:
    print("No module named 'random' found")


class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info):
        try:
            try:
                msgs = info['args'][1:][0].split()
            except Exception as e:
                pass

            if info['command'] == 'PRIVMSG' and msgs[0] == '.roll':
                text = ''
                total = 0
                dice = msgs[1:][0].split('d')
                num_of_die = int(dice[0])
                dice_sides = int(dice[1])
                if num_of_die < 1 or dice_sides < 1:
                    return methods['send'](
                        info['address'],
                        "Can't Roll Negatives")

                if num_of_die > 1000 or dice_sides > 1000:
                    return methods['send'](
                        info['address'],
                        "I'm not rolling that much")

                for n in range(0, num_of_die):
                    rand = random.randint(1, dice_sides)
                    total += rand
                    text += ''.join(f"Dice {n + 1}: {rand}")

                    if num_of_die == 1:
                        return methods['send'](info['address'], text)
                    else:
                        text += ''.join(" / ")

                text += ''.join(f"TOTAL: {total}")
                if num_of_die < 10:
                    return methods['send'](info['address'], text)
                else:
                    return methods['send'](info['address'], f"TOTAL: {total}")
        except Exception as e:
            print('woops plug', e)
