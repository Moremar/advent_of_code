import math
from part1 import count_trees, parse


def solve(trees):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return math.prod([count_trees(trees, dx, dy) for (dx, dy) in slopes])


if __name__ == '__main__':
    print(solve(parse('data.txt')))
