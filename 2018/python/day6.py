#!/usr/bin/env python

from itertools import *
from operator import *
from functools import *
from collections import defaultdict
from PIL import Image

def write_image(m, variations):
    img = Image.new('L', (len(m[0]), len(m)))
    data = []
    for row in m:
        for column in row:
            data.append((column * 255 / variations))
    img.putdata(data)
    img.save('day6.png')
    img.show()


with open("../data/day6.input") as fd:
    tuples = []
    min_x = max_x = min_y = max_y = None
    for idx, line in enumerate(fd):
        x, y = line.strip().split(", ")
        x, y = (int(x), int(y))
        tuples.append((idx+1, x, y))
        min_x = min(min_x or x, x)
        max_x = max(max_x or x, x)
        min_y = min(min_y or y, y)
        max_y = max(max_y or y, y)

    def part_one():
        matrix = []
        for y in range(max_y):
            row = []
            for x in range(max_x):
                row.append(defaultdict(int))
            matrix.append(row)

        for y in range(max_y):
            row = matrix[y]
            for x in range(max_x):
                coord = row[x]
                for (idx,tx,ty) in tuples:
                    coord[idx] = abs(x - tx) + abs(y - ty)

        dmatrix = []
        for y in range(max_y):
            dmatrix.append([0] * max_x)

        for y in range(max_y):
            row = matrix[y]
            drow = dmatrix[y]
            for x in range(max_x):
                distance, winners = next(iter(groupby(sorted(row[x].items(), key=itemgetter(1)), itemgetter(1))))
                winners = list(winners)
                if len(winners) == 1:
                    drow[x] = winners[0][0]

        write_image(dmatrix, len(tuples))
    
        inf = set([])
        inf.update(dmatrix[0])
        inf.update(dmatrix[-1])
        inf.update(x[0] for x in dmatrix)
        inf.update(x[-1] for x in dmatrix)

        result =  []
        for (idx, x, y) in tuples:
            if idx in inf:
                continue
            result.append((idx, len(reduce(concat, map(list, (filter(partial(eq,idx), (col for col in row)) for row in dmatrix))))))

        print("Largest non-infinite area:", next(iter(sorted(result, key=itemgetter(1), reverse=True))), " == ", 4475)

    def part_two():
        matrix = []
        for y in range(max_y):
            row = []
            for x in range(max_x):
                row.append(sum(abs(tx-x)+abs(ty-y) for (_,tx,ty) in tuples))
            matrix.append(row)
        print(list(reduce(concat, map(list, (filter(partial(gt,10000), (col for col in row)) for row in matrix))))[:10])
        print(len(reduce(concat, map(list, (filter(partial(gt,10000), (col for col in row)) for row in matrix)))))

    part_two()
