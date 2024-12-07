"""Solution for AOC 2024 day 7"""

import re


def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding="utf-8") as file:
        equations = []
        for line in file.readlines():
            numbers = list(map(int, re.findall(r'\d+', line)))
            equations.append((numbers[0], numbers[1:]))
        return equations


def has_solution1(equation):
    """Find if an equation has the solution with operators + and *"""
    target, numbers = equation
    if numbers[0] > target:
        return False
    if len(numbers) == 1:
        return numbers[0] == target
    return has_solution1((target, [numbers[0] + numbers[1]] + numbers[2:])) or \
        has_solution1((target, [numbers[0] * numbers[1]] + numbers[2:]))


def has_solution2(equation):
    """Find if an equation has the solution with operators +, * and ||"""
    target, numbers = equation
    if numbers[0] > target:
        return False
    if len(numbers) == 1:
        return numbers[0] == target
    return has_solution2((target, [numbers[0] + numbers[1]] + numbers[2:])) or \
        has_solution2((target, [numbers[0] * numbers[1]] + numbers[2:])) or \
        has_solution2((target, [int(f'{numbers[0]}{numbers[1]}')] + numbers[2:]))


def solve1(equations):
    """Solve part 1"""
    return sum(equation[0] for equation in equations if has_solution1(equation))


def solve2(equations):
    """Solve part 2"""
    return sum(equation[0] for equation in equations if has_solution2(equation))


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 07:', solve1(parsed), solve2(parsed))
