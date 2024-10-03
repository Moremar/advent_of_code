from script1 import parse, Person, compute_best_happiness


def solve(world):
    # Add Santa and update all relations including Santa with happiness 0
    santa = Person("Santa")
    for name in world:
        world[name].happiness["Santa"] = 0
        santa.happiness[name] = 0
    world["Santa"] = santa

    return compute_best_happiness(world)


if __name__ == '__main__':
    print(solve(parse("data.txt")))
