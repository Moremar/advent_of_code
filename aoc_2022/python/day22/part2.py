import time
import part1
from part1 import DIRECTIONS, LEFT, UP, RIGHT, DOWN

# The input file has the following shape, so we specify the links between its faces :
#
#          +---+---+
#          | 2 | 1 |
#          +---+---+
#          | 3 |
#      +---+---+
#      | 5 | 4 |
#      +---+---+
#      | 6 |
#      +---+


LINKS = {}

# LINKS for the sample

# def build_links(side):
#     for i in range(1, side + 1):
#         LINKS[((i, 2 * side + 1), LEFT)]                = ((side + 1, side + i), DOWN)               # 1 -> 3
#         LINKS[((side + 1, side + i), UP)]               = ((i, 2 * side + 1), RIGHT)                 # 3 -> 1
#         LINKS[((1, 2 * side + i), UP)]                  = ((side + 1, i), DOWN)                      # 1 -> 2
#         LINKS[((side + 1, i), UP)]                      = ((1, 2 * side + i), DOWN)                  # 2 -> 1
#         LINKS[((i, 3 * side), RIGHT)]                   = ((3 * side + 1 - i, 4 * side), LEFT)       # 1 -> 6
#         LINKS[((3 * side + 1 - i, 4 * side), RIGHT)]    = ((i, 3 * side), LEFT)                      # 6 -> 1
#         LINKS[((side + i, 1), LEFT)]                    = ((3 * side, 4 * side + 1 - i), UP)         # 2 -> 6
#         LINKS[((3 * side, 4 * side + 1 - i), DOWN)]     = ((side + i, 1), RIGHT)                     # 6 -> 2
#         LINKS[((2 * side, i), DOWN)]                    = ((3 * side, 3 * side + 1 - i), UP)         # 2 -> 5
#         LINKS[((3 * side, 3 * side + 1 - i), DOWN)]     = ((2 * side, i), UP)                        # 5 -> 2
#         LINKS[((2 * side, side + i), DOWN)]             = ((3 * side + 1 - i, 2 * side + 1), RIGHT)  # 3 -> 5
#         LINKS[((3 * side + 1 - i, 2 * side + 1), LEFT)] = ((2 * side, side + i), UP)                 # 5 -> 3
#         LINKS[((side + i, 3 * side), RIGHT)]            = ((2 * side + 1, 4 * side + 1 - i), DOWN)   # 4 -> 6
#         LINKS[((2 * side + 1, 4 * side + 1 - i), UP)]   = ((side + i, 3 * side), LEFT)               # 6 -> 4


def build_links(side):
    for i in range(1, side + 1):
        LINKS[((i, side + 1), LEFT)]                 = ((3 * side + 1 - i, 1), RIGHT)        # 1 -> 5
        LINKS[((3 * side + 1 - i, 1), LEFT)]         = ((i, side + 1), RIGHT)                # 5 -> 1
        LINKS[((1, side + i), UP)]                   = ((3 * side + i, 1), RIGHT)            # 1 -> 6
        LINKS[((3 * side + i, 1), LEFT)]             = ((1, side + i), DOWN)                 # 6 -> 1
        LINKS[((1, 2 * side + i), UP)]               = ((4 * side, i), UP)                   # 2 -> 6
        LINKS[((4 * side, i), DOWN)]                 = ((1, 2 * side + i), DOWN)             # 6 -> 2
        LINKS[((i, 3 * side), RIGHT)]                = ((3 * side + 1 - i, 2 * side), LEFT)  # 2 -> 4
        LINKS[((3 * side + 1 - i, 2 * side), RIGHT)] = ((i, 3 * side), LEFT)                 # 4 -> 2
        LINKS[((side, 2 * side + i), DOWN)]          = ((side + i, 2 * side), LEFT)          # 2 -> 3
        LINKS[((side + i, 2 * side), RIGHT)]         = ((side, 2 * side + i), UP)            # 3 -> 2
        LINKS[((side + i, side + 1), LEFT)]          = ((2 * side + 1, i), DOWN)             # 3 -> 5
        LINKS[((2 * side + 1, i), UP)]               = ((side + i, side + 1), RIGHT)         # 5 -> 3
        LINKS[((3 * side, side + i), DOWN)]          = ((3 * side + i, side), LEFT)          # 4 -> 6
        LINKS[((3 * side + i, side), RIGHT)]         = ((3 * side, side + i), UP)            # 6 -> 4


def wrap2(world, pos, direction):
    next_cell = (pos[0] + DIRECTIONS[direction][0], pos[1] + DIRECTIONS[direction][1])
    if next_cell not in world:
        assert (pos, direction) in LINKS
        return LINKS[(pos, direction)]
    return next_cell, direction


if __name__ == "__main__":
    start = time.time()
    parsed = part1.parse("data.txt")
    build_links(50)
    result = part1.solve_part1(parsed, wrap2)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
