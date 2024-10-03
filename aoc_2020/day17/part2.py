from part1 import parse, run_cycles


def get_neighbors(coords):
    neighbors = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                for dw in range(-1, 2):
                    neighbors.append((coords[0] + dx, coords[1] + dy, coords[2] + dz, coords[3] + dw))
    neighbors.remove(coords)
    return neighbors


def solve(universe):
    universe = set([(x, y, 0, 0) for (x, y) in universe])
    return run_cycles(universe, get_neighbors)


if __name__ == "__main__":
    print(solve(parse("data.txt")))
