""" Cards Game  """
# m


class Card(object):
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["C", "D", "H", "S"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        name = self.rank + self.suit
        return name


class Unprintable_card(Card):
    def __str__(self):
        return "unprintable"


class Positionable_card(Card):
    def __init__(self, rank, suit, face_is_up=True):
        super(Positionable_card, self).__init__(rank, suit)

        self.face_is_up = face_is_up

    def __str__(self):
        if self.face_is_up == True:
            name = self.rank + self.suit
            return name
        else:
            return "XX"

    def flip(self):
        self.face_is_up = not self.face_is_up


class Hand(object):
    def __init__(self, name):
        self.cards = []
        self.name = name

    def give(self, card, other_hand):
        other_hand.add(card)
        self.cards.remove(card)

    def add(self, card):
        self.cards.append(card)

    def clear(self):
        self.cards = []

    def __str__(self):
        txt = self.name + "'s Hand is: \n"
        for card in self.cards:
            txt += str(card) + "\t"

        if txt == "":
            return "<empty>"
        else:
            return txt


class Deck(Hand):
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Positionable_card(rank, suit))

    def shuffle(self):
        import random

        random.shuffle(self.cards)

    def deal(self, players, per_hand=1):
        for rounds in range(per_hand):
            for player in players:
                top_card = self.cards[0]
                self.give(top_card, player)


if __name__ == "__main__":
    print(
        "You are executing the module"
        + " separately. Please import it"
        + " to another program."
    )


# root
