#!/usr/bin/python
from itertools import groupby

def key_func(state):
    return state[-1]

with open("../DATA/presidents.txt") as pres_in:
    states = map(lambda line: line.split(':')[6], pres_in)
    sorted_states = sorted(states, key=key_func)
    groups = groupby(sorted_states, key=key_func)
    # {group1: [item1, item2, item3], group2: [item1, item2, ...], ...}
    for state, state_list in groups:
        print(state, len(list(state_list)))


