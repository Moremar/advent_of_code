#!/usr/bin/env python3
import time

SUGGESTIONS = []


def parse(input_path):
    elves = []
    with open(input_path, 'r') as f:
        for i, line in enumerate(f.readlines()):
            elves += [(i, j) for j in range(len(line)) if line[j] == '#']
    for _ in range(len(elves)):
        SUGGESTIONS.append(None)
    return elves


def get_adj(x, y):
    return [(x-1,y-1), (x-1,y), (x-1,y+1), (x,y-1), (x,y+1), (x+1,y-1), (x+1,y), (x+1,y+1)]


def play_round(round_id, elves, cycle):
    elves_set = set(elves)
    suggested = {}
    for (elf_id, elf) in enumerate(elves):
        suggest = None
        if any([(x, y) in elves_set for (x, y) in get_adj(*elf)]):
            for i in range(round_id, round_id + 4):
                spots = cycle[i % 4](*elf)
                if any([(x, y) in elves_set for (x, y) in spots]):
                    continue
                suggest = spots[1]
                break
        SUGGESTIONS[elf_id] = suggest
        if suggest is not None:
            suggested[suggest] = 1 if suggest not in suggested else 2

    # if no one moves, the operation reached a stable state
    stable = True
    for s in suggested:
        if suggested[s] == 1:
            stable = False
            break

    return [(SUGGESTIONS[elf_id] if SUGGESTIONS[elf_id] is not None and suggested[SUGGESTIONS[elf_id]] == 1
              else elves[elf_id])
              for elf_id in range(len(elves))], stable


def get_cycle():
    return [ lambda x, y : [(x-1,y-1), (x-1,y), (x-1,y+1)],    # NW, N, NE
              lambda x, y : [(x+1,y-1), (x+1,y), (x+1,y+1)],   # SW, S, SE
              lambda x, y : [(x-1,y-1), (x,y-1), (x+1,y-1)],   # NW, W, SW
              lambda x, y : [(x-1,y+1), (x,y+1), (x+1,y+1)] ]  # NE, E, SE


def solve_part1(elves):
    cycle = get_cycle()
    for k in range(10):
        elves, _ = play_round(k, elves, cycle)
    min_i, max_i = min([x for (x, y) in elves]), max([x for (x, y) in elves])
    min_j, max_j = min([y for (x, y) in elves]), max([y for (x, y) in elves])
    return (max_i - min_i + 1) * (max_j - min_j + 1) - len(elves)


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve_part1(parsed)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
