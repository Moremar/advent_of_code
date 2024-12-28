"""Solution for AOC 2024 day 21"""

POSITIONS = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
                 '0': (3, 1), 'A': (3, 2),
                 '^': (3, 1),
    '<': (4, 0), 'v': (4, 1), '>': (4, 2)
}


def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]


def cache_robot_moves():
    """Cache the number of moves at a given depth to press a button from any position"""
    # it takes a single button press to push any button at depth 0, no matter the previous button
    cache = {(x, y, 0): 1 for x in POSITIONS for y in POSITIONS}
    for depth in range(1, 27):
        for from_key in POSITIONS:
            for to_key in POSITIONS:
                dx, dy = POSITIONS[to_key][0] - POSITIONS[from_key][0], \
                         POSITIONS[to_key][1] - POSITIONS[from_key][1]
                if dx == 0:
                    sequence = ('>' if dy > 0 else '<') * abs(dy) + 'A'
                elif dy == 0:
                    sequence = ('v' if dx > 0 else '^') * abs(dx) + 'A'
                # (3, 0) is not a valid position, so we do not allow to go over it
                elif (POSITIONS[from_key][0], POSITIONS[to_key][1]) == (3, 0):
                    sequence = ('v' if dx > 0 else '^') * abs(dx) \
                               + ('>' if dy > 0 else '<') * abs(dy) + 'A'
                elif (POSITIONS[to_key][0], POSITIONS[from_key][1]) == (3, 0):
                    sequence = ('>' if dy > 0 else '<') * abs(dy) \
                               + ('v' if dx > 0 else '^') * abs(dx) + 'A'
                # when both horizontal and vertical moves are required and both order are valid,
                # it is optimal to start with the horizontal move only if it goes to the left
                elif dy < 0:
                    sequence = ('>' if dy > 0 else '<') * abs(dy) \
                               + ('v' if dx > 0 else '^') * abs(dx) + 'A'
                else:
                    sequence = ('v' if dx > 0 else '^') * abs(dx) \
                               + ('>' if dy > 0 else '<') * abs(dy) + 'A'

                # count the number of moves required to execute this sequence of buttons
                count, prev = 0, 'A'
                for c in sequence:
                    count += cache[(prev, c, depth - 1)]
                    prev = c
                cache[(from_key, to_key, depth)] = count
    return cache


def solve(codes, depth):
    """Solve part 2"""
    moves_cache = cache_robot_moves()
    res = 0
    for code in codes:
        count, prev = 0, 'A'
        for c in code:
            count += moves_cache[(prev, c, depth)]
            prev = c
        res += count * int(code[:-1])
    return res


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 21:', solve(parsed, 3), solve(parsed, 26))
