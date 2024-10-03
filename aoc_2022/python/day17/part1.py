#!/usr/bin/env python3
import time

ROCKS = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 1), (1, 2), (1, 1), (1, 0), (2, 1)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (0, 1), (1, 0), (1, 1)]
]


class Rock:
    def __init__(self, blocks):
        self. blocks = blocks


def create_rock(rock_type, height):
    return Rock([(x + 3, y + height) for (x, y) in ROCKS[rock_type]])


def parse(input_path):
    with open(input_path, 'r') as f:
        return list(f.read().strip())


def solve_part1(wind):
    world = set()
    time = rock_id = height = 0
    rock = create_rock(0, 4)

    while rock_id < 2022:

        # move horizontally
        shift = 1 if wind[time % len(wind)] == '>' else -1
        next_pos = [(x + shift, y) for (x, y) in rock.blocks]
        valid_move = True
        for (x, y) in next_pos:
            if (x, y) in world or not 1 <= x <= 7 or not y > 0:
                valid_move = False
                break
        if valid_move:
            rock.blocks = next_pos

        # move vertically
        next_pos = [(x, y - 1) for (x, y) in rock.blocks]
        valid_move = True
        for (x, y) in next_pos:
            if (x, y) in world or not 1 <= x <= 7 or not y > 0:
                valid_move = False
                break
        if valid_move:
            rock.blocks = next_pos
        else:
            # the rock comes to rest
            for (x, y) in rock.blocks:
                world.add((x, y))
                if y > height:
                    height = y
            rock_id += 1
            rock = create_rock(rock_id % 5, height + 4)
        time += 1
    return height


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve_part1(parsed)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
