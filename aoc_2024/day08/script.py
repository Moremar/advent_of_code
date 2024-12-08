"""Solution for AOC 2024 day 8"""


def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding="utf-8") as file:
        antennas = {}
        lines = [line.strip() for line in file.readlines()]
        for (i, line) in enumerate(lines):
            for (j, c) in enumerate(line):
                if c != '.':
                    if c not in antennas:
                        antennas[c] = set()
                    antennas[c].add((i, j))
        return antennas, len(lines), len(lines[0])


def add_coords(coord1, coord2):
    """Add 2 2D coordinates"""
    return coord1[0] + coord2[0], coord1[1] + coord2[1]


def sub_coords(coord1, coord2):
    """Subtract 2 2D coordinates"""
    return coord1[0] - coord2[0], coord1[1] - coord2[1]


def solve1(antenna_data):
    """Solve part 1"""
    antennas, row_count, col_count = antenna_data
    antinodes = set()
    for freq in antennas:
        for a1 in antennas[freq]:
            for a2 in antennas[freq]:
                if a1 == a2:
                    continue
                antinode = add_coords(a2, sub_coords(a2, a1))
                if 0 <= antinode[0] < row_count and 0 <= antinode[1] < col_count:
                    antinodes.add(antinode)
    return len(antinodes)


def solve2(antenna_data):
    """Solve part 2"""
    antennas, row_count, col_count = antenna_data
    antinodes = set()
    for freq in antennas:
        for a1 in antennas[freq]:
            for a2 in antennas[freq]:
                if a1 == a2:
                    continue
                antinode = a1
                while 0 <= antinode[0] < row_count and 0 <= antinode[1] < col_count:
                    antinodes.add(antinode)
                    antinode = add_coords(antinode, sub_coords(a1, a2))
    return len(antinodes)


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 08:', solve1(parsed), solve2(parsed))
