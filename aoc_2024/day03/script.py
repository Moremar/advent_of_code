import re


def parse(file_name):
    with open(file_name, 'r') as file:
        pattern = 'mul\\(\\d+,\\d+\\)|don\'t\\(\\)|do\\(\\)'
        instructions = []
        for block in re.findall(pattern, file.read()):
            if block[:3] == 'mul':
                instructions.append(('mul', int(block.split(',')[0][4:]), int(block.split(',')[1][:-1])))
            else:  # "do" or "don't"
                instructions.append((block.split('(')[0], -1, -1))
        return instructions


def solve1(instructions):
    return sum(a * b for (op, a, b) in instructions if op == 'mul')


def solve2(instructions):
    result = 0
    active = True
    for instr in instructions:
        if instr[0] in ['do', 'don\'t']:
            active = (instr[0] == 'do')
        elif active:
            result += instr[1] * instr[2]
    return result


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 03:', solve1(parsed), solve2(parsed))
