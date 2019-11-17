#!/usr/bin/env python3

from itertools import *
from operator import *
from functools import *
from collections import defaultdict
import re

d = defaultdict(set)
kd = defaultdict(set)

tst = """
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
""".strip()

with open("../data/day7.input") as fd:
    nodes = re.findall("Step (.) .+ step (.) .+", fd.read())
    from_set = set(x[0] for x in nodes)
    to_set = set(x[1] for x in nodes)

    for (f,t) in nodes:
        d[f].add(t)
        kd[t].add(f)

    start = list(from_set.difference(to_set))
    target = list(to_set.difference(from_set))

    def part_one():
        res = ''
        solved = set([])
        while kd[target[0]].difference(solved):
            alts = set(list(filter(lambda x: len(kd[x].difference(solved)) == 0, from_set.difference(solved))))
            cur = min(alts)
            res += cur
            solved.add(cur)

        res += target[0]
        print("Steps:", res)

    def part_two():
        res = ''
        solved = set([])
        workers = [(0,None),(0,None),(0,None),(0,None),(0,None)]
        #workers = [(0,None),(0,None)]
        total_time = 0
        while kd[target[0]].difference(solved):
            found1 = False
            for x in range(len(workers)):
                sec, task = workers[x]
                if sec > 0:
                    if not found1:
                        total_time += 1
                        found1 = True
                    sec = sec - 1
                    if sec == 0 and task is not None:
                        solved.add(task)
                        res += task
                        task = None
                    workers[x] = (sec, task)
            dataset = from_set.difference(solved).difference(set(t for (_,t) in workers))
            alts = sorted(list(set(list(filter(lambda x: len(kd[x].difference(solved)) == 0, dataset)))))
            for a in alts:
                found = False
                for x in range(len(workers)):
                    sec, task = workers[x]
                    if task is None:
                        workers[x] = (ord(a) - 64+60, a)
                        found = True
                        break
                if not found:
                    break
            print(alts, workers)

        res += target[0]
        print("Steps:", res)
        print(total_time + ord(target[0])-64+60)

    part_two()
