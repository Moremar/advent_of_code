from script1 import parse


def solve(sues):
    ref = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0,
           "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}
    for sue in sues:
        match = True
        for attr_name in sue.attr:
            if attr_name in ["cats", "trees"]:
                if sue.attr[attr_name] <= ref[attr_name]:
                    match = False
                    break
            elif attr_name in ["pomeranians", "goldfish"]:
                if sue.attr[attr_name] >= ref[attr_name]:
                    match = False
                    break
            elif sue.attr[attr_name] != ref[attr_name]:
                match = False
                break
        if match:
            return sue.sue_id


if __name__ == '__main__':
    print(solve(parse("data.txt")))
