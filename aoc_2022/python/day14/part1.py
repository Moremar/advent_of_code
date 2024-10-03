#!/usr/bin/env python3
import time


def get_line(p1, p2):
    if p1[0] == p2[0]:  # vertical line
        return [(p1[0], p1[1] + i) for i in range(0, p2[1] - p1[1], 1 if p2[1] > p1[1] else -1)] + [p2]
    else:               # horizontal line
        return [(p1[0] + i, p1[1]) for i in range(0, p2[0] - p1[0], 1 if p2[0] > p1[0] else -1)] + [p2]


def parse(input_path):
    with open(input_path, 'r') as f:
        paths = [[tuple(map(int, pair.split(','))) for pair in line.split(' -> ')] for line in f.readlines()]
        grid = {}
        for path in paths:
            curr = path[0]
            grid[curr] = '#'
            for point in path[1:]:
                tmp = get_line(curr, point)
                for point in tmp[1:]:
                    curr = point
                    grid[curr] = '#'
        return grid


def draw(grid):
    res = ""
    for y in range(max([y for (x, y) in grid])+1):
        for x in range(min([x for (x, y) in grid])-1, max([x for (x, y) in grid])+1):
            res += grid[(x, y)] if (x, y) in grid else "."
        res += "\n"
    print(res)


def drop_sand(grid, void = None, floor = None):
    x, y = (500, 0)
    while True:
        if y+1 == floor:
            grid[x, y] = 'o'
            return False
        elif y == void:
            return True
        elif (x, y+1) not in grid:
            y += 1
        elif (x-1, y+1) not in grid:
            x, y = x-1, y+1
        elif (x + 1, y + 1) not in grid:
            x, y = x+1, y+1
        else:
            grid[x, y] = 'o'
            return (x, y) == (500, 0)


def solve_part1(grid):
    void = max([y for (x, y) in grid])
    full = False
    while not full:
        full = drop_sand(grid, void = void)
    # draw(grid)
    return len([1 for k in grid if grid[k] == 'o'])


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve_part1(parsed)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
