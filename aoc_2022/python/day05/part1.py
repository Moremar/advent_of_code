#!/usr/bin/env python3
import collections
import re
import time


def parse(input_path):
    with open(input_path, 'r') as f:
        lines = f.readlines()
        split = lines.index("\n")

        stacks = [collections.deque() for _ in range(len(lines[0]) // 4)]
        for line in lines[:split - 1]:
            for col in range(len(stacks)):
                if line[1 + col * 4] != ' ':
                    stacks[col].appendleft(line[1 + col * 4])

        moves = [tuple(map(int, re.match(r'move (\d+) from (\d+) to (\d+)', line).groups())) \
                 for line in lines[split+1:]]

    return stacks, moves


def solve_part1(stacks, moves):
    for (nb, src, dest) in moves:
        for _ in range(nb):
            stacks[dest-1].append(stacks[src-1].pop())
    return ''.join([stack.pop() for stack in stacks])


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve_part1(*parsed)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
