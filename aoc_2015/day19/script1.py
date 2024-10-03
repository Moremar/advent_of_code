import re


def solve(data):
    (reactions, origin) = data
    generated = {}
    for reaction in reactions:
        matches = [match_index.start() for match_index in re.finditer(reaction[0], origin)]
        for match_index in matches:
            result = origin[:match_index] + reaction[1] + origin[match_index + len(reaction[0]):]
            generated[result] = 1
    return len(generated)


def parse(file_name):
    with open(file_name, "r") as f:
        reactions = []
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            if len(line) == 0:
                break
            _, left, right, _ = re.split(r"([a-zA-Z]+) => ([a-zA-Z]+)", line)
            reactions.append((left, right))
        molecule = lines[-1]
        return reactions, molecule


if __name__ == '__main__':
    print(solve(parse("data.txt")))
