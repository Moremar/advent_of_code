#!/usr/bin/env python3
import time
import part1


def solve_part2(blueprints, time):
    return part1.best_geode_number(blueprints[0], time) \
           * part1.best_geode_number(blueprints[1], time) \
           * part1.best_geode_number(blueprints[2], time)


if __name__ == "__main__":
    start = time.time()
    parsed = part1.parse("data.txt")
    result = solve_part2(parsed, 32)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
