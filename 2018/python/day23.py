#!/usr/bin/env python3

from collections import namedtuple
from operator import *
from itertools import *
from functools import *
import re


pattern = re.compile(r"pos=<([-\d]+),([-\d]+),([-\d]+)>, r=(\d+)")
Point = namedtuple("Point", ["x", "y", "z", "radius"])

def manhattan(a,b):
    return abs(a.x - b.x) + abs(a.y - b.y) + abs(a.z - b.z)

with open("../data/day23.input") as fd:
    lines = filter(len, map(str.strip, fd))
    matches = map(re.Match.groups, map(pattern.match, lines))
    points = list(starmap(Point, map(partial(map,int), matches)))
    strongest = max(points, key=attrgetter("radius"))
    distances = map(partial(manhattan, strongest), points)
    print("pt1", sum(1 for _ in (filter(partial(ge, strongest.radius), distances)))) # 674
