#!/usr/bin/env python3


from itertools import *
from functools import *
from operator import *
import re

with open("../data/day12.input") as fd:
    init = list(fd.readline().strip()[15:])

    patterns = dict(l.strip().split(" => ") for l in fd if l.strip())

def focus(line, i):
    return "".join(line[i-2:i+3])

current = init

offset = 0

def sumit(line, offset):
    return sum(map(partial(add,-offset),
                   map(itemgetter(0),
                       filter(lambda x: x[1] == "#", enumerate(line)))))

delta = olddelta = oldolddelta = 0
for i in range(1,10001):
    if "#" in current[:4]:
        current = list("....") + current + list("....")
        offset += 4
    if "#" in current[-4:]:
        current = list("....") + current + list("....")
        offset += 4
    next = ["."]*len(current)
    for j in range(len(current)):
        pot = patterns.get(focus(current, j), ".")
        next[j] = pot
    delta = sumit(next, offset)-sumit(current, offset)
    current = next
    if delta == olddelta == oldolddelta:
        break
    oldolddelta = olddelta
    olddelta = delta

print(i, delta == olddelta == oldolddelta, delta)

# pt2 = 4300000000349 pt1 = 3337
print(sumit(current, offset) + delta*(50000000000-i))
