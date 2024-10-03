#!/usr/bin/env python3
import time


def parse(input_path):
    with open(input_path, 'r') as f:
        return [(line[0:4], int(line[5:]) if len(line) > 5 else 0) for line in f.readlines()]


def solve_part1(instructions):
    res = cycle = 0
    regX = 1
    for (op, val) in instructions:
        duration = 1 if op == "noop" else 2
        for i in range(duration):
            cycle += 1
            res += (cycle * regX) if (cycle % 40 == 20) else 0
            regX += 0 if i < duration-1 else val
    return res


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve_part1(parsed)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
