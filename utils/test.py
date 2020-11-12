import random

class Player(object):
    def __init__(self,name):
        self.name = name
        self.hand = []

    def get_name(self):
        return self.name

    def add_card_to_hand(self,card):
        if card != None:
            self.hand.append(card)
    def remove_card_from_hand(self, card):
            self.hand.remove(card)
    def hand_size(self):
        return len(self.hand)

class CardDeck(object):
    def __init__(self):
        hearts = "2H, 3H , 4H , 5H, 6H, 7H, 8H, 9H"
        diamonds = "2D, 3D, 4D, 5D, 6D, 7D, 8D, 9D "
        spades = "2S, 3S, 4S, 5S, 6S, 7S, 8S, 9S"
        clubs = "1C, 2C, 3C, 4C, 5C, 6C, 7C, 8C, 9C"

        self.deck=hearts.split(',')+diamonds.split(',')+spades.split(',')

    def get_card(self):
        if len(self.deck) < 1:
            return None
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card
    def compare_cards (self, card1, card2):
        if card1[0] > card2[0]:
            return card1
        elif card1[0] < card2[0]:
            return card2
        elif card1[0] > card2[1]:
            return card1
        else:
            return card2


name1= input ("what is your name player 1")
player1=Player(name1)
name2= input ("what is your name player 2")
player2= Player(name2)
deck= CardDeck()

while True:
    player1_card= deck.get_card()
    player2_card = deck.get_card()
    player1.add_card_to_hand(player1_card)
    player2.add_card_to_hand(player2_card)

    if player1_card == None or player2_card ==None:
        print("Game over. No more cards in the deck")
        print(name1, "has", player1.hand_size())
        print(name2, "has", player2.hand_size())
        print("who won")
        if player1.hand_size() > player2.hand_size():
            print(name2, "wins ")
        elif player1.hand_size() < player2.hand_size():
            print(name1, "wins")
        else:
            print("A tie")
        break

    else:
        print(name1, ":", player1_card)
        print(name2, ":",player2_card)
        if deck.compare_cards(player1_card, player2_card) == player1_card:
            player2.add_card_to_hand(player1_card)
        else:
            player1.add_card_to_hand(player2_card)
            player2.remove_card_from_hand(player2_card)






