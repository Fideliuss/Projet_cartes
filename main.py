import random


class Cartes:
    def __init__(self):
        self.color = ["Carreau", "Pique", "Coeur", "Tréfle"]
        self.number = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]

    def creer_carte(self):
        return random.choice(self.color), random.choice(self.number)
