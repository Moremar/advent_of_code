#!/usr/bin/env python3
import collections
import time
import part1


def solve_part2(stacks, moves):
    for (nb, src, dest) in moves:
        tmp = collections.deque()
        for _ in range(nb):
            tmp.append(stacks[src-1].pop())
        for _ in range(nb):
            stacks[dest-1].append(tmp.pop())
    return ''.join([stack.pop() for stack in stacks])


if __name__ == "__main__":
    start = time.time()
    parsed = part1.parse("data.txt")
    result = solve_part2(*parsed)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
