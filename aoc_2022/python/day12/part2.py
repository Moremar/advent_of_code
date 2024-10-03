#!/usr/bin/env python3
import time
import part1


def solve_part2(grid, _, end):
    shortest = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                distance = part1.solve_part1(grid, (i, j), end)
                if shortest is None or (distance is not None and distance < shortest):
                    shortest = distance
    return shortest


if __name__ == "__main__":
    start = time.time()
    parsed = part1.parse("data.txt")
    result = solve_part2(*parsed)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
