#!/usr/bin/env python3
import time

def part_one(value):
    elf1 = 0
    elf2 = 1
    board = [3,7]
    count = len(board)
    while count < value:
        v1 = board[elf1]
        v2 = board[elf2]
        v = v1 + v2
        if v < 10:
            board.append(v)
            count += 1
        else:
            board.append(1)
            board.append(v - 10)
            count += 2
        elf1 = (elf1 + v1 + 1) % count
        elf2 = (elf2 + v2 + 1) % count
    return "".join(str(x) for x in board[-10:])

t0 = time.time()
result = part_one(920831+10)
print("{} == 7121102535 in {} seconds".format(result, time.time() - t0))

def part_two(value):
    v_offset, b_offset = 0, 0
    value = [int(x) for x in str(value)]
    goal = len(value)
    elf1, elf2 = 0, 1
    board = [3,7]
    count = len(board)
    while True:
        v1 = board[elf1]
        v2 = board[elf2]

        v = v1 + v2
        if v < 10:
            board.append(v)
            count += 1
        else:
            board.append(1)
            board.append(v - 10)
            count += 2

        while b_offset < count:
            if board[b_offset] == value[v_offset]:
                b_offset += 1
                v_offset += 1
                if v_offset == goal:
                    return b_offset - v_offset
            else:
                b_offset = b_offset - v_offset + 1
                v_offset = 0

        elf1 = (elf1 + v1 + 1) % count
        elf2 = (elf2 + v2 + 1) % count

t0 = time.time()
result = part_two(920831)
print("{} == 20236441 in {} seconds".format(result, time.time() - t0))
