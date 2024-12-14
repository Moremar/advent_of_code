"""Solution for AOC 2024 day 14"""

import re


def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        return [tuple(map(int, re.findall(r'-?\d+', line))) for line in file.readlines()]


def solve1(robots):
    """Solve part 1"""
    max_x = max(robot[0] for robot in robots)
    max_y = max(robot[1] for robot in robots)
    positions = [((px + 100 * vx) % (max_x + 1), (py + 100 * vy) % (max_y + 1))
                 for (px, py, vx, vy) in robots]

    return sum(1 for (x, y) in positions if x < max_x // 2 and y < max_y // 2) \
        * sum(1 for (x, y) in positions if x > max_x // 2 and y < max_y // 2) \
        * sum(1 for (x, y) in positions if x < max_x // 2 and y > max_y // 2) \
        * sum(1 for (x, y) in positions if x > max_x // 2 and y > max_y // 2)


def count_neighbors(pos, positions):
    return sum(positions[(pos[0] + i, pos[1] + j)]
               for i in [-1, 0, 1]
               for j in [-1, 0, 1]
               if not i == j == 0 and (pos[0] + i, pos[1] + j) in positions)


def solve2(robots):
    """Solve part 2"""
    max_x = max(robot[0] for robot in robots)
    max_y = max(robot[1] for robot in robots)
    i = 0
    while True:
        i += 1
        positions = {}
        for (px, py, vx, vy) in robots:
            pos = ((px + i * vx) % (max_x + 1), (py + i * vy) % (max_y + 1))
            positions[pos] = 1 + (positions[pos] if pos in positions else 0)
        # the density of robots should be much higher when they form a tree
        # we detect if by checking when robots have an average of over 2 neighbors
        if sum(count_neighbors(pos, positions) for pos in positions) > 2 * len(robots):
            return i


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 14:', solve1(parsed), solve2(parsed))
