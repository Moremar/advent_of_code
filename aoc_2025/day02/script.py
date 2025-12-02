"""Solution for AOC 2025 day 2"""

import re


def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        return [re.match(r'^(\d+)-(\d+)$', line).groups() for line in file.readlines()[0].split(',')]



def solve1(ranges):
    """Solve part 1"""
    total = 0
    for (range_start, range_end) in ranges:
        for i in range(int(range_start), int(range_end)+1):
            i_str = str(i)
            if i_str == i_str[:len(i_str)//2] * 2:
                total += i
    return total

def solve2(ranges):
    """Solve part 2"""
    total = 0
    for (range_start, range_end) in ranges:
        for i in range(int(range_start), int(range_end)+1):
            i_str = str(i)
            for cycle_count in range(2, (len(i_str) + 1)):
                if i_str == i_str[:len(i_str)//cycle_count] * cycle_count:
                    total += i
                    break
    return total


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 2:', solve1(parsed), solve2(parsed))
