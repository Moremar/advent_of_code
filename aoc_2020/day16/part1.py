import re


def valid(val, rule):
    return rule[1] <= val <= rule[2] or rule[3] <= val <= rule[4]


def solve(data):
    rules, _, tickets = data
    error_rate = 0
    for ticket in tickets:
        for val in ticket:
            if not any([valid(val, rule) for rule in rules]):
                error_rate += val
    return error_rate


def parse(file_name):
    with open(file_name, 'r') as f:
        fields = []
        block1, block2, block3 = f.read().split('\n\n')
        for line in block1.split('\n'):
            name, a, b, c, d = re.match(r'([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)$', line).groups()
            fields.append((name, int(a), int(b), int(c), int(d)))
        my_ticket = list(map(int, block2.split('\n')[1].split(',')))
        tickets = []
        for line in block3.split('\n')[1:]:
            tickets.append(list(map(int, line.split(','))))
        return fields, my_ticket, tickets


if __name__ == "__main__":
    print(solve(parse("data.txt")))
