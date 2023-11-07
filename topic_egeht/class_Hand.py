class Hand:
    
    def __init__(self, name):
        self.cards = []
        self.name = name
        
    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str (card) + "\t"
        else:
            rep = "<emty>"
        return rep
    
    def clear(self):
        self.cards = []
        
    def add(self, card):
        self.cards.append(card)
        
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)