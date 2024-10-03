from collections import defaultdict
#     __
#  __/NE\__     We use E = (1, 0) and NE = (0, 1)
# /NW\__/E \    Other directions become :
# \__/0 \__/      W = -E
# /W \__/SE\     SW = -NE
# \__/SW\__/     SE = E - NE
#    \__/        NW = NE - E

E, W, NE, NW, SE, SW = (1, 0), (-1, 0), (0, 1), (-1, 1), (1, -1), (0, -1)


def add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])


def get_black_tiles(data):
    tiles_count = defaultdict(lambda: 0)
    for path in data:
        curr_tile = (0, 0)
        for direction in path:
            curr_tile = add(curr_tile, direction)
        tiles_count[curr_tile] += 1
    return set([tile for tile in tiles_count if tiles_count[tile] % 2 == 1])


def solve(data):
    return len(get_black_tiles(data))


def parse(file_name):
    tiles = []
    directions = {'e': E, 'w': W, 'ne': NE, 'nw': NW, 'se': SE, 'sw': SW}
    with open(file_name, 'r') as f:
        for line in f.readlines():
            path = '.'.join(line.strip()).replace('s.', 's').replace('n.', 'n').split('.')
            tiles.append([directions[d] for d in path])
        return tiles


if __name__ == "__main__":
    print(solve(parse("data.txt")))
