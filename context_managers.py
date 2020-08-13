import sqlite3
from threading import Lock

with open('DATA/mary.txt') as mary_in:
    pass

with sqlite3.connect('mydatabase.db') as conn:
    pass

# yale = Lock()
# with yale:
#     print("locked")

class Spam():

    def wombat(self):
        print("wombat")

    def __enter__(self):
        print("hello!")
        return self

    def __exit__(self, _type, value, traceback):
        print("goodbye!")
        return value

with Spam() as s:
    print(s)
    print("doing some excellent business logic here...")

p = Spam()
p.wombat()

