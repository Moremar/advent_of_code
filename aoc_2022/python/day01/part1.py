#!/usr/bin/env python3
import time


def parse(input_path):
    res = []
    curr = 0
    with open(input_path, 'r') as f:
        for line in f.readlines():
            if len(line.strip()) == 0:
                res.append(curr)
                curr = 0
            else:
                curr += int(line)
    return res


def solve_part1(arr):
    return max(arr)


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve_part1(parsed)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
