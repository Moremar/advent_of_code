#!/usr/bin/env python3
import time
import part1


def solve_part2(grid):
    floor = max([y for (x, y) in grid]) + 2
    full = False
    while not full:
        full = part1.drop_sand(grid, floor = floor)
    # part1.draw(grid)
    return len([1 for k in grid if grid[k] == 'o'])


if __name__ == "__main__":
    start = time.time()
    parsed = part1.parse("data.txt")
    result = solve_part2(parsed)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
