from Poker_game import *
from BlackJack_game import *


deck = Deck(6, False)
poker = PokerGame()
bj = BlackJackGame()
print(len(poker.cards))
print(len(bj.cards))
print(deck.cards)
