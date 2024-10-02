#!/usr/bin/env python3
import time
from collections import Counter
from functools import cmp_to_key

CARD_VAL = {'2': 2, '3': 3, '4': 4, '5': 5,
            '6': 6, '7': 7, '8': 8, '9': 9,
            'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


def parse(input_path):
    with open(input_path, 'r') as f:
        hands = []
        for line in f.readlines():
            cards, bid = line.strip().split()
            hands.append((list(cards), int(bid)))
        return hands


def get_type(cards):
    counter = Counter(cards).most_common()
    if counter[0][1] == 5:
        return 7  # five of a kind
    elif counter[0][1] == 4:
        return 6  # four of a kind
    elif counter[0][1] == 3 and len(counter) == 2:
        return 5  # full house
    elif counter[0][1] == 3:
        return 4  # three of a kind
    elif counter[0][1] == 2 and len(counter) == 3:
        return 3  # two pairs
    elif counter[0][1] == 2:
        return 2  # one pair
    else:
        return 1  # high card


def hand_comparator(hand1, hand2):
    # order by hand type
    type1, type2 = get_type(hand1[0]), get_type(hand2[0])
    if type1 != type2:
        return 1 if type1 > type2 else -1
    # if same hand type, order by cards in hand
    for i in range(len(hand1[0])):
        if hand1[0][i] != hand2[0][i]:
            return 1 if CARD_VAL[hand1[0][i]] > CARD_VAL[hand2[0][i]] else -1
    return 0


def solve(hands):
    ordered_hands = sorted(hands, key=cmp_to_key(hand_comparator))
    return sum([(i+1) * ordered_hands[i][1] for i in range(len(ordered_hands))])


if __name__ == "__main__":
    start = time.time()
    hands = parse("data.txt")
    result = solve(hands)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')