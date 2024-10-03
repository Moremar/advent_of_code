#!/usr/bin/env python3
import time
import part1


def solve_part2(arr):
    return sum(sorted(arr)[-3:])


if __name__ == "__main__":
    start = time.time()
    parsed = part1.parse("data.txt")
    result = solve_part2(parsed)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
