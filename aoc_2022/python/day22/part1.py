#!/usr/bin/env python3
import re
import time

EMPTY, WALL = '.', '#'
RIGHT, DOWN, LEFT, UP = range(4)
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def parse(input_path):
    world = {}
    start = None
    moves = []
    with open(input_path, 'r') as f:
        lines = f.readlines()
        for (row, line) in enumerate(lines[:-1]):
            for(col, c) in enumerate(line):
                if c == EMPTY and start is None:
                    start = (1 + row, 1 + col)
                if c in [EMPTY, WALL]:
                    world[(1 + row, 1 + col)] = c
        for token in re.findall('\d+[LRE]', lines[-1].strip() + 'E'):
            moves.append((int(token[:-1]), token[-1]))
    return start, world, moves


def wrap(world, pos, direction):
    next_cell = (pos[0] + DIRECTIONS[direction][0], pos[1] + DIRECTIONS[direction][1])
    if next_cell not in world:
        if direction == RIGHT:
            next_cell = (next_cell[0], min([y for (x, y) in world if x == next_cell[0]]))
        elif direction == DOWN:
            next_cell = (min([x for (x, y) in world if y == next_cell[1]]), next_cell[1])
        elif direction == LEFT:
            next_cell = (next_cell[0], max([y for (x, y) in world if x == next_cell[0]]))
        elif direction == UP:
            next_cell = (max([x for (x, y) in world if y == next_cell[1]]), next_cell[1])
    return next_cell, direction


def solve_part1(parsed, wrapping_fn):
    position, world, moves = parsed
    direction = RIGHT
    for move in moves:
        for i in range(move[0]):
            next_cell, next_direction = wrapping_fn(world, position, direction)
            if world[next_cell] == WALL:
                break
            position = next_cell
            direction = next_direction
        if move[1] == 'L':
            direction = (direction + 3) % 4
        elif move[1] == 'R':
            direction = (direction + 1) % 4
    return 1000 * position[0] + 4 * position[1] + direction


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve_part1(parsed, wrap)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
