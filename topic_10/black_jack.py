import Cards, Games

min_bet = 5

class BJ_Card(Cards.Position_able_Card):
    ACE_VALUE = 1
    
    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJ_Deck(Cards.Deck):
    
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))

class BJ_Hand(Cards.Hand):
    
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def __str__(self):
        rep = self.name + ":\t" + super().__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep
    
    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None
    
        t = 0
        contains_ase = False
        for card in self.cards:
            t += card.value
            if card.value == BJ_Card.ACE_VALUE:
                contains_ase = True
        if contains_ase and t <= 11:
            t += 10
        return t
    
    def is_busted(self):
        return self.total > 21
    
class BJ_Player(BJ_Hand):
    
    def __init__(self, name, dolors):
        super().__init__(name)
        self.dolors = dolors
    
    def is_hitting(self):
        response = Games.ask_yes_no("\n" + self.name +
                ", taking more cards: ")
        return response == "y"
    
    def bust(self):
        print(self.name, "excluded.")
        self.lose()
    
    def fold(self):
        print(self.name, "fold.")
    
    def lose(self):
        print(self.name, "lose.")
    
    def win(self):
        self.dolors += 2 * self.bet_value
        print(self.name, "win.")
    
    def push(self):
        self.dolors += self.bet_value
        print(self.name, "play draw.")
    
    def bet(self ,bet_value):
        if bet_value > self.dolors:
            return False
        self.bet_value = bet_value
        self.dolors -= self.bet_value
        return bet_value
    
    def fold(self):
        self.dolors += int(self.bet_value * 0.5)
        self.clear()
        print(self.name, "fold")
    
    def is_fold(self):
        return len(self.cards) == 0
    
class BJ_Dealer(BJ_Hand):
    
    def is_hitting(self):
        return self.total < 7
    
    def bust(self):
        print(self.name, "excluded.")
    
    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()

class BJ_Game:
    
    def __init__(self, players):
        self.players = []
        for name, dolors in players.items():
            player = BJ_Player(name,dolors)
            self.players.append(player)
        
        self.dealer = BJ_Dealer("Dealer")
        
        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()
    
    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp
    
    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()
    
    def __betting(self):
        for player in self.players.copy():
            if player.dolors < min_bet:
                self.players.remove(player)
                print("Player ", player.name, " delete with ", player.dolors, " dolors")
                continue
            bet_value = Games.ask_number(f"Your bet {player.name}, money {player.dolors}:", min_bet, player.dolors)
            player.bet(bet_value)
    
    def __ask_fold(self, player):
        answer = Games.ask_yes_no(f"{player} do you want fold")
        if answer == "y":
            player.fold()
            return True
        return False
        
    def play(self):
        
        if len(self.deck.cards) < (len(self.players) + 1)* 2:
            self.add_new_deck()
        
        self.deck.deal(self.players + [self.dealer],
                       per_hand = 2)
        self.dealer.flip_first_card()
        
        for player in self.players:
            print(player)
        print(self.dealer)
        
        self.__betting()
        for player in self.players:
            self.__ask_fold(player)
            
        for player in self.players:
            self.__additional_cards(player)
        
        self.dealer.flip_first_card()

        if not self.still_playing:
            print(self.dealer)
        else:
            print(self.dealer)
            self.__additional_cards(self.dealer)
        if self.dealer.is_busted():
            for player in self.still_playing:
                player.win()
        else:
            for player in self.still_playing:
                if player.total > self.dealer.total:
                    player.win()
                elif player.total < self.dealer.total:
                    player.lose()
                elif ask_yes_no("are you playing?"):
                    player.fold()
                else:
                    player.push()
        for player in self.players:
            player.clear()
        self.dealer.clear()

def main():
    print("\t\tgame black-jack")
    
    players = {}
    number = Games.ask_number("how many players (1 - 7): ",
                              low = 1, high = 7)
    for i in range(number):
        name = input("players name " + str(i + 1) + ": ")
        dolors = Games.ask_number(f"{name} money: ",min_bet ,min_bet * 100)
        players[name] = dolors
    print()

    game = BJ_Game(players)
    again = None
    while again != "n":
        game.play()
        again = Games.ask_yes_no("\nplay again")
main()
