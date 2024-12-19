"""Solution for AOC 2024 day 19"""

CACHE = {}


def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        available, patterns = file.read().split('\n\n')
        return available.split(', '), [line.strip() for line in patterns.split('\n')]


def count_combinations(pattern, available):
    """Count the number of combinations to create a pattern with the available designs"""
    if len(pattern) == 0:
        return 1
    if pattern not in CACHE:
        CACHE[pattern] = sum(count_combinations(pattern[len(a):], available)
                             for a in available
                             if len(a) <= len(pattern) and pattern[:len(a)] == a)
    return CACHE[pattern]


def solve1(available, patterns):
    """Solve part 1"""
    return len([pattern for pattern in patterns if count_combinations(pattern, available) > 0])


def solve2(available, patterns):
    """Solve part 2"""
    return sum(count_combinations(pattern, available) for pattern in patterns)


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 19:', solve1(*parsed), solve2(*parsed))
