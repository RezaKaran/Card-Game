import random
class Symbol:
    def __init__(self):

        self.icon = {"Spade": "Black" , "Heart": "Red", "Diamond": "Red", "Club": "Black"}


class Card(Symbol):
    def __init__(self):

        self.number=["Ace", "Jack","Queen","King","2","3","4","5","6","7","8""9","10"]

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
        i = self.cards.pop()
    def distribute(self,np):
        print("Are you ready The game will start ")
        number_of_cards = 52 // self.number_of_players
        print(number_of_cards)






d=Deck()
d.fill_deck()