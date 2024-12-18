"""Solution for AOC 2024 day 18"""

from collections import deque
import re


def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        return [tuple(map(int, re.findall(r'\d+', line))) for line in file.readlines()]


def get_steps_to_exit(falling_bytes, map_size, fallen_byte_count):
    """Get the minimum number of steps to the exit, -1 if not reachable"""
    blocked = set(falling_bytes[0:fallen_byte_count])
    target = (map_size, map_size)
    to_check = deque([((0, 0), 0)])
    seen = {}
    while len(to_check) > 0:
        (curr_pos, curr_steps) = to_check.popleft()
        if curr_pos in seen:
            continue
        seen[curr_pos] = curr_steps
        if curr_pos == target:
            return curr_steps
        for direction in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            adj = curr_pos[0] + direction[0], curr_pos[1] + direction[1]
            if adj in blocked or not 0 <= adj[0] <= map_size or not 0 <= adj[1] <= map_size:
                continue
            to_check.append((adj, curr_steps + 1))
    return -1


def solve1(falling_bytes, map_size, fallen_byte_count):
    """Solve part 1"""
    return get_steps_to_exit(falling_bytes, map_size, fallen_byte_count)


def solve2(falling_bytes, map_size, fallen_byte_count):
    """Solve part 2"""
    for i in range(fallen_byte_count, len(falling_bytes)):
        if get_steps_to_exit(falling_bytes, map_size, i) == -1:
            return falling_bytes[i-1]
    return 0


if __name__ == '__main__':
    parsed = parse('data.txt')
    MAP_SIZE = 70
    FALLEN_BYTE_COUNT = 1024
    print('Day 18:', solve1(parsed, MAP_SIZE, FALLEN_BYTE_COUNT),
                     solve2(parsed, MAP_SIZE, FALLEN_BYTE_COUNT))
