import re


def apply_mask(mask, val):
    res = bin(val)[2:].zfill(36)  # strip the '0b' prefix
    for (i, char) in enumerate(mask):
        if char != 'X':
            res = res[:i] + char + res[i+1:]
    return int(res, base=2)


def solve(commands):
    memory, mask = {}, ''
    for command in commands:
        if command[0] == 'mask':
            mask = command[1]
        else:
            memory[command[1][0]] = apply_mask(mask, command[1][1])
    return sum([memory[x] for x in memory.keys()])


def parse(file_name):
    commands = []
    with open(file_name, 'r') as f:
        for line in f.readlines():
            if 'mask' in line:
                mask = re.match(r'mask = ([01X]+)$', line.strip()).group(1)
                commands.append(('mask', mask))
            else:
                address, val = re.match(r'mem\[([\d]+)\] = ([\d]+)$', line.strip()).groups()
                commands.append(('mem', (address, int(val))))
        return commands


if __name__ == "__main__":
    print(solve(parse("data.txt")))
