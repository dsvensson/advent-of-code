#!/usr/bin/env python3
from concurrent.futures import ProcessPoolExecutor
from operator import itemgetter
import numpy as np

# a much better solution would be based on https://youtu.be/uEJ71VlUmMQ?t=313

# Puzzle input
serial = 8199

g = np.zeros((300,300))

for x in range(300):
    for y in range(300):
        rack_id = x + 10
        power = rack_id * y + serial
        power *= rack_id
        power = int((power % 1000) / 100) - 5
        g[y][x] = power

def traverse(n):
    lens = np.arange(n)
    for x in range(300-(n-1)):
        for y in range(300-(n-1)):
            yield (n,x,y,g[np.ix_(lens+y,lens+x)].sum())

def find_largest(n):
    return max(traverse(n), key=itemgetter(3))

def part_one():
    print(find_largest(3))

def part_two():
    with ProcessPoolExecutor() as executor:
        print(max(executor.map(find_largest, range(300)), key=itemgetter(3)))

part_one() # x: 235, y:  87, size:  3
part_two() # x: 234, y: 272, size: 18