#!/usr/bin/env python3
import time


class Node:
    def __init__(self, id, val, prev=None):
        self.id = id
        self.val = val
        self.prev = prev
        self.next = None


def parse(input_path, decryption_key):
    with open(input_path, 'r') as f:
        count = 0
        start = None
        curr = None
        # build the linked-list
        for val in [decryption_key * int(line) for line in f.readlines()]:
            curr = Node(count, val, curr)
            count += 1
            if start is None:
                start = curr
            else:
                curr.prev.next = curr  # bidirectional-link
        # close the loop
        curr.next = start
        start.prev = curr
        return count, start


def solve_part1(parsed, loops):
    count, curr = parsed
    for k in range(loops):
        for i in range(count):
            # find the node to move
            while curr.id != i:
                curr = curr.next
            shift = curr.val % (count - 1)
            if shift == 0:
                continue
            if shift > (count - 1)//2 :
                shift -= (count - 1)
            # find the position it should go to
            next_pos = curr
            if shift > 0:
                for _ in range(shift + 1):
                    next_pos = next_pos.next
            else:
                for _ in range(-shift):
                    next_pos = next_pos.prev
            # re-arrange the links between curr and its next position
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            curr.prev = next_pos.prev
            curr.prev.next = curr
            curr.next = next_pos
            next_pos.prev = curr

    # done with all permutations, calculate the result
    while curr.val != 0:
        curr = curr.next
    res = 0
    for i in range(3):
        for _ in range(1000):
            curr = curr.next
        res += curr.val
    return res


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt", 1)
    result = solve_part1(parsed, 1)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')