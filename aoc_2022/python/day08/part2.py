#!/usr/bin/env python3
import time
import part1


def viewing_distance(tree_row, height):
    distance = 0
    for h in tree_row:
        distance += 1
        if h >= height:
            break
    return distance


def solve_part2(trees):
    best_score = 0
    for i in range(len(trees)):
        for j in range(len(trees[0])):
            height = trees[i][j]
            left  = viewing_distance(trees[i][:j][::-1], height)
            right = viewing_distance(trees[i][j + 1:], height)
            above = viewing_distance([trees[k][j] for k in range(i)][::-1], height)
            below = viewing_distance([trees[k][j] for k in range(i + 1, len(trees))], height)
            best_score = max(best_score, left * right * above * below)
    return best_score


if __name__ == "__main__":
    start = time.time()
    parsed = part1.parse("data.txt")
    result = solve_part2(parsed)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
