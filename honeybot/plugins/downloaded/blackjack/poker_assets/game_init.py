""" game initialization """

# pylint: disable=E1601, W0612

import card
import deck
import board
import hand
import player
import pot


def init_players(nr_of_players, starting_chips):
    """ players initialization """

    PLAYERS = [player.Player(i, starting_chips) for i in range(nr_of_players)]
    return PLAYERS


def init_game(players, round):
    """ table initialization """

    DECK = deck.Deck()
    BOARD = board.Board(DECK.make_board())
    POT = pot.Pot()
    PLAYERS = players

    for PLAYER in PLAYERS:

        PLAYER.add_hand(hand.Hand(DECK.make_hand()))

    for i in range(len(PLAYERS)):

        PLAYERS[i].add_position(
            (len(PLAYERS) * round + (i - (round - 1))) % len(PLAYERS)
        )

    return DECK, BOARD, POT, PLAYERS


players = init_players(6, 100)
game = init_game(players, 9)

deck = game[0]
board = game[1]
pot = game[2]
players = game[3]
for card in board.get_board():

    print(card.show_card())

print(pot.show_pot())

players[0].show_player_hand().best_five(board)

for player in players:

    print(player.general_name())

    print(
        player.general_name(),
        player.show_player_hand().show_hand()[0].show_card(),
        player.show_player_hand().show_hand()[1].show_card(),
        player.chips(),
        player.position_nr(),
        player.position_name(),
        player.show_player_hand().hand_strength(board),
        str(player.show_player_hand().best_five(board)),
    )

print(len(deck.show_deck()))
