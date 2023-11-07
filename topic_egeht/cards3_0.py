import class_card
from class_card import Card
import class_deck
from class_deck import Deck
import class_Hand
from class_Hand import Hand

class Unpritabale_Card(Card):

    def __str__(self):
        return "error"
class Positionabele_Card(Card):
    def __init__(self, rank, suit, fase_up = True):
        super().__init__(rank, suit)
        self.is_fase_up = fase_up
        
    def __str__(self):
        if self.is_fase_up:
            rep = super().__str__()
        else:
            rep ="XX"
        return rep
    def flip(self):
        self.is_fase_up =  not self.is_fase_up
def main():
    per = [str(i) for i in input().split()]
    list_pet: [Deck] = [Deck(str(i)) for i in per]
    list_pet_hand: [Hand] = [Hand(str(i)) for i in per]
    count = [0] * len(list_pet)
    decks = []
    for i in range(int(input())):
        count[i] = list_pet[i]
        list_pet[i].deal(list_pet_hand, per_hand = 1)
        for i in range(len(list_pet)):
            print(count[i], ":", list_pet[i])
main()
    
        

