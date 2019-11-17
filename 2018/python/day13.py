#!/usr/bin/env python3

from itertools import *
from functools import *
from operator import *
from enum import Enum
import re
import sys

with open("../data/day13.input") as fd:
    chart = []
    for line in fd:
        chart.append(list(line[:-1]))

class Direction(Enum):
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3

    def turn(self, leaning):
        lookup = {
            Direction.NORTH: {
                Leaning.STRAIGHT: Direction.NORTH,
                Leaning.LEFT: Direction.WEST,
                Leaning.RIGHT: Direction.EAST,
            },
            Direction.SOUTH: {
                Leaning.STRAIGHT: Direction.SOUTH,
                Leaning.LEFT: Direction.EAST,
                Leaning.RIGHT: Direction.WEST,
            },
            Direction.EAST: {
                Leaning.STRAIGHT: Direction.EAST,
                Leaning.LEFT: Direction.NORTH,
                Leaning.RIGHT: Direction.SOUTH,
            },
            Direction.WEST: {
                Leaning.STRAIGHT: Direction.WEST,
                Leaning.LEFT: Direction.SOUTH,
                Leaning.RIGHT: Direction.NORTH,
            },
        }
        return lookup[self][leaning]

    def __str__(self):
        return {
            Direction.NORTH: "^",
            Direction.SOUTH: "V",
            Direction.WEST: "<",
            Direction.EAST: ">",
        }[self]


class Leaning(Enum):
    LEFT = 0
    STRAIGHT = 1
    RIGHT = 2

    def next(self):
        return {
            Leaning.LEFT: Leaning.STRAIGHT,
            Leaning.STRAIGHT: Leaning.RIGHT,
            Leaning.RIGHT: Leaning.LEFT,
        }[self]


class Cart(object):
    def __init__(self, x, y, direction):
        self.pos = (x, y)
        self.direction = direction
        self.leaning = Leaning.LEFT

    def move(self, chart):
        x, y = self.pos
        section = chart[self.pos[1]][self.pos[0]]

        if self.direction is Direction.NORTH:
            self.pos = (x, y - 1)
        elif self.direction is Direction.SOUTH:
            self.pos = (x, y + 1)
        elif self.direction is Direction.WEST:
            self.pos = (x - 1, y)
        else:
            self.pos = (x + 1, y)
        self.realign(chart)
        return self

    def realign(self, chart):
        x, y = self.pos
        section = chart[y][x]
        if section in ("-", "|"):
            return
        elif section == "+":
            self.direction = self.direction.turn(self.leaning)
            self.leaning = self.leaning.next()
        elif section == "/":
            self.direction = {
                Direction.NORTH: Direction.EAST,
                Direction.SOUTH: Direction.WEST,
                Direction.EAST: Direction.NORTH,
                Direction.WEST: Direction.SOUTH,
            }[self.direction]
        elif section == "\\":
            self.direction = {
                Direction.NORTH: Direction.WEST,
                Direction.SOUTH: Direction.EAST,
                Direction.EAST: Direction.SOUTH,
                Direction.WEST: Direction.NORTH,
            }[self.direction]
        else:
            raise Exception("oh crap")

    def __str__(self):
        return "Cart({}, {}, {}, {})".format(self.direction, self.leaning, self.pos[0], self.pos[1])

    def __repr__(self):
        return str(self)

def draw(chart, carts):
    for y in range(len(chart)):
        for x in range(len(chart[y])):
            if (x,y) in (x.pos for x in carts):
                sys.stdout.write("@")
            else:
                sys.stdout.write(chart[y][x])
        sys.stdout.write("\n")
    sys.stdout.write("\n")

carts = []

for y in range(len(chart)):
    for x in range(len(chart[y])):
        section = chart[y][x]
        if section == ">":
            carts.append(Cart(x, y, Direction.EAST))
            chart[y][x] = "-"
        elif section == "<":
            carts.append(Cart(x, y, Direction.WEST))
            chart[y][x] = "-"
        elif section == "^":
            carts.append(Cart(x, y, Direction.NORTH))
            chart[y][x] = "|"
        elif section == "v":
            carts.append(Cart(x, y, Direction.SOUTH))
            chart[y][x] = "|"

draw(chart, carts)

first = True
while True:
    crashed = {}
    for cart in sorted(carts, key=lambda x: x.pos):
        if cart.pos in crashed:
            continue
        cart.move(chart)
        positions = dict((x.pos, x) for x in carts)
        opponent = positions.get(cart.pos)
        if opponent is not None:
            crashed[opponent.pos] = opponent
            crashed[cart.pos] = cart

    if crashed:
        next_carts = []
        for a,b in groupby(sorted(carts, key=lambda x: x.pos), key=lambda x: x.pos):
            l = list(b)
            if len(l) == 1:
                next_carts += l
            elif first:
                print("pt1", l[0].pos)
                first = False
        carts = next_carts
        if len(carts) == 1:
            print("pt2", carts[0].pos)
            break
