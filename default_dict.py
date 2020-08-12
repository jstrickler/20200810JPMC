from collections import defaultdict

def zero():
    return 0

dd = defaultdict(zero)

dd['a'] = 25
dd['wombat'] = 3
dd['koala'] = 22
print(dd['koala'])
print(dd['JPMC'])

x = defaultdict(list)

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

fruit_letters = defaultdict(list)
for fruit in fruits:
    first_letter = fruit[0]
    fruit_letters[first_letter].append(fruit)
print(fruit_letters, '\n')

for letter, flist in fruit_letters.items():
    print(letter, flist)
