#!/usr/bin/env python3
import time
import part1


if __name__ == "__main__":
    start = time.time()
    parsed = part1.parse("data.txt", 811589153)
    result = part1.solve_part1(parsed, 10)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
