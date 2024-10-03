#!/usr/bin/env python3
import time


class Monkey:
    def __init__(self, items, op, dest):
        self.items = items
        self.op = op
        self.dest = dest
        self.inspected = 0

    def __repr__(self):
        return f'Monkey({self.items}, {self.op}, {self.dest}, {self.inspected})'


def parse(input_path):
    monkeys = []
    with open(input_path, 'r') as f:
        for block in f.read().split('\n\n'):
            lines = block.split('\n')
            items = list(map(int, lines[1].split(': ')[1].split(', ')))
            op = 'ADD' if lines[2].split('old ')[1][0] == '+' else 'MUL', lines[2].split('old ')[1][1:].strip()
            dest = (int(lines[3].split('by')[1]), int(lines[4].split('key')[1]), int(lines[5].split('key')[1]))
            monkeys.append(Monkey(items, op, dest))
    return monkeys


def solve_part1(monkeys):
    for _ in range(20):
        for monkey in monkeys:
            while len(monkey.items):
                monkey.inspected += 1
                item = monkey.items[0]
                monkey.items = monkey.items[1:]
                val = item if monkey.op[1] == 'old' else int(monkey.op[1])
                worry = item + val if monkey.op[0] == 'ADD' else item * val
                worry //= 3
                next_monkey = monkey.dest[1] if worry % monkey.dest[0] == 0 else monkey.dest[2]
                monkeys[next_monkey].items.append(worry)
    inspected = sorted([monkey.inspected for monkey in monkeys], reverse=True)
    return inspected[0] * inspected[1]


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve_part1(parsed)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
