"""Solution for AOC 2024 day 20"""

from collections import deque


def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        world = {}
        start, target = None, None
        for (i, line) in enumerate(file.readlines()):
            for (j, c) in enumerate(line.strip()):
                if c == 'S':
                    start, c = (i, j), '.'
                if c == 'E':
                    target, c = (i, j), '.'
                world[(i, j)] = c
        return start, target, world


def get_path(start, target, world):
    """Get the path from the start to the end of the race"""
    queue = deque([(start, [start])])
    while len(queue) > 0:
        pos, path = queue.popleft()
        if pos == target:
            return path
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_pos = pos[0] + direction[0], pos[1] + direction[1]
            if world[next_pos] == '.' and (len(path) < 2 or next_pos != path[-2]):
                queue.append((next_pos, path + [next_pos]))
    return []


def get_manhattan(a, b):
    """Get the Manhattan distance between 2 positions"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def solve(start, target, world, cheat_time, threshold):
    """Solve part 1 and 2"""
    path = get_path(start, target, world)
    distances = {path[i]: len(path)-i-1 for i in range(len(path))}
    result = 0
    for (i, pos) in enumerate(path[threshold:]):
        for (j, pos2) in enumerate(path[:i]):
            cheat_distance = get_manhattan(pos, pos2)
            if cheat_distance > cheat_time:
                continue
            if distances[start] - (j + cheat_distance + distances[pos]) >= threshold:
                result += 1
    return result


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 20:', solve(*parsed, 2, 100), solve(*parsed, 20, 100))
