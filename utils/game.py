import time
from utils.player import Player
from utils.card import Card
from utils.card import Deck
class Board():
    def __init__(self):
        self.number_of_players = int(input("How many wants to play "))
        self.active_cards = []
        self.history_allcards_exceptactive=[]
    def start_game(self):

        print("Are you ready The game will start " )
        self.number_cards4eachp = 52 // self.number_of_players
        print(self.number_cards4eachp)
        for i in self.number_of_players:
            Player(input("please write your name"))
        Board().play(self.number_cards4eachp)





b=Board()
b.start_game()

