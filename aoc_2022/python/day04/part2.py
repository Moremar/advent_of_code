#!/usr/bin/env python3
import time
import part1


def solve_part2(elves):
    return len([ 1 for (elf1, elf2) in elves
        if elf1[0] <= elf2[0] <= elf1[1] \
        or elf1[0] <= elf2[1] <= elf1[1] \
        or elf2[0] <= elf1[0] <= elf2[1] \
        or elf2[0] <= elf1[1] <= elf2[1] ])


if __name__ == "__main__":
    start = time.time()
    parsed = part1.parse("data.txt")
    result = solve_part2(parsed)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
