from part1 import parse, eval
import re


def eval_flat(expression):
    while '+' in expression:
        match = re.search(r'(\d+)\+(\d+)', expression)
        a, b, pos1, pos2 = match.group(1), match.group(2), match.span()[0], match.span()[1]
        res = int(a) + int(b)
        expression = expression[:pos1] + str(res) + expression[pos2:]
    while '*' in expression:
        match = re.search(r'(\d+)\*(\d+)', expression)
        a, b, pos1, pos2 = match.group(1), match.group(2), match.span()[0], match.span()[1]
        res = int(a) * int(b)
        expression = expression[:pos1] + str(res) + expression[pos2:]
    return expression


def solve(expressions):
    return sum([eval(expression, eval_flat) for expression in expressions])


if __name__ == "__main__":
    print(solve(parse("data.txt")))
