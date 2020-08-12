#!/usr/bin/env python

from itertools import groupby, islice

with open('../DATA/words.txt') as words_in:  # <1>
    all_words = (w.rstrip() for w in words_in)  # <2>

    g = groupby(all_words, key=lambda e: e[0])  # <3>

    # gdict = {letter: list(words) for letter, words in g}

    print(g)

    # for key, <virtual list of values> in <groupby object which is like a dict but virtual>
    for letter, words in g:  # for key, value in dict.items()
        print(letter, list(islice(words, 5)))

exit()

counts = {letter: len(list(wlist)) for letter, wlist in g}  # <4>

sorted_letters = sorted(counts.items(), key=lambda e: e[1], reverse=True)  # <5>
for letter, count in sorted_letters:  # <6>
    print(letter, count)

print()
print("Total words counted:", sum(counts.values()))  # <7>
