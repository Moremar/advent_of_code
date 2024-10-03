from part1 import parse


def get_addresses(mask, address):
    address = bin(int(address))[2:].zfill(36)   # strip the '0b' prefix
    # replace by 1 the bits in the address when a 1 is in the mask
    for (i, char) in enumerate(mask):
        if char == '1':
            address = address[:i] + '1' + address[i+1:]
    # for each X in the mask, generate all possibilities in the addresses
    addresses = [address]
    for (i, char) in enumerate(mask):
        if char == 'X':
            new_addresses = []
            for address in addresses:
                new_addresses.append(address[:i] + '1' + address[i+1:])
                new_addresses.append(address[:i] + '0' + address[i + 1:])
            addresses = new_addresses
    return [int(s, base=2) for s in addresses]


def solve(commands):
    memory, mask = {}, ''
    for command in commands:
        if command[0] == 'mask':
            mask = command[1]
        else:
            for address in get_addresses(mask, command[1][0]):
                memory[address] = command[1][1]
    return sum([memory[x] for x in memory])


if __name__ == "__main__":
    print(solve(parse("data.txt")))
