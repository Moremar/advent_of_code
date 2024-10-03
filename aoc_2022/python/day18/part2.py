#!/usr/bin/env python3
import collections
import time
import part1


def solve_part2(lava_drops):
    world = set(lava_drops)
    points_in_contact = []   # can contain several times the same point
    internal = set()         # points that are not exposed to the outside
    external = set()         # points that are exposed to the outside
    count = 0

    for lava_drop in lava_drops:
        for adj in part1.get_adj(lava_drop):
            if adj not in world:
                points_in_contact.append(adj)

    # for each air point in contact, check if it is exposed or not to the outside
    # only increment the count if it is
    for adj in points_in_contact:
        if adj in internal:
            continue
        elif adj in external:
            count += 1
        else:
            # need to decide if the point is internal or external
            points = {adj}
            to_check = collections.deque([adj])
            reached_outside = False
            while not reached_outside and len(to_check) > 0:
                curr_point = to_check.popleft()
                for curr_adj in part1.get_adj(curr_point):
                    if curr_adj in world or curr_adj in points:
                        continue
                    elif curr_adj[0] == 0 or curr_adj[1] == 0 or curr_adj[2] == 0:
                        reached_outside = True
                    else:
                        points.add(curr_adj)
                        to_check.append(curr_adj)

            if reached_outside:
                external = external | points
                count += 1
            else:
                internal = internal | points

    return count


if __name__ == "__main__":
    start = time.time()
    parsed = part1.parse("data.txt")
    result = solve_part2(parsed)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
