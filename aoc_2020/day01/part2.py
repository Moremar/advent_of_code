def solve(entries):
    for i in range(0, len(entries)-2):
        for j in range(i+1, len(entries)-1):
            for k in range(j+1, len(entries)):
                if entries[i] + entries[j] + entries[k] == 2020:
                    return entries[i] * entries[j] * entries[k]
    raise Exception('Not found')


def parse(file_name):
    with open(file_name, 'r') as f:
        return [int(line) for line in f.readlines()]


if __name__ == '__main__':
    print(solve(parse('data.txt')))