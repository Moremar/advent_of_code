import numpy as np
from part1 import parse, build_scan, add


MONSTER_PATTERN = [(1, 0), (2, 1), (2, 4), (1, 5), (1, 6), (2, 7), (2, 10), (1, 11),
                   (1, 12), (2, 13), (2, 16), (1, 17), (1, 18), (1, 19), (0, 18)]


def build_image(xmin, ymin, xmax, ymax, scan, tiles):
    matrix = []
    tile_size = len(tiles[scan[(xmin, ymin)]].matrix) - 2  # remove the borders
    for y in range(ymax, ymin-1, -1):
        for i in range(tile_size):
            row = []
            for x in range(xmin, xmax+1):
                for j in range(tile_size):
                    tile = tiles[scan[(x, y)]]
                    row.append(tile.matrix[i+1, j+1])
            matrix.append(row)
    return np.array(matrix)


def has_monster(matrix, i, j):
    imax = max([x for (x, _) in MONSTER_PATTERN])
    jmax = max([y for (_, y) in MONSTER_PATTERN])
    if i + imax >= len(matrix) or j + jmax >= len(matrix):
        return False
    return all([matrix[add((i, j), k)] == 1 for k in MONSTER_PATTERN])


def count_monsters(image):
    flipped_h = np.flipud(image)
    flipped_v = np.fliplr(image)
    matrices = [image, np.rot90(image, 1), np.rot90(image, 2), np.rot90(image, 3),
                flipped_h, np.rot90(flipped_h, 1), np.rot90(flipped_h, 2), np.rot90(flipped_h, 3),
                flipped_v, np.rot90(flipped_v, 1), np.rot90(flipped_v, 2), np.rot90(flipped_v, 3)]
    monsters = 0
    for matrix in matrices:
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                monsters += has_monster(matrix, i, j)
        if monsters > 0:
            return np.sum(matrix) - monsters * len(MONSTER_PATTERN)


def solve(tiles):
    scan = build_scan(tiles)
    xmin, ymin = min([x for (x, _) in scan]), min([y for (_, y) in scan])
    xmax, ymax = max([x for (x, _) in scan]), max([y for (_, y) in scan])
    image = build_image(xmin, ymin, xmax, ymax, scan, tiles)
    return count_monsters(image)


if __name__ == "__main__":
    print(solve(parse("data.txt")))
