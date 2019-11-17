#!/usr/bin/env python3

import time
from itertools import *
from operator import *
from functools import *

def compose2(f, g):
    return lambda *a, **kw: f(g(*a, **kw))

def compose(*fs):
    return reduce(compose2, fs)

def part_one():
    with open("../data/day2.input") as fd:
        return mul(*map(compose(len, list, itemgetter(1)),
                        groupby(sorted(reduce(chain, (set(filter(partial(lt, 1),
                                                                 map(compose(len, list, itemgetter(1)),
                                                                     groupby(sorted(line), id)))) for line in fd))), id)))

import Levenshtein

def part_two():
    with open("../data/day2.input") as fd:
        ids = list(line.strip() for line in fd if line.strip())
        distance, (first, second) = list(filter(lambda x: x[0] == 1, map(lambda a: (Levenshtein.distance(a[0],a[1]), a), permutations(filter(truth, map(str.strip, ids)), 2))))[0]
        res = ''
        for (a,b) in zip(first, second):
            if a==b:
                res += a
        return res

def part_two2():
    with open("../data/day2.input") as fd:
        perms = list(permutations(filter(truth, map(str.strip, fd)), 2))
        offbyone = next(iter(sorted(enumerate(map(compose(compose(len, list),
                                                          partial(filter, partial(lt, 1)),
                                                          partial(map, compose(len, set))),
                                                  map(list, map(partial(reduce, zip), perms)))), key=itemgetter(1))))
        return ''.join(map(itemgetter(0), filter(compose(partial(eq,1), len, set), reduce(zip, perms[offbyone[0]]))))

t0 = time.time()
print("Checksum:", part_one(), time.time() - t0)
t1 = time.time()
print("    Diff:", part_two(), time.time() - t1)
t2 = time.time()
print("    Diff:", part_two2(), time.time() - t2)
