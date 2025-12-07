"""Solution for AOC 2025 day 7"""
from collections import defaultdict


def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        splitters = set()
        for (i, line) in enumerate(file.readlines()):
            for (j, c) in enumerate(line):
                if c == 'S':
                    start = (i, j)
                elif c == '^':
                    splitters.add((i, j))
        return start, splitters


def solve1(start, splitters):
    """Solve part 1"""
    max_i = max(i for (i, j) in splitters)
    curr_i = start[0]
    rays = {curr_i: {start[1]}}
    splits = 0
    while curr_i <= max_i:
        rays[curr_i + 1] = set()
        for ray_j in rays[curr_i]:
            if (curr_i + 1, ray_j) in splitters:
                rays[curr_i + 1].add(ray_j - 1)
                rays[curr_i + 1].add(ray_j + 1)
                splits += 1
            else:
                rays[curr_i + 1].add(ray_j)
        curr_i += 1
    return splits


def solve2(start, splitters):
    """Solve part 2"""
    max_i = max(i for (i, j) in splitters)
    curr_i = start[0]
    timelines = {curr_i: {start[1]: 1}}
    while curr_i <= max_i:
        timelines[curr_i + 1] = defaultdict(int)
        for timeline_j in timelines[curr_i]:
            if (curr_i+1, timeline_j) in splitters:
                timelines[curr_i + 1][timeline_j - 1] += timelines[curr_i][timeline_j]
                timelines[curr_i + 1][timeline_j + 1] += timelines[curr_i][timeline_j]
            else:
                timelines[curr_i + 1][timeline_j] += timelines[curr_i][timeline_j]
        curr_i += 1
    return sum(timelines[curr_i][j] for j in timelines[curr_i])


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 7:', solve1(*parsed), solve2(*parsed))
