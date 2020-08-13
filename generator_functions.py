
with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)
print()

def nltrimmer(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            yield line.rstrip('\r\n')  # provide value for next()

lines = nltrimmer('DATA/mary.txt')
for line in lines:
    print(line)

def pep_boys():
    yield "Manny"
    yield "Moe"
    yield "Jack"

p = pep_boys()
for pb in p:
    print(pb)
print(p)

p = pep_boys()
a = next(p)
print(a)
print(next(p))
print(next(p))
# print(next(p))

# next() give me the "next" value YIELDED by the generator