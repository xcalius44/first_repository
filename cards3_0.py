from class_card import Card
from class_deck import Deck
from class_Hand import Hand

class Unpritabale_Card(Card):

    def __str__(self):
        return "error"

class Positionabele_Card(Card):
    
    def __init__(self, rank, suit, is_fase_up = True):
        super().__init__(rank, suit)
        self.is_fase_up = is_fase_up
        
    def __str__(self):
        if self.is_fase_up:
            rep = super().__str__()
        else:
            rep = "XX"
        return rep
    
    def flip(self):
        self.is_fase_up =  not self.is_fase_up
        
class player(Hand()):
    
    def __init__(self, name):
        self.name = name
        
def main():
    
    per = [str(i) for i in input().split()]
    # names but not objekt
    list_plears = Deck()
    list_pet_hand: [player] = [player(str(i)) for i in per]
    count = [0] * len(list_plears)
    decks = []
    for i in range(int(input())):
        count[i] = list_plears[i]
        list_plears[i].deal(list_pet_hand, per_hand = 1)
        for i in range(len(list_plears)):
            print(count[i], ":", list_plears[i])

main()
    
        

