from part1 import parse


def solve(ids):
    ids.sort()
    for i in range(1, len(ids)):
        if ids[i-1] != ids[i] - 1:
            return ids[i] - 1
    raise Exception('Not found')


if __name__ == '__main__':
    print(solve(parse('data.txt')))
