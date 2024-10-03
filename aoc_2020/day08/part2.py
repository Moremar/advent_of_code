from part1 import parse, Compiler


def solve(instructions):
    for i in range(len(instructions)):
        if instructions[i][0] == 'acc':
            continue
        updated = list(instructions)
        new_op = 'jmp' if instructions[i][0] == 'nop' else 'nop'
        updated[i] = (new_op, instructions[i][1])
        (success, val) = Compiler(updated).run()
        if success:
            return val


if __name__ == "__main__":
    print(solve(parse("data.txt")))
