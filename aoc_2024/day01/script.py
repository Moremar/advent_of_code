"""Solution for AOC 2024 day 1"""

from collections import Counter


def parse(file_name):
    """Parse the input file"""
    with open(file_name, "r", encoding="utf-8") as file:
        pairs = [line.split("   ") for line in file.readlines()]
        return [int(pair[0]) for pair in pairs], [int(pair[1]) for pair in pairs]


def solve1(lists):
    """Solve part 1"""
    list1, list2 = lists
    list1.sort()
    list2.sort()
    return sum(abs(list1[i] - list2[i]) for i in range(len(list1)))


def solve2(lists):
    """Solve part 2"""
    list1, list2 = lists
    counter = Counter(list2)
    return sum(list1[i] * counter[list1[i]] for i in range(len(list1)))


if __name__ == '__main__':
    parsed = parse("data.txt")
    print("Day 01:", solve1(parsed), solve2(parsed))
