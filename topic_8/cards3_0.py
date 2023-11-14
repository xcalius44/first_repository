from Card import Card
from Deck import Deck
from Hand import Hand

class Unprintabale_Card(Card):

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
            rep ="XX"
        return rep
    
    def flip(self):
        self.is_fase_up =  not self.is_fase_up
        
class Player(Hand):
    
    def __init__(self, name):
        super().__init__()
        self.name = name
        
def main():
    names_but_not_object = [str(i) for i in input().split()]
    list_players = Deck()
    players: [Player] = [Player(str(i)) for i in names_but_not_object]
    list_players.populate()
    list_players.shuffle()
    value = [0] * len(players)
    count = [0] * len(players)
    ansver = [0] * len(players)
    decks_end = 52 // len(names_but_not_object) 
    count_max_ruond = 0
    a = 0
    # Numbe of rounds
    for i in range(int(input())):
        if decks_end == count_max_ruond:
            print("end of deck")
            break 
        list_players.deal(players, per_hand = 1)
        for i in range(len(players)):
            count[i] = players[i].cards[0].Value()
        a = count.index(max(count))
        ansver[a] += 1
        for i in range(0, len(players)):
            print(names_but_not_object[i], ":", ansver[i],"and the card is:", players[i])
        for i in range(0, len(players)):
            players[i].clear()

main()
    
        

