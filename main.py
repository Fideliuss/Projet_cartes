from Poker_game import *
from BlackJack_game import *


deck = Deck(6)
poker = PokerGame()
bj = BlackJackGame()
print(len(poker.cards))
print(len(bj.cards))
print(poker.draw_board())
QFR = []
count = 0
while QFR != [('10', 'Trèfle'), ('Valet', 'Trèfle'), ('Dame', 'Trèfle'), ('Roi', 'Trèfle'), ('As', 'Trèfle')]:
    QFR = poker.draw_board()
    count += 1
    poker.reset_deck()
print(count)
