from script1 import parse, Program


def solve(commands):
    pgm = Program(commands, {"a": 1, "b": 0})
    pgm.run()
    return pgm.registers["b"]


if __name__ == '__main__':
    print(solve(parse("data.txt")))
