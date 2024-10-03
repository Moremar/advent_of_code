#!/usr/bin/env python3
import time
import part1


def solve_part2(wind):
    world = set()
    time = rock_id = height = 0
    rock = part1.create_rock(0, 4)
    height_sequence = []

    # Compute the height for the first 5000 rocks
    # we assume that there is a repeating pattern, so we look for the period
    while rock_id < 5000:

        # move horizontally with the wind
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
            for (x, y) in rock.blocks:
                world.add((x, y))
                if y > height:
                    height = y
            height_sequence.append(height)
            rock_id += 1
            rock = part1.create_rock(rock_id % 5, height + 4)
        time += 1

    # find the repeating period
    diff = [height_sequence[i] - height_sequence[i-1] for i in range(1, 5000)]
    period = -1
    for i in range(1001, 4900):
        if all([diff[i + k] == diff[1000 + k] for k in range(100)]):
            period = i - 1000
            break

    # skip the first period as it is a bit irregular until there
    height_per_period = height_sequence[4000] - height_sequence[4000 - period]
    cycle_count = 1000000000000 // period
    similar_rock = 1000000000000 % period

    return height_sequence[similar_rock - 1 + period] + height_per_period * (cycle_count - 1)


if __name__ == "__main__":
    start = time.time()
    parsed = part1.parse("data.txt")
    result = solve_part2(parsed)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
