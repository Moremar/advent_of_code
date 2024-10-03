from script1 import parse, get_best_path


def longer_path(path1, path2):
    return path1.distance > path2.distance


def solve(world):
    return get_best_path(world, longer_path)


if __name__ == '__main__':
    print(solve(parse("data.txt")))
