#!/usr/bin/env python
#

strings = ['wombat', 'koala', 'kookaburra', 'blue-ringed octopus']

result = [s.upper() for s in strings]  # <1>
print(result)

ustrings = map(str.upper, strings)  # <2>
for ustring in ustrings:
    print(ustring)
print()

results = map(len, strings)  # <3>
for result in results:
    print(result)
