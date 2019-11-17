#!/usr/bin/env python3
import numpy as np
import re

# first version actually visual inspection with matplotlib
def solve(input):
    data = np.array([(int(x),int(y),int(vx),int(vy))
                     for (x,y,vx,vy)
                     in re.findall("[^<]+<([^,]+),([^>]+)>[^<]+<([^,]+),([^>]+)>", input)])

    p = data[:,:2]
    v = data[:,2:]

    i = 0
    s0 = 2**32
    while True:
        s1 = p[:,0].max() - p[:,0].min() + p[:,1].max() - p[:,1].min()
        if s0 < s1:
            p -= v
            i -= 1
            break
        p += v
        i += 1
        s0 = s1

    min_x = p[:,0].min()
    min_y = p[:,1].min()
    width =  p[:,0].max() - min_x
    height =  p[:,1].max() - min_y

    b = np.full((height+1, width+1), ".")
    for x,y in p:
        b[y-min_y,x-min_x] = "*"

    print("Seconds:", i)
    for row in b:
        print(''.join(row))

with open("../data/day10.input") as fd:
    solve(fd.read()) # pt1: XLZAKBGZ, pt2: 10656
