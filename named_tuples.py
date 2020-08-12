from collections import namedtuple
#  Jane Dough Chicago

jane_list = ["Jane", "Dough", "Chicago"]
jane_tuple = "Jane", "Dough", "Chicago"
jane_dict = {'first_name': "Jane", 'last_name': 'Dough', 'city': 'Chicago'}

print(jane_list[2], jane_tuple[2], jane_dict['city'])

Person = namedtuple("Person", "first_name last_name city")

jane_namedtuple = Person("Jane", "Dough", "Chicago")
print(jane_namedtuple[0], jane_namedtuple.first_name)

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

Nerd = namedtuple("Nerd", 'first_name last_name product dob')
nerds = []
for first_name, last_name, product, dob in people:
    nerd = Nerd(first_name, last_name, product, dob)
    nerds.append(nerd)

print(nerds, '\n')

for nerd in nerds:
    print(nerd.last_name, nerd.product)

x = nerds[0]
print(x)

y = x._replace(first_name='Bill')
print(y)

print(x._asdict())

