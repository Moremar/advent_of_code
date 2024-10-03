#!/usr/bin/env python3
import time
import part1


def solve_part2(instructions):
    cycle = pixel = 0
    regX = 1
    res = ""
    for (op, val) in instructions:
        duration = 1 if op == "noop" else 2
        for i in range(duration):
            res += "\n" if cycle % 40 == 0 else ""
            cycle += 1
            res += "#" if regX-1 <= pixel <= regX+1 else "."
            regX += 0 if i < duration-1 else val
            pixel = (pixel + 1) % 40
    return res


if __name__ == "__main__":
    start = time.time()
    parsed = part1.parse("data.txt")
    result = solve_part2(parsed)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
