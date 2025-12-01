"""Solution for AOC 2025 day X"""

import re
from collections import deque


def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        result = []
        for line in file.readlines():
            a, b = re.match(r'^(.*) (.*) ', line).groups()
            result.append((int(a), int(b)))
        return result


def solve1(parsed):
    """Solve part 1"""
    return 0


def solve2(parsed):
    """Solve part 2"""
    return 0


if __name__ == '__main__':
    parsed = parse('sample.txt')
    print('Day X:', solve1(parsed), solve2(parsed))
