from deck import *


class PokerGame(Deck):
    def __init__(self):
        super().__init__()
    
    def draw_poker_board(self):
        if self.nb_deck == 1:
            self.draw_first_card()  # 1st burnt card
            flop = [self.draw_first_card(), self.draw_first_card(), self.draw_first_card()]
            self.draw_first_card()  # 2nd burnt card
            turn = self.draw_first_card()
            self.draw_first_card()  # 3rd burnt card
            river = self.draw_first_card()
            return flop + [turn, river]
        return None