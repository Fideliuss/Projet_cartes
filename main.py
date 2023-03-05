from Poker_game import *
from BlackJack_game import *


deck = Deck(6)
poker = PokerGame()
bj = BlackJackGame()
print(len(poker.cards))
print(len(bj.cards))
print(poker.draw_board())
poker.reset_deck()
