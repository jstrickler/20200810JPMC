import random

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self, dealer):
        self._dealer = dealer
        self._make_deck()

    def _make_deck(self):
        self._cards = []  # list
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    @property
    def cards(self):
        return self._cards

    @property
    def dealer(self):
        return self._dealer

    @dealer.setter
    def dealer(self, value):
        if isinstance(value, str):
            self._dealer = value
        else:
            raise TypeError("Dealer must be a string")

    @classmethod
    def get_ranks(cls):
        return cls.RANKS

    @staticmethod
    def whoo(count):
        print("WHOOOOOOOOO!" * count)

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return "{}({},{})".format(
            my_name, self.dealer, len(self)
        )

    def __repr__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return '{}("{}")'.format(
            my_name, self.dealer
        )
