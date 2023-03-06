from Poker_game import *
from BlackJack_game import *


deck = Deck(6)
poker = PokerGame()
bj = BlackJackGame()
print(len(poker.deck.cards))
print(len(bj.shoe.cards))
print(poker.draw_board())
poker.deck.reset_deck()
