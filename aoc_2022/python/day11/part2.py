#!/usr/bin/env python3
import time
import part1

# without the "divide by 3" operation, we get unmanageably big worry levels
# we do not need to work with these actual numbers, since all we care about to
# decide which monkey will receive each item is whether or not the number is divisible
# by each monkey's test value
# instead of using the actual number, we can just use its remainder modulo LCM
# (least common multiple of all monkeys' test values)
# since all monkeys test values are prime, the LCM is the product of distinct values


def solve_part2(monkeys):
    lcm = 1
    for prime in set([m.dest[0] for m in monkeys]):
        lcm *= prime

    for i in range(10000):
        for monkey in monkeys:
            while len(monkey.items):
                monkey.inspected += 1
                item = monkey.items[0]
                monkey.items = monkey.items[1:]
                val = item if monkey.op[1] == 'old' else int(monkey.op[1])
                worry = item + val if monkey.op[0] == 'ADD' else item * val
                worry = worry % lcm
                next_monkey = monkey.dest[1] if worry % monkey.dest[0] == 0 else monkey.dest[2]
                monkeys[next_monkey].items.append(worry)
    inspected = sorted([monkey.inspected for monkey in monkeys], reverse=True)
    return inspected[0] * inspected[1]


if __name__ == "__main__":
    start = time.time()
    parsed = part1.parse("data.txt")
    result = solve_part2(parsed)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
