"""Solution for AOC 2025 day 1"""

DIRECTIONS = { 'L': -1, 'R': 1 }


def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        return [(DIRECTIONS[line[0]], int(line[1:])) for line in file.readlines()]


def solve1(moves):
    """Solve part 1"""
    value = 50
    zeroes = 0
    for (direction, count) in moves:
        value = (value + count * direction + 100) % 100
        if value == 0:
            zeroes += 1
    return zeroes


def solve2(moves):
    """Solve part 2"""
    value = 50
    zeroes = 0
    for (direction, count) in moves:
        zeroes += count // 100
        count = count % 100
        if count > 0:
            next_value = value + count * direction
            if value != 0 and not 0 < next_value < 100:
                zeroes += 1
            value = (next_value + 100) % 100
    return zeroes


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 01:', solve1(parsed), solve2(parsed))
