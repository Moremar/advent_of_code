"""Solution for AOC 2024 day 5"""


def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        rules = []
        updates = []
        rules_block, updates_block = file.read().split('\n\n')
        for line in rules_block.split('\n'):
            x, y = line.split('|')
            rules.append((int(x), int(y)))
        for line in updates_block.split('\n'):
            updates.append(list(map(int, line.split(','))))
        return rules, updates


def is_valid(update, rules):
    return not any(rule[0] in update and
                   rule[1] in update and
                   update.index(rule[0]) > update.index(rule[1])
                   for rule in rules)


def solve1(parsed):
    """Solve part 1"""
    rules, updates = parsed
    return sum(update[len(update) // 2] for update in updates if is_valid(update, rules))


def solve2(parsed):
    """Solve part 2"""
    rules, updates = parsed
    invalid_rules = [update for update in updates if not is_valid(update, rules)]

    total = 0
    for i in range(len(invalid_rules)):
        while not is_valid(invalid_rules[i], rules):
            # find the next breached rule and move the 1st page of the rule right before the 2nd
            for rule in rules:
                if rule[0] in invalid_rules[i] and rule[1] in invalid_rules[i]:
                    idx1 = invalid_rules[i].index(rule[0])
                    idx2 = invalid_rules[i].index(rule[1])
                    if idx2 < idx1:
                        invalid_rules[i] = (invalid_rules[i][:idx2] +
                                            [invalid_rules[i][idx1]] +
                                            invalid_rules[i][idx2:idx1] +
                                            invalid_rules[i][idx1 + 1:])
            if is_valid(invalid_rules[i], rules):
                total += invalid_rules[i][len(invalid_rules[i]) // 2]
                break
    return total


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 05:', solve1(parsed), solve2(parsed))
