#!/usr/bin/env python3
import time
import part1

MOVES = {'A': part1.ROCK, 'B': part1.PAPER, 'C': part1.SCISSORS}


def get_play(his_play, target):
    return (MOVES[his_play] + 2) % 3 if target == 'X' \
        else MOVES[his_play] if target == 'Y' \
        else (MOVES[his_play] + 1) % 3


def parse(input_path):
    with open(input_path, 'r') as f:
        return [(MOVES[line[0]], get_play(line[0], line[2])) for line in f.readlines()]


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = part1.solve_part1(parsed)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
