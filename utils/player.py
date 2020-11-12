from utils.card import Card

import random

class Player():
    def __init__(self, name, cards, history_played, turn_count, number_of_cards):
        self.cards= cards
        self.name = name
        self.history_played = []
        self.turn_count = 0
        self.number_of_cards =0
    
        
    def play(self, name):
        if self.cards!= None
            card_chosen = random.choice(self.cards)
        self.cards.remove(card_chosen)
        self.history_played.append(card_chosen)
        print(name, "have played", card_chosen)

      def get_name(self):
          return self.name


class Deck:
    def __init__(self):
        self.cards = []
    def fill_deck(self):
        i = Symbol()
        j = Card()
        for c in i.icon:
            for n in j.number:
                self.cards.append(n + " " + c)
        random.shuffle(self.cards)




