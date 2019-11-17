#!/usr/bin/env python3

import operator
import types
import re
from collections import defaultdict

def op_first(a,b):
    return a

class Machine(object):
    def __init__(self):
        self.regs = [0,0,0,0]
        self.instructions = {}

        register = lambda x: self.regs[x]
        immediate = lambda x: x

        self.gen_funcs({
            'addr': (operator.add, register, register),
            'addi': (operator.add, register, immediate),
            'mulr': (operator.mul, register, register),
            'muli': (operator.mul, register, immediate),
            'banr': (operator.and_, register, register),
            'bani': (operator.and_, register, immediate),
            'borr': (operator.or_, register, register),
            'bori': (operator.or_, register, immediate),
            'setr': (op_first, register, immediate),
            'seti': (op_first, immediate, immediate),
            'gtir': (operator.gt, immediate, register),
            'gtri': (operator.gt, register, immediate),
            'gtrr': (operator.gt, register, register),
            'eqir': (operator.eq, immediate, register),
            'eqri': (operator.eq, register, immediate),
            'eqrr': (operator.eq, register, register),
        })

    
    def gen_func(self, op, acc1, acc2):
        def func(a, b, c):
            self.regs[c] = int(op(acc1(a), acc2(b)))
        return func

    def gen_funcs(self, funcs):
        for name, (op, acc1, acc2) in funcs.items():
            self.__dict__[name] = self.gen_func(op, acc1, acc2)
            self.instructions[name] = self.__dict__[name]

    def find(self, before, after, instr, p0, p1, dst):
        result = []
        for name, fun in self.instructions.items():
            self.regs = before[:]
            fun(p0, p1, dst)
            if self.regs == after:
                result.append(name)
        return result

    def set_mapping(self, mapping):
        self.opcodes = {}
        for name, opcode in mapping.items():
            self.opcodes[opcode] = self.instructions[name]

    def execute(self, opcode, a, b, c):
        self.opcodes[opcode](a, b, c)

m = Machine()

count = 0
variants = defaultdict(set)

def parse_before(line):
    return list(map(int, re.match("Before: \[(?P<r0>\d+), (?P<r1>\d+), (?P<r2>\d+), (?P<r3>\d+)\]", line).groups()))

def parse_after(line):
    return list(map(int, re.match("After:  \[(?P<r0>\d+), (?P<r1>\d+), (?P<r2>\d+), (?P<r3>\d+)\]", line).groups()))

def parse_instr(line):
    return list(map(int, re.match("(?P<r0>\d+) (?P<r1>\d+) (?P<r2>\d+) (?P<r3>\d+)", line).groups()))

with open("../data/day16.input") as fd:
    for line in map(str.strip, fd):
        if not line:
            empty += 1
            if empty > 2:
                break
            continue
        empty = 0
        if line.startswith("Before"):
            before = parse_before(line)
        elif line.startswith("After"):
            after = parse_after(line)
            matches = m.find(before, after, opcode, a, b, c)
            if len(matches) >= 3:
                count += 1
            for match in matches:
                variants[match].add(opcode)

        else:
            opcode, a, b, c = parse_instr(line)

    print("pt1", count)

    mapping = {}

    while len(variants):
        found = set([])
        for name, instr in filter(lambda x: len(x[1]) == 1, variants.items()):
            mapping[name] = next(iter(instr))
            found.update(instr)
        
        variants = dict(filter(lambda x: x[0] not in mapping, map(lambda x: (x[0], x[1].difference(found)), variants.items())))

    m.set_mapping(mapping)

    m.regs = [0,0,0,0]

    for line in map(str.strip, fd):
        if not line:
            continue
        opcode, a, b, c = parse_instr(line)

        m.execute(opcode, a, b, c)

    print("pt2", m.regs[0])
