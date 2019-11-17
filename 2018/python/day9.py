#!/usr/bin/env python3

from operator import *
import sys
import re
import gc
gc.disable()


def play(nplayers, high_score):
    players = dict((x,0) for x in range(1, nplayers + 1))
    circle = [0]

    offset = 0
    marble = 0

    # print("[-]  (0)")
    for x in range(high_score):
        marble += 1

        if (marble % 23) == 0:
            players[x%nplayers + 1] += marble + circle.pop(offset - 7)
            offset -= 7
            if offset < 0:
                offset += len(circle) + 1
            continue


        if len(circle) == 1:
            circle.append(marble)
            offset = 1
        else:
            offset += 2
            if offset == len(circle):
                circle.append(marble)
            else:
                offset %= len(circle)
                circle.insert(offset, marble)

        # sys.stdout.write("[%d] "%(x%nplayers+1))
        # for i, x in enumerate(circle):
        #     if i == (offset%len(circle)):
        #         sys.stdout.write('(%2d)' % x)
        #     else:
        #         sys.stdout.write(' %2d ' % x)
        # sys.stdout.write('\n')

    return max(players.items(), key=itemgetter(1))


# print(play(9, 25))
# print(play(10, 1618), 8317)
# print(play(13, 7999), 146373)
# print(play(17, 1104), 2764)
# print(play(21, 6111), 54718)
# print(play(30, 5807), 37305)

with open("../data/day9.input") as fd:
    nplayers, points = re.findall(r"(\d+)[^\d]+(\d+)[^\d]+", fd.read())[0]
    print(play(int(nplayers), int(points)), 398242)
    print(play(int(nplayers), int(points)*100), 3273842452)
