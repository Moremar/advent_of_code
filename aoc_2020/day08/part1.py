import re


class Compiler:
    def __init__(self, instructions):
        self.instructions = instructions
        self.val = 0
        self.ptr = 0

    def run(self):
        seen = []
        while True:
            if self.ptr >= len(self.instructions):
                return True, self.val
            if self.ptr in seen:
                return False, self.val
            seen.append(self.ptr)
            (op, arg) = self.instructions[self.ptr]
            if op == 'acc':
                self.val += int(arg)
                self.ptr += 1
            elif op == 'jmp':
                self.ptr += int(arg)
            elif op == 'nop':
                self.ptr += 1


def solve(instructions):
    return Compiler(instructions).run()[1]


def parse(file_name):
    instructions = []
    with open(file_name, 'r') as f:
        for line in f.readlines():
            instructions.append(re.match(r'([a-z]+) (.*)$', line.strip()).groups())
        return instructions


if __name__ == "__main__":
    print(solve(parse("data.txt")))
