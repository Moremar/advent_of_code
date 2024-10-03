#!/usr/bin/env python3
import re
import time


def parse(input_path):
    res = []
    with open(input_path, 'r') as f:
        for line in f.readlines():
            m = re.match(r'(\d+)-(\d+),(\d+)-(\d+)', line)
            n1, n2, n3, n4 = m.groups()
            res.append(((int(n1), int(n2)), (int(n3), int(n4))))
    return res


def solve_part1(elves):
    return len([ 1 for (elf1, elf2) in elves
                    if elf1[0] <= elf2[0] <= elf2[1] <= elf1[1]
                    or elf2[0] <= elf1[0] <= elf1[1] <= elf2[1] ])


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve_part1(parsed)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
