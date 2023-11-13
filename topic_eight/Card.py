class Card:
    
    RANKS = ["A", "2", "v c3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    cards_deck = {"2" : 1, "3" : 2, "4" : 3, "5" : 4, "6" : 5, "7" : 6, "8" : 7, "9" : 8, "10" : 9, "J" : 10, "Q" : 11, "K" : 12, "A" : 13}
    
    # 
    SUITS = [u'\u2660', u'\u2663', u'\u2665', u'\u2666']
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        rep = self.rank + self.suit
        return rep
    
    def Value(self):
        return Card.cards_deck[self.rank]
    