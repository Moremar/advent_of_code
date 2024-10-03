import re


class Instruction:
    def __init__(self, op, res, param1, param2=None):
        self.op = op
        self.res = res
        self.param1 = param1
        self.param2 = param2
        self.param1_is_int = re.match(r"[0-9]", param1[0])
        self.param2_is_int = param2 is not None and re.match(r"[0-9]", param2[0])


def order_instructions(instructions):
    ordered = []
    known_wires = []
    instrs = list(instructions)  # take a copy since we will remove lines one by one
    while len(instrs):
        instr = instrs.pop(0)
        param1_ok = instr.param1_is_int or instr.param1 in known_wires
        param2_ok = instr.param2 is None or instr.param2_is_int or instr.param2 in known_wires
        if param1_ok and param2_ok:
            ordered.append(instr)
            known_wires.append(instr.res)
        else:
            instrs.append(instr)  # put it back at the end
    return ordered


def exec_instr(instr, wires):
    if instr.op == "ASSIGN":
        val = int(instr.param1) if instr.param1_is_int else wires[instr.param1]
        wires[instr.res] = val
    elif instr.op == "NOT":
        wires[instr.res] = ~ wires[instr.param1]
    elif instr.op == "AND":
        left = int(instr.param1) if instr.param1_is_int else wires[instr.param1]
        right = int(instr.param2) if instr.param2_is_int else wires[instr.param2]
        wires[instr.res] = left & right
    elif instr.op == "OR":
        left = int(instr.param1) if instr.param1_is_int else wires[instr.param1]
        right = int(instr.param2) if instr.param2_is_int else wires[instr.param2]
        wires[instr.res] = left | right
    elif instr.op == "LSHIFT":
        wires[instr.res] = wires[instr.param1] << int(instr.param2)
    elif instr.op == "RSHIFT":
        wires[instr.res] = wires[instr.param1] >> int(instr.param2)


def solve(instructions):
    wires = {}
    for instr in order_instructions(instructions):
        exec_instr(instr, wires)
    return wires["a"]


def parse(file_name):
    with open(file_name, "r") as f:
        instructions = []
        for line in f.readlines():
            if "NOT" in line:
                _, op, param1, res, _ = re.split(r"^(NOT) ([a-z]+) -> ([a-z]+)", line)
                instructions.append(Instruction(op, res, param1))
            elif any(operator in line for operator in ["AND", "OR", "LSHIFT", "RSHIFT"]):
                _, param1, op, param2, res, _ = re.split(r"^([a-z0-9]+) ([A-Z]+) ([a-z0-9]+) -> ([a-z]+)", line)
                instructions.append(Instruction(op, res, param1, param2))
            else:  # assignment
                _, param1, res, _ = re.split(r"^([a-z0-9]+) -> ([a-z]+)", line)
                instructions.append(Instruction("ASSIGN", res, param1))
        return instructions


if __name__ == '__main__':
    print(solve(parse("data.txt")))
