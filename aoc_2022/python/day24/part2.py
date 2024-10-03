#!/usr/bin/env python3
import time
import part1


def solve_part2(parsed):
    max_i, max_j = parsed
    start, target = (-1, 0), (max_i+1, max_j)
    time_to_target = part1.find_path(0, start, target, max_i, max_j)
    time_back_to_start = part1.find_path(time_to_target, target, start, max_i, max_j)
    return part1.find_path(time_back_to_start, start, target, max_i, max_j)


if __name__ == "__main__":
    start = time.time()
    parsed = part1.parse("data.txt")
    result = solve_part2(parsed)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
