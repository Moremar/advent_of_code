from collections import defaultdict


def get_neighbors(coords):
    neighbors = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                neighbors.append((coords[0] + dx, coords[1] + dy, coords[2] + dz))
    neighbors.remove(coords)
    return neighbors


def run_cycles(universe, neighbors_fn):
    for cycle in range(6):
        next_universe = set()
        neighbor_count = defaultdict(lambda: 0)
        # for all current active cubes, add them in the next state if 2 or 3 active neighbors
        for coords in universe:
            count = 0
            for neighbor in neighbors_fn(coords):
                if neighbor in universe:
                    count += 1
                else:
                    neighbor_count[neighbor] += 1
            if 2 <= count <= 3:
                next_universe.add(coords)
        # for all inactive cubes, add them in the next state if 3 active neighbors
        for coords in neighbor_count:
            if neighbor_count[coords] == 3:
                next_universe.add(coords)
        universe = next_universe
    return len(universe)


def solve(universe):
    universe = set([(x, y, 0) for (x, y) in universe])
    return run_cycles(universe, get_neighbors)


def parse(file_name):
    universe = set()
    with open(file_name, 'r') as f:
        for (x, line) in enumerate(f.readlines()):
            for (y, c) in enumerate(line.strip()):
                if c == '#':
                    universe.add((x, y))
        return universe


if __name__ == "__main__":
    print(solve(parse("data.txt")))
