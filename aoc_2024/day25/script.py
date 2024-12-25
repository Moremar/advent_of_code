"""Solution for AOC 2024 day 25"""


def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        locks, keys = [], []
        for schema in file.read().split('\n\n'):
            lines = schema.split('\n')
            if schema[0] == '#':
                locks.append([max(i for i in range(7) if lines[i][j] == '#') for j in range(5)])
            else:
                keys.append([6 - min(i for i in range(7) if lines[i][j] == '#') for j in range(5)])
        return locks, keys


def solve1(locks, keys):
    """Solve part 1"""
    return sum(1 if all(key[j] + lock[j] <= 5 for j in range(5)) else 0
               for lock in locks
               for key in keys)


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 25:', solve1(*parsed))
