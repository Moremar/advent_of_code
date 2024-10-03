import re


def solve(ids):
    return max(ids)


def parse(file_name):
    ids = []
    with open(file_name, 'r') as f:
        for line in map(str.strip, f.readlines()):
            x, y = re.match(r'^([FB]{7})([LR]{3})$', line.strip()).groups()
            # turn strings of 0 and 1 into their corresponding int
            x = int(x.replace('B', '1').replace('F', '0'), base=2)
            y = int(y.replace('R', '1').replace('L', '0'), base=2)
            ids.append(x * 8 + y)
        return ids


if __name__ == '__main__':
    print(solve(parse('data.txt')))
