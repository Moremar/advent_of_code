import re


class Rule:
    def __init__(self, rule_id, rule_type, left=None, right=None, seq=None, literal=None):
        self.rule_id = rule_id
        self.type = rule_type
        self.left = left
        self.right = right
        self.seq = seq
        self.literal = literal
        self.regex = literal


def calculate_regex(rule, rules):
    if rule.regex:
        return
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


def parse_rule(line):
    rule_id, expr = re.match(r'(\d+): (.*)$', line).groups()
    rule_id = int(rule_id)
    if '"' in expr:
        return Rule(rule_id, "NODE", literal=expr[1:2])
    elif '|' in expr:
        left, right = expr.split(' | ')
        left_rule = Rule(None, 'SEQ', seq=list(map(int, left.split(' '))))
        right_rule = Rule(None, 'SEQ', seq=list(map(int, right.split(' '))))
        return Rule(rule_id, 'OR', left=left_rule, right=right_rule)
    else:
        return Rule(rule_id, 'SEQ', seq=list(map(int, expr.split(' '))))


def parse(file_name):
    with open(file_name, 'r') as f:
        rules_lines, messages_lines = f.read().split('\n\n')
        rules = {}
        for line in rules_lines.split('\n'):
            rule = parse_rule(line.strip())
            rules[rule.rule_id] = rule
        return rules, [line.strip() for line in messages_lines.split('\n')]


if __name__ == "__main__":
    print(solve(parse("data.txt")))
