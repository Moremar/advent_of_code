from part1 import parse, next_move


def solve(cups):
    next_cups = {}

    cups = cups + list(range(10, 1000000 + 1))
    for i in range(len(cups)-1):
        next_cups[cups[i]] = cups[i+1]
    next_cups[cups[len(cups)-1]] = cups[0]

    curr = cups[0]
    for i in range(10000000):
        curr = next_move(curr, next_cups)

    return next_cups[1] * next_cups[next_cups[1]]


if __name__ == "__main__":
    print(solve(parse("data.txt")))
