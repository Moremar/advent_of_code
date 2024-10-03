from script1 import parse, Instruction, order_instructions, exec_instr


def solve(instructions):
    # compute value of "a" wire (part 1)
    wires = {}
    instructions = order_instructions(instructions)
    for instr in instructions:
        exec_instr(instr, wires)
    a_wire = wires["a"]

    # override "b" with the value of "a" calculated above
    instructions = [instr for instr in instructions if instr.res != "b"]
    instructions.insert(0, Instruction("ASSIGN", "b", str(a_wire)))

    # re-execute the instructions
    wires = {}
    for instr in instructions:
        exec_instr(instr, wires)
    return wires["a"]


if __name__ == '__main__':
    print(solve(parse("data.txt")))
