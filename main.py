import random as rng


class Deck:
    def __init__(self):
        self.colors = ["Carreau", "Pique", "Coeur", "Tréfle"]
        self.numbers = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]
        self.paquet = []
        self.set_deck()
        self.riffle_riffle()

    def set_deck(self):
        for color in self.colors:
            for number in self.numbers:
                self.paquet.append((number, color))

    def riffle_riffle(self):
        rng.shuffle(self.paquet)

    def draw_card(self):
        return self.paquet.pop()

    def reset_deck(self):
        self.paquet[:] = []
        self.set_deck()
        self.riffle_riffle()
        return print("*Riffle Riffle* Paquet reconstitué et mélangé")

    def draw_board(self):
        self.draw_card()
        flop = [self.draw_card(), self.draw_card(), self.draw_card()]
        self.draw_card()
        turn = self.draw_card()
        self.draw_card()
        river = self.draw_card()
        return flop + [turn, river]


deck = Deck()
j1 = [deck.draw_card(), deck.draw_card()]
j2 = [deck.draw_card(), deck.draw_card()]
j3 = [deck.draw_card(), deck.draw_card()]
board = deck.draw_board()
print(board)
