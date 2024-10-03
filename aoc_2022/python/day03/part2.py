#!/usr/bin/env python3
import time
import part1


def solve_part2(bags):
    res, i = 0, 0
    while i < len(bags):
        bag1, bag2, bag3 = bags[i:i+3]
        i += 3
        for c in bag1:
            if c in bag2 and c in bag3:
                res += part1.priority(c)
                break
    return res


if __name__ == "__main__":
    start = time.time()
    parsed = part1.parse("data.txt")
    result = solve_part2(parsed)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
