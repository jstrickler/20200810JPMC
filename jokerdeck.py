from carddeck import CardDeck

class GameThing():
    def spam(self):
        print("hello from GameThing.spam()")

class JokerDeck(GameThing, CardDeck):

    def _make_deck(self):
        super()._make_deck()
        j1 = 1, 'Joker'
        j2 = 2, 'Joker'
        self._cards.append(j1)
        self._cards.append(j2)
