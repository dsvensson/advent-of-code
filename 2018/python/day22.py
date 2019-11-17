#!/usr/bin/env python3
import time
from enum import *
from functools import *
from itertools import *
from operator import *

import networkx


class ToolType(Enum):
    TORCH = 0
    CLIMBING_GEAR = 1
    NEITHER = 2

class RegionType(Enum):
    ROCKY = 0
    WET = 1
    NARROW = 2

def solve(depth, dstX, dstY):
    @lru_cache(maxsize=None)
    def erosion_level(x, y):
        return (geologic_index(x, y) + depth) % 20183

    @lru_cache(maxsize=None)
    def geologic_index(x, y):
        if x == 0 and y == 0:
            return 0
        if x == dstX and y == dstY:
            return 0
        if x == 0:
            return y * 48271
        if y == 0:
            return x * 16807
        return erosion_level(x - 1, y) * erosion_level(x, y - 1)

    def region_type(x, y):
        return RegionType(erosion_level(x, y) % 3)

    print("pt1", sum(region_type(x, y).value for x, y in product(range(dstX+1), range(dstY+1))))

    # TIL A* algorithm
    # https://en.wikipedia.org/wiki/A*_search_algorithm

    # Construct a graph with edges between tiles for tools that
    # also works on neighboring tiles, and self-looping edges
    # for tool switching.

    t0 = time.time()
    COMPAT_GEAR = {
        RegionType.ROCKY: set([ToolType.CLIMBING_GEAR, ToolType.TORCH]),
        RegionType.WET: set([ToolType.CLIMBING_GEAR, ToolType.NEITHER]),
        RegionType.NARROW: set([ToolType.TORCH, ToolType.NEITHER])
    }

    def add_gear_switching(graph, typ, x, y):
        gear1, gear2 = COMPAT_GEAR[typ]
        graph.add_edge((x, y, gear1), (x, y, gear2), weight=7)

    def neighbors(x, y):
        if x != 0:
            yield (x - 1, y)
        yield (x + 1, y)
        if y != 0:
            yield (x, y - 1)
        yield (x, y + 1)

    def add_neighbors(graph, typ, x, y):
        gear1, gear2 = COMPAT_GEAR[typ]
        for nx, ny in neighbors(x, y):
            next_gear = COMPAT_GEAR[region_type(nx, ny)]
            if gear1 in next_gear:
                graph.add_edge((x, y, gear1), (nx, ny, gear1), weight=1)
            if gear2 in next_gear:
                graph.add_edge((x, y, gear2), (nx, ny, gear2), weight=1)

    graph = networkx.Graph()
    for x, y in product(range(dstX+30), range(dstY+1)):
        typ = region_type(x, y)
        add_gear_switching(graph, typ, x, y)
        add_neighbors(graph, typ, x, y)

    def manhattan(a, b):
        x1, y1, _ = a
        x2, y2, _ = b
        return abs(x2 - x1) + abs(y2 - y1)

    print("pt2", networkx.algorithms.astar_path_length(graph, (0, 0, ToolType.TORCH), (dstX, dstY, ToolType.TORCH), manhattan))


#solve(510, 10, 10)  #   114, 45
solve(4848, 15, 700) # 11359, 976
