import re


class Sue:
    def __init__(self, sue_id, attr1, val1, attr2, val2, attr3, val3):
        self.sue_id = sue_id
        self.attr = {attr1: val1, attr2: val2, attr3: val3}


def solve(sues):
    ref = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0,
           "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}
    for sue in sues:
        match = True
        for attr_name in sue.attr:
            if sue.attr[attr_name] != ref[attr_name]:
                match = False
                break
        if match:
            return sue.sue_id


def parse(file_name):
    with open(file_name, "r") as f:
        sues = []
        for line in f.readlines():
            _, sue_id, attr1, val1, attr2, val2, attr3, val3, _ = re.split(
                "Sue ([0-9]+): ([a-z]+): ([0-9]+), ([a-z]+): ([0-9]+), ([a-z]+): ([0-9]+)", line)
            sues.append(Sue(sue_id, attr1, int(val1), attr2, int(val2), attr3, int(val3)))
        return sues


if __name__ == '__main__':
    print(solve(parse("data.txt")))
