"""Solution for AOC 2024 day 12"""

from collections import deque


def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines()]
        return {(i, j): c for (i, line) in enumerate(lines) for (j, c) in enumerate(line)}


def get_adjacent(x):
    """Get the 4 plots adjacent to a given plot"""
    return [(x[0] + dx, x[1] + dy) for (dx, dy) in [(0, 1), (1, 0), (0, -1), (-1, 0)]]


def get_region(plot, world):
    """Get the region including a given plot"""
    region = {plot}
    to_process = deque([plot])
    while len(to_process) > 0:
        curr = to_process.popleft()
        for adj in get_adjacent(curr):
            if adj in world and world[adj] == world[curr] and adj not in region:
                region.add(adj)
                to_process.append(adj)
    return region


def get_regions(world):
    """Get all the regions in the map"""
    seen = set()
    regions = []
    for i in range(max(i for (i, _) in world) + 1):
        for j in range(max(j for (_, j) in world) + 1):
            if (i, j) not in seen:
                region = get_region((i, j), world)
                regions.append(region)
                seen = seen.union(region)
    return regions


def get_perimeter(region):
    """Get the perimeter of a region"""
    return sum(1 for plot in region for adj in get_adjacent(plot) if adj not in region)


def get_sides(region):
    """Get the number of sides of a region"""
    fences = {(plot, adj) for plot in region for adj in get_adjacent(plot) if adj not in region}
    done = set()
    sides = 0
    for fence in fences:
        if fence not in done:
            sides += 1
            done.add(fence)
            # mark all other parts of this fence (both directions) as done
            for shift in (-1, 1):
                curr = fence
                while curr in fences:
                    if curr[0][0] == curr[1][0]:  # vertical fence
                        curr = (curr[0][0] + shift, curr[0][1]), (curr[1][0] + shift, curr[1][1])
                    else:  # horizontal fence
                        curr = (curr[0][0], curr[0][1] + shift), (curr[1][0], curr[1][1] + shift)
                    done.add(curr)
    return sides


def solve1(world):
    """Solve part 1"""
    return sum(len(region) * get_perimeter(region) for region in get_regions(world))


def solve2(world):
    """Solve part 2"""
    return sum(len(region) * get_sides(region) for region in get_regions(world))


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 12:', solve1(parsed), solve2(parsed))
