
a = 1, 2, 3
b = ['a', 'b', 'c']
c = range(10)
d = open('DATA/alice.txt')

for thing in a:
    print(thing)

bi = iter(b)
print(next(bi))
print(next(bi))
# print(next(b))

ai = iter(a)
print(next(ai))
print(next(ai))
print(next(ai))
try:
    print(next(ai))
except:
    pass

c = range(5)
for i in c:
    print(i)

ri = iter(range(5))
print(ri)
print(next(ri))

colors = ['red', 'green', 'blue']

i = iter(colors)
while True:
    try:
        color = next(i)
    except StopIteration:
        break
    print(color)

for color in colors:
    print(color)