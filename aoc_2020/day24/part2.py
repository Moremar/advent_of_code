from part1 import parse, add, get_black_tiles, E, W, NE, NW, SE, SW


def get_neighbors(tile):
    return set([add(tile, direction) for direction in [E, W, NE, NW, SE, SW]])


def get_next_black_tiles(tiles):
    next_black_tiles = set()
    to_check = set()
    # black tiles stay black if 1 or 2 neighbors
    for tile in tiles:
        neighbors = get_neighbors(tile)
        to_check = to_check.union(neighbors)
        if len(neighbors.intersection(tiles)) in [1, 2]:
            next_black_tiles.add(tile)
    # white tiles turn black if 2 neighbors
    for tile in to_check:
        if tile in tiles:   # ignore black tiles
            continue
        if len(get_neighbors(tile).intersection(tiles)) == 2:
            next_black_tiles.add(tile)
    return next_black_tiles


def solve(tiles):
    black_tiles = get_black_tiles(tiles)
    for i in range(100):
        black_tiles = get_next_black_tiles(black_tiles)
    return len(black_tiles)


if __name__ == "__main__":
    print(solve(parse("data.txt")))
