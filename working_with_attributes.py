# getattr() hasattr() setattr() delattr()

class Spam():

    def __init__(self, value):
        self._value = value

    @property
    def some_value(self):
        return self._value

    @some_value.setter
    def some_value(self, value):
        self._value = value

    @some_value.deleter
    def some_value(self):
        del self._value

s = Spam(42)
print(s.some_value)
print(getattr(s, "some_value"))
setattr(s, "some_value", 1000)
print(s.some_value)

print(hasattr(s, "some_value"))
print(hasattr(s, "some_other_value"))

delattr(s, "some_value")

setattr(Spam, 'bark', lambda self: print("Woof woof"))
s.bark()

