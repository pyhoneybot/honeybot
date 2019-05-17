''' poker test '''

import board
import deck
import hand
import player
import pot
#import game_init

deck = deck.Deck()

print(deck.show_deck())
print(deck.nth_card(23))
print(deck.nth_card(23).show_card(), deck.nth_card(23).figure(), deck.nth_card(23).color(), deck.nth_card(23).value())
print(deck.draw_by_number(1).show_card())
print(deck.show_deck())
print(deck.draw_by_name('AS').show_card())
print(deck.show_deck())
print(board.Board(deck.make_board()).show_board())
print(hand.Hand(deck.make_hand()).show_hand())
print(len(deck.show_deck()))
print(deck.show_deck())
print(deck.nth_card(66).show_card())

board = board.Board(deck.make_board())

print(board.show_board())
print(deck.show_deck())
print(board.flop())
print(board.flop1())
print(board.flop2())
print(board.flop3())
print(board.turn())
print(board.river())

hand1 = hand.Hand(deck.make_hand())

print(deck.show_deck())
print(hand1.show_hand())
print(hand1.show_hand_obj()[0].show_card())
print(hand1.show_hand_obj()[0].value())
print(hand1.show_hand_obj()[0].color())
print(hand1.best_five(board))
print(hand1.hand_strength(board))

hand2 = hand.Hand(deck.make_hand())

print(deck.show_deck())
print(hand2.show_hand())
print(hand2.show_hand_obj()[1].show_card())
print(hand2.show_hand_obj()[1].value())
print(hand2.show_hand_obj()[1].color())
print(hand2.best_five(board))
print(hand2.hand_strength(board))

player1 = player.Player(1, 100)

player1.add_hand(hand1)
print(player1.show_player_hand().show_hand())
print(player1.show_player_hand().show_hand_obj()[0].color())
print(player1.show_player_hand().hand_strength(board))
print(str(player1.chips()))
player1.increase_chips(50)
print(str(player1.chips()))
print(player1.position_name())
player1.add_position(4)
print(player1.position_name())

player2 = player.Player(2, 100)

player2.add_hand(hand2)
print(player2.show_player_hand().show_hand())
print(player2.show_player_hand().show_hand_obj()[1].color())
print(player2.show_player_hand().hand_strength(board))
print(str(player2.chips()))
player2.decrease_chips(30)
print(str(player2.chips()))
print(player2.position_name())
player2.add_position(7)
print(player2.position_name())

pot1 = pot.Pot()
print(pot1.show_pot())
pot1.increase_pot(55)
print(pot1.show_pot())
POT = pot.Pot()
print(POT.show_pot())
POT.increase_pot(24)
print(POT.show_pot())
POT.increase_pot(6)
print(POT.show_pot())

print(" ".join([c.show_card() for h in game_init.game[3] for c in h.show_player_hand().show_hand_obj()]))


print(len(game_init.game[0])+len(game_init.game[1])+len(game_init.game[3])*2)

for player in game_init.game[3]:
    print(player.general_name(), player.show_player_hand().show_hand(), player.chips(), \
          player.position_nr(), player.position_name(), \
          player.show_player_hand().hand_strength(board), player.show_player_hand().best_five(board))

game_init.game[0].show_deck()
game_init.game[1].show_board()
for p in game_init.game[3]:
    p.show_player_hand().show_hand()
