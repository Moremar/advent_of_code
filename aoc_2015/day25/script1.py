import re


def get_code_index(coord):
    code_index = 0
    for i in range(1, sum(coord) - 1):
        code_index += i
    return code_index + coord[1]


def get_next_code(code):
    return (code * 252533) % 33554393


def solve(coord):
    code_index = get_code_index(coord)
    code = 20151125
    for i in range(1, code_index):
        code = get_next_code(code)
    return code


def parse(file_name):
    with open(file_name, "r") as f:
        _, row, col, _ = re.split(r"row ([0-9]+).* column ([0-9]+).", f.readline())
        return int(row), int(col)


if __name__ == '__main__':
    print(solve(parse("data.txt")))
