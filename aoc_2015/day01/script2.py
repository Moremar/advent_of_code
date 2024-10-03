from script1 import parse


def solve(line):
    floor = 0
    step = 1
    for c in line:
        floor += 1 if c == "(" else -1
        if floor == -1:
            return step
        step += 1


if __name__ == '__main__':
    print(solve(parse("data.txt")))
