#!/usr/bin/env python3
import string
import time


def parse(input_path):
    with open(input_path, 'r') as f:
        return [line.strip() for line in f.readlines()]


def priority(c):
    return string.ascii_letters.index(c) + 1


def solve_part1(bags):
    res = 0
    for bag in bags:
        for item_type in bag[:len(bag)//2]:
            if item_type in bag[len(bag)//2:]:
                res += priority(item_type)
                break
    return res


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve_part1(parsed)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
