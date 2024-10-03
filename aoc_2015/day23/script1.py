import re


class Command:
    def __init__(self, name, register, jump_addr=None):
        self.name = name
        self.register = register
        self.jump_addr = jump_addr


class Program:
    def __init__(self, commands, registers):
        self.commands = commands
        self.registers = registers
        self.instr_ptr = 0

    def exec_next_command(self):
        cmd = self.commands[self.instr_ptr]
        if cmd.name == "hlf":
            self.registers[cmd.register] //= 2
            self.instr_ptr += 1
        elif cmd.name == "tpl":
            self.registers[cmd.register] *= 3
            self.instr_ptr += 1
        elif cmd.name == "inc":
            self.registers[cmd.register] += 1
            self.instr_ptr += 1
        elif cmd.name == "jmp":
            self.instr_ptr += cmd.jump_addr
        elif cmd.name == "jie":
            self.instr_ptr += cmd.jump_addr if self.registers[cmd.register] % 2 == 0 else 1
        elif cmd.name == "jio":
            self.instr_ptr += cmd.jump_addr if self.registers[cmd.register] == 1 else 1
        else:
            raise ValueError("Unsupported command: ", cmd.name)

    def run(self):
        while self.instr_ptr < len(self.commands):
            self.exec_next_command()


def solve(commands):
    pgm = Program(commands, {"a": 0, "b": 0})
    pgm.run()
    return pgm.registers["b"]


def parse(file_name):
    with open(file_name, "r") as f:
        commands = []
        for line in f.readlines():
            if any([cmd in line for cmd in ["inc", "tpl", "hlf"]]):
                _, cmd, r, _ = re.split(r"([a-z]+) ([a|b])", line)
                commands.append(Command(cmd, r))
            elif "jmp" in line:
                _, cmd, jmp_addr, _ = re.split(r"([a-z]+) ([+|-][0-9]+)", line)
                commands.append(Command(cmd, None, int(jmp_addr)))
            if any([cmd in line for cmd in ["jie", "jio"]]):
                _, cmd, r, jmp_addr, _ = re.split(r"([a-z]+) ([a|b]), ([+\-0-9]+)", line)
                commands.append(Command(cmd, r, int(jmp_addr)))
        return commands


if __name__ == '__main__':
    print(solve(parse("data.txt")))
