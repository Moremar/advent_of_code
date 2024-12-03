"""Solution for AOC 2024 day 2"""

def parse(file_name):
    """Parse the input file"""
    with open(file_name, "r", encoding="utf-8") as file:
        return [list(map(int, line.split())) for line in file.readlines()]


def is_valid1(report):
    """Check if a report is valid"""
    if len(report) > 1:
        asc = report[1] > report[0]
        for i in range(1, len(report)):
            if abs(report[i] - report[i-1]) not in [1, 2, 3] or (report[i] > report[i-1]) != asc:
                return False
    return True


def is_valid2(report):
    """Check if a report is valid with the 1-error tolerance"""
    return is_valid1(report) \
        or any(is_valid1(report[:i] + report[i+1:]) for i in range(len(report)))


def solve1(reports):
    """Solve part 1"""
    return len([1 for report in reports if is_valid1(report)])


def solve2(reports):
    """Solve part 2"""
    return len([1 for report in reports if is_valid2(report)])


if __name__ == '__main__':
    parsed = parse("data.txt")
    print("Day 02:", solve1(parsed), solve2(parsed))
