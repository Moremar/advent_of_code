"""Solution for AOC 2025 day 10"""
import re
from collections import deque
from z3 import Int, Optimize, sat


def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        machines = []
        for line in file.readlines():
            block1, block2, block3 = re.match(r'^\[(.*)\] (.*) \{(.*)\}', line).groups()
            lights = [1 if c == '#' else 0 for c in block1]
            buttons = []
            for token in block2.split(' '):
                buttons.append(set(int(i) for i in token[1:-1].split(',')))
            joltage = [int(i) for i in block3.split(',')]
            machines.append((lights, buttons, joltage))
        return machines


def get_light_button_press(lights, buttons):
    seen = {tuple(0 for _ in lights)}
    to_check = deque([([0] * len(lights), 0)])
    while to_check:
        state, steps = to_check.popleft()
        for button in buttons:
            next_state = list(state)
            for i in button:
                next_state[i] = (next_state[i] + 1) % 2
            if next_state == lights:
                return steps + 1
            key = tuple(next_state)
            if key not in seen:
                seen.add(key)
                to_check.append((next_state, steps + 1))


def solve1(machines):
    """Solve part 1"""
    return sum(get_light_button_press(lights, buttons) for (lights, buttons, _) in machines)


def get_joltage_button_press(joltage, buttons):
    """Get the minimum number of buttons to press to reach the target joltage"""
    s = Optimize()
    for k in range(len(buttons)):
        s.add(Int(f't{k}') >= 0)  # all ti should be positive
    for i in range(len(joltage)):
        s.add(sum(Int(f't{k}') for k in range(len(buttons)) if i in buttons[k]) == joltage[i])
    # configure the solver to minimize the sum of all ti variables
    s.add(sum(Int(f't{k}') for k in range(len(buttons))) == Int('t'))
    s.minimize(Int('t'))
    # we know there is a solution, so the solver check should always be satisfied
    if s.check() == sat:
        return s.model()[Int('t')].as_long()


def solve2(machines):
    """Solve part 2"""
    return sum(get_joltage_button_press(joltage, buttons) for (_, buttons, joltage) in machines)


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 10:', solve1(parsed), solve2(parsed))
