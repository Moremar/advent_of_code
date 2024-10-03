#!/usr/bin/env python3
import time
from collections import deque

BLIZZARDS = {}
RIGHT, DOWN, LEFT, UP, STILL = (0, 1), (1, 0), (0, -1), (-1, 0), (0, 0)


def parse(input_path):
    BLIZZARDS[0] = {}
    with open(input_path, 'r') as f:
        for i, line in enumerate(f.readlines()[1:-1]):
            max_i, max_j = i, len(line)-4
            for (j, c) in enumerate(line[1:-2]):
                if c in '>v<^':
                    BLIZZARDS[0][(i, j)] = [RIGHT] if c == '>' else [DOWN] if c == 'v' else [LEFT] if c == '<' else [UP]
    return max_i, max_j


def add_tuple(a, b):
    return a[0] + b[0], a[1] + b[1]


def compute_blizzards(step, max_i, max_j):
    if step not in BLIZZARDS:
        assert (step-1) in BLIZZARDS
        BLIZZARDS[step] = {}
        for (key, winds) in BLIZZARDS[step-1].items():
            for wind in winds:
                next_wind = add_tuple(key, wind)
                next_wind = (next_wind[0] % (max_i + 1), next_wind[1] % (max_j + 1))
                if next_wind not in BLIZZARDS[step]:
                    BLIZZARDS[step][next_wind] = []
                BLIZZARDS[step][next_wind] += [wind]


def find_path(step, start, target, max_i, max_j):
    seen = set()
    to_process = deque([(start, step)])
    while len(to_process) > 0:
        position, step = to_process.popleft()
        compute_blizzards(step + 1, max_i, max_j)
        for direction in [RIGHT, DOWN, LEFT, UP, STILL]:
            next_position = add_tuple(position, direction)
            if next_position == target:
                return step+1
            elif not (next_position == start or 0 <= next_position[0] <= max_i) or not 0 <= next_position[1] <= max_j:
                continue
            elif next_position not in BLIZZARDS[step+1]:
                if (next_position, step+1) not in seen:
                    seen.add((next_position, step+1))
                    to_process.append((next_position, step+1))


def solve_part1(parsed):
    max_i, max_j = parsed
    start, target = (-1, 0), (max_i+1, max_j)
    return find_path(0, start, target, max_i, max_j)


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve_part1(parsed)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
