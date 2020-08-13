fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

fcomp = [f.upper() for f in fruits]
print("fcomp:", fcomp, '\n')

fgen = (f.upper() for f in fruits)
print("fgen:", fgen, '\n')
for fruit in fgen:
    print(fruit, end=' ')
print('\n')

print("second loop:")
for fruit in fgen:
    print(fruit, end=' ')
print('\n')

def spam(values):
    for v in values:
        print(v, end=' ')
    print()

spam((f.upper() for f in fruits))


people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

last_names = [p[1] for p in people]
print(last_names)

last_names_gen = (p[1] for p in people if p[3] > '1960')

for last_name in last_names_gen:
    print(last_name)

last_names_gen = ((p[0], p[1]) for p in people if p[3] > '1960')
upper_names = ((n[0], n[1].upper()) for n in last_names_gen)
print(list(upper_names))
