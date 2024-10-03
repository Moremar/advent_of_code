import math
from part1 import parse, get_diff_sequence

# All combinations must be in increasing order with no less than 3 jolts difference
# between 2 successive values.
# For every 3 jolts difference, the values before and after the jump must be in every combination.
# This means that the only parts that will change from a combination to another are the sequences of
# several values with just 1 jolt difference.
# We need to count the number of combinations for each sequence of consecutive 1 jolt differences
# and multiply them together to get the total number of combinations.


def count_combinations(size, jolt_diff):
    if size < 2:
        return 1

    # if we reached 3 jolts difference with the previous value, we must include this value
    if jolt_diff == 3:
        return count_combinations(size-1, 1)

    # include or not the current value
    return count_combinations(size-1, 1) + count_combinations(size-1, jolt_diff+1)


def solve(jolts):
    diffs = get_diff_sequence(jolts)
    seqs_of_1 = ''.join(map(str, diffs)).split('3')
    combinations = [count_combinations(len(seq), 1) for seq in seqs_of_1]
    return math.prod(combinations)


if __name__ == "__main__":
    print(solve(parse("data.txt")))