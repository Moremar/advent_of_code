#!/usr/bin/env python3
import time
from collections import deque


def parse(input_path):
    grid = []
    with open(input_path, 'r') as f:
        for i, line in enumerate(f.readlines()):
            if 'S' in line :
                start = (i, line.index('S'))
            if 'E' in line :
                end = (i, line.index('E'))
            grid.append([ord(c) - ord('a') for c in line.strip().replace('S', 'a').replace('E', 'z')])
    return grid, start, end


def solve_part1(grid, start, end):
    seen = set()
    to_process = deque([(start, 0)])
    while len(to_process):
        p, steps = to_process.popleft()
        if p in seen:
            continue
        seen.add(p)
        for next_pos in [(p[0]+1, p[1]), (p[0]-1, p[1]), (p[0], p[1]+1), (p[0], p[1]-1)]:
            if next_pos not in seen \
                    and 0 <= next_pos[0] < len(grid) \
                    and 0 <= next_pos[1] < len(grid[0]) \
                    and grid[next_pos[0]][next_pos[1]] <= grid[p[0]][p[1]] + 1:
                if next_pos == end:
                    return steps + 1
                seen.add(p)
                to_process.append((next_pos, steps + 1))


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve_part1(*parsed)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
