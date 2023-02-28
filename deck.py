import random as rng


class Deck:
    def __init__(self, nb_deck=1):
        self.colors = ["Carreau", "Pique", "Coeur", "Trèfle"]
        self.numbers = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]
        self.cards = []
        self.nb_deck = nb_deck
        self.set_deck(self.nb_deck)
        self.riffle_riffle()

    def set_deck(self, nb_deck):
        for nb in range(nb_deck):
            for color in self.colors:
                for number in self.numbers:
                    self.cards.append((number, color))

    def riffle_riffle(self):
        rng.shuffle(self.cards)

    def draw_first_card(self):
        return self.cards.pop(0)

    def reset_deck(self):
        self.cards[:] = []
        self.set_deck(self.nb_deck)
        self.riffle_riffle()
        return print("*Riffle Riffle* Deck reconstitué et mélangé")

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
