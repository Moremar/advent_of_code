import re
from part1 import parse


def calculate_regex(rule, rules):
    if rule.regex:
        return
    if rule.rule_id == 8:
        calculate_regex(rules[42], rules)
        rule.regex = '(' + rules[42].regex + ')+'
    elif rule.rule_id == 11:
        calculate_regex(rules[42], rules)
        calculate_regex(rules[31], rules)
        block42 = '(' + rules[42].regex + ')'
        block31 = '(' + rules[31].regex + ')'
        # hack to get a mirror regex with X blocks 42 followed by the same number of blocks 31
        mirror = [block42 + '{' + str(i) + '}' + block31 + '{' + str(i) + '}' for i in range(1, 10)]
        rule.regex = '(' + '|'.join(mirror) + ')'
    elif rule.type == "SEQ":
        for i in rule.seq:
            calculate_regex(rules[i], rules)
        rule.regex = ''.join(rules[i].regex for i in rule.seq)
    elif rule.type == "OR":
        calculate_regex(rule.left, rules)
        calculate_regex(rule.right, rules)
        rule.regex = '(' + rule.left.regex + '|' + rule.right.regex + ')'


def solve(data):
    rules, messages = data
    calculate_regex(rules[0], rules)
    return len([1 for message in messages if re.match(rules[0].regex + '$', message)])


if __name__ == "__main__":
    print(solve(parse("data.txt")))
