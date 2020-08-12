
# class Spam():
#     pass

Spam = type('Spam', (), {})

s = Spam()

print(Spam)
print(s)

Animal = type('Animal', (), {})

Dog = type('Dog', (Animal,), {'bark': lambda self: print("Woof woof")})
d = Dog()
d.bark()

