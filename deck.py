import random as rng


class Deck:
    def __init__(self, nb_deck=1, shuffled=True):
        self.colors = ["Carreau", "Pique", "Coeur", "Trèfle"]
        self.numbers = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]
        self.cards = []
        self.nb_deck = nb_deck
        self.set_deck(self.nb_deck)
        if shuffled:
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

    def draw_random_card(self):
        return self.cards.pop(rng.randint(0, len(self.cards)))

    def draw_cards(self, n):
        cards = []
        for i in range(n):
            cards.append(self.cards.pop(0))
        return cards

    def reset_deck(self):
        self.cards[:] = []
        self.set_deck(self.nb_deck)
        self.riffle_riffle()
