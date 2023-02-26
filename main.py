import random as rng


class Deck:
    def __init__(self):
        self.colors = ["Carreau", "Pique", "Coeur", "Tréfle"]
        self.numbers = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]
        self.paquet = []
        self.nb_cards = 0
        self.creer_paquet()
        self.riffle_riffle()

    def creer_paquet(self):
        for color in self.colors:
            for number in self.numbers:
                self.paquet.append(f"{number} de {color}")

    def riffle_riffle(self):
        rng.shuffle(self.paquet)

    def draw_random_card(self):
        rand_index = rng.randint(0, 51)
        return self.paquet.pop(rand_index)


