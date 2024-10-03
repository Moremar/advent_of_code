import re


def get_deepest_block(expression):
    depth, max_depth, max_depth_open, max_depth_close, in_max_depth = 0, -1, -1, -1, False
    for (i, c) in enumerate(expression):
        if c == '(':
            depth += 1
            if depth > max_depth:
                max_depth, max_depth_open, in_max_depth = depth, i, True
        elif c == ')':
            depth -= 1
            if in_max_depth:
                max_depth_close = i
                in_max_depth = False
    return max_depth_open, max_depth_close


def eval_flat(expression):
    while '*' in expression or '+' in expression:
        match = re.match(r'((\d+)([+*])(\d+))', expression)
        block, a, op, b = match.groups()
        res = int(a) + int(b) if op == '+' else int(a) * int(b)
        expression = str(res) + expression[len(block):]
    return expression


def eval(expression, eval_flat_fn):
    while '(' in expression:
        pos1, pos2 = get_deepest_block(expression)
        expression = expression[:pos1] + eval_flat_fn(expression[pos1+1:pos2]) + expression[pos2+1:]
    return int(expression)


def solve(expressions):
    return sum([eval(expression, eval_flat) for expression in expressions])


def parse(file_name):
    with open(file_name, 'r') as f:
        return ['(' + line.strip().replace(' ', '') + ')' for line in f.readlines()]


if __name__ == "__main__":
    print(solve(parse("data.txt")))
