#!/usr/bin/env python3

def part_one():
    frequency = 0
    with open("../data/day1.input") as fd:
        for line in fd:
            change = line.strip()
            if not change:
                break
            if change.startswith('+'):
                frequency += int(change[1:])
            else:
                frequency -= int(change[1:])
    return frequency

def part_two():
    def generate():
        acc = 0
        yield acc
        while True:
            with open("../data/day1.input") as fd:
                for line in fd:
                    change = line.strip()
                    if not change:
                        break
                    if change.startswith('+'):
                        acc += int(change[1:])
                    else:
                        acc -= int(change[1:])
                    yield acc

    frequencies = set([])
    for frequency in generate():
        if frequency in frequencies:
            return frequency
        frequencies.add(frequency)

print("Pt1:", part_one())
print("Pt2:", part_two())
