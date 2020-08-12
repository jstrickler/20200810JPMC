from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Guido")
d2 = CardDeck("Tim")

print(d1)
print(d1.dealer)
d1.dealer = "Larry"
print(d1.dealer)

try:
    d1.dealer = 123.456
except TypeError as err:
    print(err)
else:
    print(d1.dealer)


d1.shuffle()

print(d1.cards)

for i in range(5):
    print(d1.draw())
print()

print(d1.get_ranks())
print(CardDeck.get_ranks())

d1.whoo(3)

# print(len(d1))
from some_utils import foo, bar, blah
foo()
bar()
print()

j1 = JokerDeck("Jimmy")
print(j1)
j1.shuffle()
print(j1.cards)

print(JokerDeck.mro())
j1.spam()
print(d1)
print(j1)
print(d2)

print(len(d1))
# CardDeck.__len__(d1)
print(len(j1))

print(str(d1))
print(d1)  # same as line 54
print(j1)
print(repr(d1))
print(repr(j1))
