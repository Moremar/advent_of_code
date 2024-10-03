#!/usr/bin/env python3
import time


def parse(input_path):
    with open(input_path, 'r') as f:
        return [ list(map(int, [*line.strip()])) for line in f.readlines()]


def solve_part1(trees):
    visible = 0
    for i in range(len(trees)):
        for j in range(len(trees[0])):
            if i in [0, len(trees)-1] or j in [0, len(trees[0])-1]:
                visible += 1
            else:
                left  = trees[i][:j]
                right = trees[i][j + 1:]
                above = [trees[k][j] for k in range(i)]
                below = [trees[k][j] for k in range(i + 1, len(trees))]
                if trees[i][j] > min([max(left), max(right), max(above), max(below)]):
                    visible += 1
    return visible


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve_part1(parsed)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
