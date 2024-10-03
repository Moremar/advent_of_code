def solve(entries):
    for i in range(0, len(entries)-1):
        for j in range(i+1, len(entries)):
            if entries[i] + entries[j] == 2020:
                return entries[i] * entries[j]
    raise Exception('Not found')


def parse(file_name):
    with open(file_name, 'r') as f:
        return [int(line) for line in f.readlines()]


if __name__ == '__main__':
    print(solve(parse('data.txt')))