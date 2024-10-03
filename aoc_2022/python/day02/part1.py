#!/usr/bin/env python3
import time

ROCK, PAPER, SCISSORS = 0, 1, 2
MOVES = {'A': ROCK, 'B': PAPER, 'C': SCISSORS,
         'X': ROCK, 'Y': PAPER, 'Z': SCISSORS}


def parse(input_path):
    with open(input_path, 'r') as f:
        return [(MOVES[line[0]], MOVES[line[2]]) for line in f.readlines()]


def solve_part1(parsed):
    score = 0
    for play in parsed:
        shape_val = play[1] + 1
        outcome_val = 3 if play[0] == play[1] \
                 else 6 if play[1] == (play[0] + 1) % 3 \
                 else 0
        score += shape_val + outcome_val
    return score


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve_part1(parsed)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')