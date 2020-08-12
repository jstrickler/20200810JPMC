
def make_str(char, size):
    return char * size

print(make_str("_", 10))
print(make_str("*", 25))

args = "-", 50

# print(make_str(args))
print(make_str(args[0], args[1]))
print(make_str(*args))

def config(**values):
    print(values)

config(name="Fred", city="Durham", street="Elm")
args = {
    'name': 'Andy',
    'city': 'Spokane',
    'street': 'Main',
}
config(**args)





