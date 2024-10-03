#!/usr/bin/env python3
import time
import part1


def solve_part2(instructions):
    snake = [(0, 0) for _ in range(10)]
    visited = set()
    for (move, steps) in instructions:
        for k in range(steps):
            snake[-1] = snake[-1][0] + move[0], snake[-1][1] + move[1]
            for bit in range(9):
                front_knot = snake[-1-bit]
                rear_knot = snake[-1-bit-1]
                snake[-1-bit-1] = part1.next_tail_pos(front_knot, rear_knot)
            visited.add(snake[0])
    return len(visited)


if __name__ == "__main__":
    start = time.time()
    parsed = part1.parse("data.txt")
    result = solve_part2(parsed)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
