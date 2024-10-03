import re


class Person:
    def __init__(self, name):
        self.name = name
        self.happiness = {}


def compute_permutations(prev, items, result):
    if len(items) == 0:
        result.append(prev)
    for i in range(0, len(items)):
        rest = list(items)
        item = rest.pop(i)
        compute_permutations(prev + [item], rest, result)


def get_permutations(items):
    permutations = []
    compute_permutations([], items, permutations)
    return permutations


def compute_best_happiness(world):
    best_happiness = 0
    for permutation in get_permutations([name for name in world]):
        happiness = 0
        for i in range(0, len(permutation)):
            name = permutation[i]
            neighbours = [permutation[(i-1) % len(permutation)], permutation[(i+1) % len(permutation)]]
            for neighbour_name in neighbours:
                happiness += world[name].happiness[neighbour_name]
        if happiness > best_happiness:
            best_happiness = happiness
    return best_happiness


def solve(world):
    return compute_best_happiness(world)


def parse(file_name):
    with open(file_name, "r") as f:
        world = {}
        for line in f.readlines():
            _, name1, direction, quantity, name2, _ = re.split(
                r"([A-Za-z]+) would ([a-z]+) ([0-9]+) happiness units by sitting next to ([A-Za-z]+)", line)
            if name1 not in world:
                world[name1] = Person(name1)
            world[name1].happiness[name2] = int(quantity) * (1 if direction == "gain" else -1)
        return world


if __name__ == '__main__':
    print(solve(parse("data.txt")))
