"""Solution for AOC 2024 day 13"""

# Button A moves the crane by (ax, ay), and button B by (bx, by).
# The target position is (tx, ty).
# We need to find the number of times ka and kb to press buttons A and B to reach the target.
# This gives a 2 equations system :
#
# (1) ka * ax + kb * bx = tx
# (2) ka * ay + kb * by = ty
#
# From (2) we get :  (3) kb = (ty - ka * ay) / by
#
# We replace kb by this value in (1) and get :  (3) ka = (tx * by - bx * ty) / (ax * by - ay * bx)
#
# When we find ka, we can replace its value in (3) to find kb.
#
# If ka and kb are positive integers, then the price to reach the target is (3 * ka + kb)

import re


def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        result = []
        for lines_str in file.read().split('\n\n'):
            lines = lines_str.split('\n')
            a = tuple(map(int, re.findall(r'\d+', lines[0])))
            b = tuple(map(int, re.findall(r'\d+', lines[1])))
            c = tuple(map(int, re.findall(r'\d+', lines[2])))
            result.append((a, b, c))
        return result


def price_to_win(machine):
    """Get the price to pay to get the prize if possible, otherwise 0"""
    (ax, ay), (bx, by), (tx, ty) = machine
    ka_top = tx * by - bx * ty
    ka_bottom = ax * by - ay * bx
    if ka_bottom == 0 or ka_top % ka_bottom != 0 or ka_top // ka_bottom < 0:
        return 0
    ka = ka_top // ka_bottom
    kb_top = ty - ka * ay
    kb_bottom = by
    if kb_top % kb_bottom != 0 or kb_top // kb_bottom < 0:
        return 0
    kb = kb_top // kb_bottom
    return 3 * ka + kb


def solve1(machines):
    """Solve part 1"""
    return sum(price_to_win(machine) for machine in machines)


def solve2(machines):
    """Solve part 2"""
    shift = 10000000000000
    return solve1([(m[0], m[1], (m[2][0] + shift, m[2][1] + shift)) for m in machines])


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 13:', solve1(parsed), solve2(parsed))
