#!/usr/bin/env python3

from itertools import *
from operator import *
from functools import *
from collections import defaultdict, namedtuple
import re

Node = namedtuple("Node", ["metadata", "children"])


with open("../data/day8.input") as fd:
    input = fd.read()
    t = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
    def solve(txt):
        def munch(data,offset):
            ncount = data[offset+0]
            nmetadata = data[offset+1]
            children = []
            offset += 2
            for x in range(ncount):
                node, offset = munch(data, offset)
                children.append(node)
            metadata = data[offset:offset+nmetadata]
            offset += nmetadata
            return Node(metadata, children), offset
        tree, offset = munch(list(map(int, txt.split())), 0)


        def sumtree(node):
            return sum(sumtree(x) for x in node.children)+sum(node.metadata)
        print("pt1", sumtree(tree))

        def sum2(node):
            if len(node.children) == 0:
                return sum(node.metadata)
            tot = 0
            for x in node.metadata:
                if x > len(node.children):
                    continue
                tot += sum2(node.children[x-1])
            return tot
        print("pt2", sum2(tree))

    solve(input)
