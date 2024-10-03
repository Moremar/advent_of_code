def get_combinations(curr_combination, recipients, target, combinations):
    if len(recipients) == 0:
        if target == 0:
            combinations.append(curr_combination)
    elif recipients[0] > target:
        get_combinations(curr_combination + [0], recipients[1:], target, combinations)
    else:
        get_combinations(curr_combination + [0], recipients[1:], target, combinations)
        get_combinations(curr_combination + [1], recipients[1:], target - recipients[0], combinations)


def solve(recipients):
    combinations = []
    get_combinations([], recipients, 150, combinations)
    return len(combinations)


def parse(file_name):
    with open(file_name, "r") as f:
        return [int(line.strip()) for line in f.readlines()]


if __name__ == '__main__':
    print(solve(parse("data.txt")))
