#!/usr/bin/env python3

import re


with open("../data/day3.input") as fd:
    squares = []
    max_x = 0
    max_y = 0
    for line in fd:
        cid, sx, sy, sw, sh = re.findall("#([^ ]+) @ ([^,]+),([^:]+): ([^:]+)x([\d]+)", line)[0]
        x, y, w, h = int(sx),int(sy),int(sw),int(sh)
        squares.append((cid, x,y,w,h))
        max_x = max(max_x, x+w)
        max_y = max(max_y, y+h)

    matrix = []
    for y in range(max_y):
        matrix.append([0] * max_x)

    for (_, x,y,w,h) in squares:
        for xoff in range(w):
            for yoff in range(h):
                matrix[y+yoff][x+xoff] += 1

    overlap = 0
    for row in matrix:
        for col in row:
            if col > 1:
               overlap += 1

    print("pt1", overlap)

    for (cid, x,y,w,h) in squares:
        clean = True

        for xoff in range(w):
            if not clean:
                break
            for yoff in range(h):
                if matrix[y+yoff][x+xoff] > 1:
                    clean = False
                    break

        if clean:
            print("pt2", cid)
