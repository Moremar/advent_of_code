#!/usr/bin/env python3
import functools
import time
import part1


def solve_part2(pairs):
    packets = [[2], [6]]
    for (p1, p2) in pairs:
        packets += [p1, p2]
    packets.sort(key=functools.cmp_to_key(lambda a, b: part1.compare(a, b)))
    return (1 + packets.index([2])) * (1 + packets.index([6]))


if __name__ == "__main__":
    start = time.time()
    parsed = part1.parse("data.txt")
    result = solve_part2(parsed)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
