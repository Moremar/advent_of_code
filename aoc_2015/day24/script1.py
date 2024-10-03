from math import inf


def compute_groups(target, choices, so_far, groups):
    if target == 0:
        groups.append(so_far)
    elif len(choices) == 0:
        return []
    elif choices[0] > target:
        compute_groups(target, choices[1:], so_far, groups)
    else:
        compute_groups(target, choices[1:], so_far, groups)
        compute_groups(target - choices[0], choices[1:], so_far + [choices[0]], groups)


def best_entanglement(groups):
    best = inf
    for group in groups:
        entanglement = 1
        for elem in group:
            entanglement *= elem
        if entanglement < best:
            best = entanglement
    return best


def solve(weights):
    group_weight = sum(weights) / 3
    groups = []
    compute_groups(group_weight, weights, [], groups)
    groups.sort(key=lambda g: len(g))
    return best_entanglement([g for g in groups if len(g) == len(groups[0])])


def parse(file_name):
    with open(file_name, "r") as f:
        return [int(line.strip()) for line in f.readlines()]


if __name__ == '__main__':
    print(solve(parse("data.txt")))
