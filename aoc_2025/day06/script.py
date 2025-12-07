"""Solution for AOC 2025 day 6"""
import re


def parse1(file_name):
    """Parse the input file for part 1"""
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = [line.strip('\n') for line in file.readlines()]
        operators = re.split(r' +', lines[-1].strip())
        number_rows = [re.split(r' +', line.strip()) for line in lines[:-1]]
        tokens = []
        for j in range(len(number_rows[0])):
            tokens.append([int(number_rows[i][j]) for i in range(len(number_rows))])
        return operators, tokens


def parse2(file_name):
    """Parse the input file for part 2"""
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = [line.strip('\n') for line in file.readlines()]
        # pad lines with spaces, so they all have the same size
        max_line_size = max(len(line) for line in lines)
        for i in range(len(lines)):
            lines[i] += ' ' * (max_line_size - len(lines[i]))
        columns = [''.join([lines[i][j] for i in range(len(lines))]) for j in range(max_line_size)]
        operators = []
        tokens = []
        curr_list = []
        for column in columns:
            if column[-1] in ['+', '*']:
                operators.append(column[-1])
                column = column[:-1]
            column = column.strip()
            if column:
                curr_list.append(int(column))
            else:
                # empty column so this is the beginning of a new list of numbers
                tokens.append(curr_list)
                curr_list = []
        tokens.append(curr_list)
        return operators, tokens


def solve(operators, tokens):
    """Solve parts 1 and 2"""
    total = 0
    for i in range(len(tokens)):
        subtotal = tokens[i][0]
        for j in range(1, len(tokens[i])):
            subtotal = subtotal + tokens[i][j] if operators[i] == '+' else subtotal * tokens[i][j]
        total += subtotal
    return total


if __name__ == '__main__':
    file_name = 'data.txt'
    print('Day 6:', solve(*parse1(file_name)), solve(*parse2(file_name)))
