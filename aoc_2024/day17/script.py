"""Solution for AOC 2024 day 17"""
import math
import re


def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines()]
        return {'A': int(re.search(r'\d+', lines[0]).group()),
                'B': int(re.search(r'\d+', lines[1]).group()),
                'C': int(re.search(r'\d+', lines[2]).group())
                }, list(map(int, re.findall(r'\d+', lines[4])))


def combo(operand, registers):
    """Get the combo value of a digit"""
    if operand == 4:
        return registers['A']
    if operand == 5:
        return registers['B']
    if operand == 6:
        return registers['C']
    return operand


def execute(registers, instructions, position, output):
    """Execute a single instruction"""
    opcode, operand = instructions[position], instructions[position + 1]
    if opcode == 0:  # adv
        registers['A'] = registers['A'] // int(math.pow(2, combo(operand, registers)))
    if opcode == 1:  # bxl
        registers['B'] = registers['B'] ^ operand
    if opcode == 2:  # bst
        registers['B'] = combo(operand, registers) % 8
    if opcode == 3:  # jnz
        if registers['A'] != 0:
            return operand
    if opcode == 4:  # bxc
        registers['B'] = registers['B'] ^ registers['C']
    if opcode == 5:  # out
        output.append(combo(operand, registers) % 8)
    if opcode == 6:  # bdv
        registers['B'] = registers['A'] // int(math.pow(2, combo(operand, registers)))
    if opcode == 7:  # cdv
        registers['C'] = registers['A'] // int(math.pow(2, combo(operand, registers)))
    return position + 2


def solve1(registers_init, instructions):
    """Solve part 1"""
    position = 0
    output = []
    registers = dict(registers_init)
    while 0 <= position < len(instructions) - 1:
        position = execute(registers, instructions, position, output)
    return ','.join(map(str, output))


def solve2(registers_init, instructions):
    """Solve part 2"""

    # The value of A that produces the original program in its output is too high
    # to be brute-forced, so we need to reverse-engineer the program:
    #
    # 1)   2,4    B = A % 8
    # 2)   1,7    B = B xor 7
    # 3)   7,5    C = A / 2^B
    # 4)   1,7    B = B xor 7
    # 5)   0,3    A = A / 8
    # 6)   4,1    B = B xor C
    # 7)   5,5    print B % 8
    # 8)   3,0    go to 1) if A != 0
    #
    # We notice that the program is a big loop of instructions 1) to 8) that stops when A is 0.
    # At each loop iteration, one value is sent to the output and A is divided by 8 (3 bits).
    # This means that the last digit in the output only depends on the last 3 bits, then the
    # previous digits depends on the last 6 bits, etc...
    # This way we can find the possible solution by brute-forcing the possibilities from the last
    # digit to the first digit by checking the generated digit at each step.

    results = [0]
    next_results = []
    for target_digit in instructions[::-1]:
        next_results = []
        for partial_result in results:
            for i in range(8):
                if partial_result == 0 and i == 0:
                    continue
                registers = dict(registers_init)
                registers['A'] = partial_result * 8 + i
                position = 0
                output = []
                while 0 <= position < len(instructions) - 1:
                    position = execute(registers, instructions, position, output)
                if output[0] == target_digit:
                    next_results.append(8 * partial_result + i)
            results = next_results
    return next_results[0]


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 17:', solve1(*parsed), solve2(*parsed))
