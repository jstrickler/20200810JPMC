from copy import deepcopy

x = 5   # int x = new int(5);
y = x   # y is another label for int obj

x = 10

print(x, y)

y = "spam"

a = 25
b = a
c = a
del a
print(b, c)
del b
print(c)
del c

a = 25
b = a
c = a
print(id(a), id(b), id(c))

if (a == b):
    print("equal values")

if (a is b):
    print("same object")

a = 5
b = 5
c = 5
print(a is b is c)

a = "spam"
b = "spam"
c = "spam"

print(a is b is c)
print(id(a), id(b), id(c))

spam = ['a', 'b', 'c']
ham = spam

ham.append('d')
print(spam, ham)

spam.append([1, 2, 3])

print(spam, ham)
spam[4].append(4)
print(spam, ham)

copy1 = list(spam)
copy2 = spam.copy()
copy3 = [*spam]

print(copy1)
print(copy2)
print(copy3)
copy1.append('wombat')
copy2.append('wallaby')
copy3.append('koala')

print(copy1)
print(copy2)
print(copy3)
print(spam)
print(id(spam), id(copy1), id(copy2), id(copy3))
copy1[4].append('cupcake')

print(copy1)
print(copy2)
print(copy3)
print(spam)
copy4 = deepcopy(spam)
copy4[4].append("thumb")
print(copy4)
print(spam)

foo = 1, 2, [3, 4, 5]
bar = deepcopy(foo)
blah = tuple(foo)

print(id(foo), id(bar), id(blah))

foo[2].append("WOW")
print(foo, blah)
print(bar)