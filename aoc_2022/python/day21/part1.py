#!/usr/bin/env python3
import time
from operator import add, sub, mul, truediv


class Monkey:
    def __init__(self, name, val):
        self.name = name
        self.val = val
        self.left = self.op = self.right = None


def parse(input_path, match=False):
    parsed = []
    with open(input_path, 'r') as f:
        for line in f.readlines():
            name, rest = line.strip().split(': ')
            if match and 'humn:' in line:
                parsed.append((name, complex(0, 1), None, None, None))
            elif any([c in rest for c in ['+', '-', '*', '/']]):
                parsed.append((name, None, *rest.split(' ')))
            else:
                parsed.append((name, int(rest), None, None, None))

    # need to create all nodes first because one node can be referenced multiple times
    nodes = {name: Monkey(name, val) for (name, val, _, _, _) in parsed}
    for (name, val, left, op, right) in parsed:
        nodes[name].left = None if left is None else nodes[left]
        nodes[name].right = None if right is None else nodes[right]
        nodes[name].op = add if op == '+' \
                    else sub if op == '-' \
                    else mul if op == '*' \
                    else truediv if op == '/' \
                    else None
    return nodes['root']


def compute(tree):
    if tree.val is None:
        tree.val = tree.op(compute(tree.left), compute(tree.right))
    return tree.val


def solve_part1(tree):
    return round(compute(tree))


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve_part1(parsed)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
