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
    """Check if an update is valid according to a set of rules"""
    return not any(rule[0] in update and
                   rule[1] in update and
                   update.index(rule[0]) > update.index(rule[1])
                   for rule in rules)


def solve1(rules_and_updates):
    """Solve part 1"""
    rules, updates = rules_and_updates
    return sum(update[len(update) // 2] for update in updates if is_valid(update, rules))


def solve2(rules_and_updates):
    """Solve part 2"""
    rules, updates = rules_and_updates
    invalid_rules = [update for update in updates if not is_valid(update, rules)]

    total = 0
    for invalid_rule in invalid_rules:
        while not is_valid(invalid_rule, rules):
            # find the next breached rule and move the 1st page of the rule right before the 2nd
            for rule in rules:
                if rule[0] in invalid_rule and rule[1] in invalid_rule:
                    idx1 = invalid_rule.index(rule[0])
                    idx2 = invalid_rule.index(rule[1])
                    if idx2 < idx1:
                        invalid_rule = invalid_rule[:idx2] + \
                                       [invalid_rule[idx1]] + \
                                       invalid_rule[idx2:idx1] + \
                                       invalid_rule[idx1 + 1:]
            if is_valid(invalid_rule, rules):
                total += invalid_rule[len(invalid_rule) // 2]
                break
    return total


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 05:', solve1(parsed), solve2(parsed))
