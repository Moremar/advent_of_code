"""Solution for AOC 2024 day 10"""

from collections import deque


def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        world = {}
        for (i, line) in enumerate(file.readlines()):
            for (j, c) in enumerate(line.strip()):
                world[(i, j)] = int(c)
        return world


def get_summits(trailhead, world):
    """Get a list of the summit of each trail starting at a given trailhead"""
    summits = []
    positions = deque([trailhead])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while len(positions) > 0:
        pos = positions.popleft()
        for next_position in [(pos[0] + dx, pos[1] + dy) for (dx, dy) in directions]:
            if next_position in world and world[next_position] == world[pos] + 1:
                if world[next_position] == 9:
                    summits.append(next_position)
                else:
                    positions.append(next_position)
    return summits


def solve1(world):
    """Solve part 1"""
    return sum(len(set(get_summits(trailhead, world)))
               for trailhead in world
               if world[trailhead] == 0)


def solve2(world):
    """Solve part 2"""
    return sum(len(get_summits(trailhead, world))
               for trailhead in world
               if world[trailhead] == 0)


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 10:', solve1(parsed), solve2(parsed))
