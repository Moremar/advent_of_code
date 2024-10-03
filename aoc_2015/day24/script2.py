from script1 import parse, compute_groups, best_entanglement


def solve(weights):
    group_weight = sum(weights) / 4
    groups = []
    compute_groups(group_weight, weights, [], groups)
    groups.sort(key=lambda g: len(g))
    return best_entanglement([g for g in groups if len(g) == len(groups[0])])


if __name__ == '__main__':
    print(solve(parse("data.txt")))
