import re


class City:
    def __init__(self, name):
        self.name = name
        self.edges = {}


class Path:
    def __init__(self, city, visited, distance):
        self.city = city
        self.visited = visited
        self.distance = distance


def shorter_path(path1, path2):
    return path1.distance < path2.distance


def get_best_path(world, is_better_path):
    best_path = None
    for start in world:  # loop on all city to decide the starting one
        to_process = [Path(start, [start], 0)]
        while len(to_process) > 0:
            curr_path = to_process.pop(0)
            if len(curr_path.visited) == len(world):
                if best_path is None or is_better_path(curr_path, best_path):
                    best_path = curr_path
            else:
                for next_city in world[curr_path.city].edges:
                    if next_city not in curr_path.visited:
                        dist_to_next_city = curr_path.distance + world[curr_path.city].edges[next_city]
                        to_process.append(Path(next_city, curr_path.visited + [next_city], dist_to_next_city))
    return best_path.distance


def solve(world):
    return get_best_path(world, shorter_path)


def parse(file_name):
    with open(file_name, "r") as f:
        world = {}
        for line in f.readlines():
            _, city1, city2, distance, _ = re.split(r"([A-Za-z]+) to ([A-Za-z]+) = ([0-9]+)", line)
            if city1 not in world:
                world[city1] = City(city1)
            if city2 not in world:
                world[city2] = City(city2)
            world[city1].edges[city2] = int(distance)
            world[city2].edges[city1] = int(distance)
        return world


if __name__ == '__main__':
    print(solve(parse("data.txt")))
