
from utils.card import Card
from utils.card import Deck
from utils.game import Board
import random

class Player():
    def __init__(self, name,number_of_cards):
        self.name = name
        self.history_played = []
        self.turn_count = 0
        self.number_of_cards = number_of_cards

    def play(self):
        for i in self.number_of_cards:
            card = random.choice(self.cards)
            self.history_played.append(card)



