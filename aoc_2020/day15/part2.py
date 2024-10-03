from part1 import parse, get_nth_number


def solve(starting_numbers):
    return get_nth_number(starting_numbers, 30000000)


if __name__ == "__main__":
    print(solve(parse("data.txt")))
