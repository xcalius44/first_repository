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

class Unprintabale_Card(Card):

    def __str__(self):
        return "<error_printing>"

class Positionable_Card(Card):
    
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

class Hand:
    
    def __init__(self):
        self.cards = []
        
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
    
class Deck(Hand):

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))
    
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    
    def add_new_deck(self):
        self.populate()
        self.shuffle()
        
    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("end of deck")
                    
if __name__ == "__main__":
    print("You have started the cards module, "
        "and not imported it (import cards).")
    
    print("Module testing. \n")
    
    card1  = Card("T", Card.SUITS[0])
    
    card2  = Unprintabale_Card("T", Card.SUITS[1])
    
    card3  = Positionabele_Card("T", Card.SUITS[2])
    
    print("Card object:", card1) 
    
    print("Unprintable_Card object:", card2)
    
    print("Positionable_Card object:", card3)
          
    card3.flip()

    print("Turning the Positionable_Card object:", card3)
    
    deck1  = Deck()

    print("\nNew deck created:", deck1)

    deck1.populate()

    print("Cards appeared in the deck:", deck1, sep="\n")

    deck1.shuffle()

    print("Deck shuffled:", deck1, sep="\n")

    hand1 = Hand()
    
    hand2 = Hand()

    deck1.deal (hands = (hand1, hand2), per_hand = 5)

    print("\n5 cards dealt.")

    print("handl:", hand1)

    print("hand2:", hand2)

    print("Left in deck:", deck1, sep="\n")

    deck1.clear()

    print("Deck cleared:", deck1)


