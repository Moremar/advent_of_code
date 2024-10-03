#!/usr/bin/env python3
import time
import part1


def find_min_folder_size(folder, target):
    assert folder.size >= target
    candidates = [folder.size]
    for f in folder.folders:
        if f.size >= target:
            candidates.append(find_min_folder_size(f, target))
    return min(candidates)


def solve_part2(commands):
    root = part1.build_tree(commands)
    target = 30000000 - (70000000 - root.size)
    return find_min_folder_size(root, target)


if __name__ == "__main__":
    start = time.time()
    parsed = part1.parse("data.txt")
    result = solve_part2(parsed)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
