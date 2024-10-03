#!/usr/bin/env python3
import time

DEC_TO_STAFU = {'0': 0, '1': 1, '2': 2, '-': -1, '=': -2}
STAFU_TO_DEC = {0: '0', 1: '1', 2: '2', -1: '-', -2: '='}


def to_decimal(snafu):
    return sum([DEC_TO_STAFU[c] * pow(5, len(snafu)-1-i) for (i, c) in enumerate(snafu)])


def to_snafu(number):
    res = ""
    while number > 0:
        remainder = number % 5
        if remainder > 2:
            remainder -= 5
        res = STAFU_TO_DEC[remainder] + res
        number -= remainder
        number //= 5
    return res


def parse(input_path):
    with open(input_path, 'r') as f:
        return [line.strip() for line in f.readlines()]


def solve_part1(snafus):
    return to_snafu(sum([to_decimal(snafu) for snafu in snafus]))


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve_part1(parsed)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
