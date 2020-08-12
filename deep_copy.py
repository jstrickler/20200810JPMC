import copy

data = [
    [1, 2, 3],
    [4, 5, 6],
]

d1 = data
d2 = list(data)
print(id(data), id(d1), id(d2))
d1.append('wombat')

print("data:", data)
print("d1:", d1)
print("d2:", d2)
print()
d1[0].append('spam')
print("data:", data)
print("d1:", d1)
print("d2:", d2)

d3 = copy.deepcopy(data)
data[0].append('ham')

print("data:", data)
print("d1:", d1)
print("d2:", d2)
print("d3:", d3)


