from deck import *


class PokerGame(Deck):
    def __init__(self):
        super().__init__(1)
        self.flop = []
        self.turn = ()
        self.river = ()

    def draw_flop(self):
        self.draw_first_card()  # 1st burnt card
        self.flop = self.draw_cards(3)
        return self.flop

    def draw_turn(self):
        self.draw_first_card()  # 2nd burnt card
        self.turn = self.draw_first_card()
        return self.turn

    def draw_river(self):
        self.draw_first_card()  # 3rd burnt card
        self.river = self.draw_first_card()
        return self.river

    def draw_board(self):
        self.draw_flop()
        self.draw_turn()
        self.draw_river()
        return self.flop + [self.turn, self.river]