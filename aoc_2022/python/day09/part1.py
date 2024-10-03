#!/usr/bin/env python3
import time

DIRS = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}


def parse(input_path):
    with open(input_path, 'r') as f:
        return [(DIRS[line[0]], int(line[2:])) for line in f.readlines()]


def next_tail_pos(head, tail):
    if abs(head[0] - tail[0]) > 1 and abs(head[1] - tail[1]) > 1:
        return tail[0] + (1 if head[0] > tail[0] else -1), (tail[1] + (1 if head[1] > tail[1] else -1))
    elif abs(head[0] - tail[0]) > 1:
        return tail[0] + (1 if head[0] > tail[0] else -1), head[1]
    elif abs(head[1] - tail[1]) > 1:
        return head[0], tail[1] + (1 if head[1] > tail[1] else -1)
    else:
        return tail


def solve_part1(instructions):
    head = tail = (0, 0)
    visited = set()
    for (move, steps) in instructions:
        for k in range(steps):
            head = head[0] + move[0], head[1] + move[1]
            tail = next_tail_pos(head, tail)
            visited.add(tail)
    return len(visited)


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve_part1(parsed)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
