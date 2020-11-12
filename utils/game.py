
from utils.player import Player
from utils.player import Deck

class Board():
    def __init__(self):

        self.active_cards = []
        self.history_allcards_exceptactive=[]
    def start_game(self):

        print("Are you ready The game will start " )
        number_of_players = int(input("How many wants to play "))
        number_cards4eachp = 52 // number_of_players

        for i in range(1, number_of_players + 1):
            player_name = input("Please enter the name of player " + str(i) )
            pname = Player(player_name)
            Deck.distribute(pname, number_cards4eachp, )
            
