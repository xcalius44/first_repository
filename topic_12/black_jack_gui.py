import easygui as gui

import Cards_gui
import Games_gui


TITLE = "Блек Джек"
ICON = "topic_12/black-jack.png"


class BJ_Card(Cards_gui.Position_able_Card):

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


class BJ_Deck(Cards_gui.Deck):

    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))


class BJ_Hand(Cards_gui.Hand):

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
        contains_ace = False
        for card in self.cards:
            t += card.value
            
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True
        
        if contains_ace and t <= 11:
            t += 10
        return t

    def is_busted(self):
        return self.total > 21

    def show_message(self, message):
        gui.buttonbox(message, choices=["Ok"], images=self.card_images, title=TITLE)


class BJ_Player(BJ_Hand):

    def is_hitting(self):
        response = gui.buttonbox(
            f"{self.name}, братимете ще карти ({self.total}) ?",
            choices=["Yes", "No"],
            images=self.card_images,
        )
        return response == "Yes"

    def bust(self):
        self.show_message(self.name + " перебрав(ла).")

    def lose(self):
        self.show_message(self.name + " програв(ла).")

    def win(self):
        self.show_message(self.name + " виграв(ла).")

    def push(self):
        self.show_message(self.name + " зіграв(ла) з дилером внічию.")


class BJ_Dealer(BJ_Hand):

    def is_hitting(self):
        return self.total < 11

    def bust(self):
        self.show_message(self.name + " перебрав.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()


class BJ_Game:

    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

        self.dealer = BJ_Dealer("Дилер")

        self.deck = BJ_Deck()
        self.deck.add_new_deck()

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
            if player.is_busted():
                player.bust()

    def play(self):
        self.deck.deal(self.players + [self.dealer], per_hand=2)
        self.dealer.flip_first_card()
        self.dealer.show_message("Починаємо гру, Дилер оримав такі карти:")

 
        for player in self.players:
            self.__additional_cards(player)
        self.dealer.flip_first_card()

        if not self.still_playing:
            self.dealer.show_message(self.dealer.name + " переміг!")
        else:

            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():

                for player in self.still_playing:
                    player.win()
            else:
                self.dealer.show_message(
                    f"{self.dealer.name} набрав додаткові карти {self.dealer.total}."
                )

                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()


        for player in self.players:
            player.clear()
        self.dealer.clear()


def main():
    gui.msgbox("Ласкаво просимо до гри Блек-джек!", TITLE, image=ICON)

    names = []
    number = Games_gui.ask_number("Скільки всього гравців? (1 - 7): ", low=1, high=7)
    if number is None:
        exit()
    fields = ["Гравець " + str(i + 1) for i in range(number)]
    names = gui.multenterbox("Введіть імена гравців", TITLE, fields=fields, values=fields)
    if names is None:
        exit()
    game = BJ_Game(names)

    again = True
    while again:
        game.play()
        again = Games_gui.ask_yes_no("Бажаєте зіграти ще раз", TITLE)


main()