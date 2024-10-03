#!/usr/bin/env python3
import time
import part1


def solve_part2(tree):
    first = part1.compute(tree.left)
    second = part1.compute(tree.right)
    return round((first.real - second.real) / (second.imag - first.imag))


if __name__ == "__main__":
    start = time.time()
    parsed = part1.parse("data.txt", True)
    result = solve_part2(parsed)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
