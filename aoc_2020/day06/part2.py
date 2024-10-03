from part1 import parse


def solve(answers):
    return sum([len([c for c in counter if counter[c] == people]) for (people, counter) in answers])


if __name__ == '__main__':
    print(solve(parse('data.txt')))
