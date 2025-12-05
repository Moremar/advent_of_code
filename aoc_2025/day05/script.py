"""Solution for AOC 2025 day 5"""
import re

def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        block1, block2 = file.read().split('\n\n')
        fresh = set()
        for line in block1.split('\n'):
            a, b = re.match(r'^(.*)-(.*)', line).groups()
            fresh.add((int(a), int(b)))
        ingredients = {int(line) for line in block2.split('\n')}
    return fresh, ingredients


def solve1(fresh, ingredients):
    """Solve part 1"""
    return len({i for i in ingredients if any(a <= i <= b for (a, b) in fresh)})


def solve2(fresh):
    """Solve part 2"""
    fresh_ranges = dict()
    to_process = set(fresh)
    while to_process:
        (a, b) = to_process.pop()
        for (from_id, to_id) in fresh_ranges.items():
            if a > b:
                # invalid range, skip it
                break
            if from_id <= a <= to_id:
                to_process.add((to_id + 1, b))
                break
            if from_id <= b <= to_id:
                to_process.add((a, from_id - 1))
                break
            if a < from_id <= to_id < b:
                # the range [a, b] contains an existing range
                to_process.add((a, from_id-1))
                to_process.add((to_id+1, b))
                break
        else:
            # the range [a, b] does not intersect with any existing range
            fresh_ranges[a] = b
    return sum(b - a + 1 for (a, b) in fresh_ranges.items())


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 5:', solve1(*parsed), solve2(parsed[0]))
