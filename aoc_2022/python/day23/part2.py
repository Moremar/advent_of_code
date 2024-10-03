#!/usr/bin/env python3
import time
import part1


def solve_part2(elves):
    cycle = part1.get_cycle()

    round_id, stable = 0, False
    while not stable:
        elves, stable = part1.play_round(round_id, elves, cycle)
        round_id = round_id + 1

    return round_id


if __name__ == "__main__":
    start = time.time()
    parsed = part1.parse("data.txt")
    result = solve_part2(parsed)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
