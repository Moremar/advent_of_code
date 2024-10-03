import re
from collections import defaultdict
import numpy as np

NORTH, WEST, SOUTH, EAST = 0, 1, 2, 3
DIRECTIONS = (0, 1), (-1, 0), (0, -1), (1, 0)


def add(v1, v2):
    return v1[0] + v2[0], v1[1] + v2[1]


class Tile:
    def __init__(self, tile_id, matrix):
        self.tile_id = tile_id
        self.matrix = matrix

    def get_border(self, direction):
        if direction == NORTH:
            row = self.matrix[0]
        elif direction == EAST:
            row = self.matrix[:, -1]  # last column
        elif direction == SOUTH:
            row = self.matrix[len(self.matrix) - 1][::-1]  # last line reversed
        else:
            row = self.matrix[:, 0][::-1]  # first column reversed
        return ''.join(map(str, row))      # convert into a string usable as a key in a dict

    def get_direction(self, border):
        for direction in range(4):
            if self.get_border(direction) == border:
                return direction
        raise Exception('Not Found')

    def reshape(self, border, direction):
        """Reshape the matrix to have the given border in the given direction"""
        # flip if needed
        mirror = border[::-1]
        if mirror in [self.get_border(NORTH), self.get_border(SOUTH)]:
            self.matrix = np.flipud(self.matrix)  # flip up/down
        elif mirror in [self.get_border(WEST), self.get_border(EAST)]:
            self.matrix = np.fliplr(self.matrix)  # flip left/right
        # rotate if needed
        border_direction = self.get_direction(border)
        self.matrix = np.rot90(self.matrix, (direction - border_direction) % 4)


def build_borders_info(tiles):
    """Create a map giving for each border which tile IDs have it (either as-is or reversed)"""
    info = defaultdict(lambda: [])
    for tile_id in tiles:
        for direction in range(4):
            key = tiles[tile_id].get_border(direction)
            info[key].append(tile_id)
            info[key[::-1]].append(tile_id)
    return info


def build_scan(tiles):
    """Keep a first tile as-is and rotate/flip others around it to order the tiles by matching border"""
    info = build_borders_info(tiles)
    first_tile_id = list(tiles.keys())[0]
    to_process = [(first_tile_id, (0, 0))]
    scan = {(0, 0): first_tile_id}
    while len(to_process):
        tile_id, coord = to_process.pop()
        for direction in range(4):
            next_coord = add(coord, DIRECTIONS[direction])
            if next_coord not in scan:
                key = tiles[tile_id].get_border(direction)
                if len(info[key]) != 1:
                    next_tile_id = [x for x in info[key] if x != tile_id][0]
                    next_tile = tiles[next_tile_id]
                    next_tile.reshape(key[::-1], (direction + 2) % 4)
                    scan[next_coord] = next_tile_id
                    to_process.append((next_tile_id, next_coord))
    return scan


def solve(tiles):
    scan = build_scan(tiles)
    xmin, ymin = min([x for (x, _) in scan]), min([y for (_, y) in scan])
    xmax, ymax = max([x for (x, _) in scan]), max([y for (_, y) in scan])
    return scan[xmin, ymin] * scan[xmin, ymax] * scan[xmax, ymin] * scan[xmax, ymax]


def parse(file_name):
    tiles = {}
    with open(file_name, 'r') as f:
        for tile in f.read().split('\n\n'):
            tile_id = re.match(r'Tile (\d+):', tile).group(1)
            matrix = []
            for line in tile.split('\n')[1:]:
                matrix.append([1 if c == '#' else 0 for c in line.strip()])
            tiles[int(tile_id)] = Tile(int(tile_id), np.array(matrix))
        return tiles


if __name__ == "__main__":
    print(solve(parse("data.txt")))
