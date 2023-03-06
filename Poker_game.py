from deck import *


class PokerGame:
    def __init__(self):
        self.deck = Deck()
        self.flop = []
        self.turn = ()
        self.river = ()

    def draw_flop(self):
        self.deck.draw_first_card()  # 1st burnt card
        self.flop = self.deck.draw_cards(3)
        return self.flop

    def draw_turn(self):
        self.deck.draw_first_card()  # 2nd burnt card
        self.turn = self.deck.draw_first_card()
        return self.turn

    def draw_river(self):
        self.deck.draw_first_card()  # 3rd burnt card
        self.river = self.deck.draw_first_card()
        return self.river

    def draw_board(self):
        self.draw_flop()
        self.draw_turn()
        self.draw_river()
        return self.flop + [self.turn, self.river]