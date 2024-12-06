"""Solution for AOC 2024 day 6"""

UP, RIGHT, DOWN, LEFT = (-1, 0), (0, 1), (1, 0), (0, -1)
DIRECTIONS = [UP, RIGHT, DOWN, LEFT]


def next_direction(direction):
    """Get the direction to the right of a direction"""
    return DIRECTIONS[(DIRECTIONS.index(direction) + 1) % 4]


def add_coords(c1, c2):
    """Add two 2D coordinates"""
    return c1[0] + c2[0], c1[1] + c2[1]


def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        blocks = set()
        start = (-1, -1)
        lines = [line.strip() for line in file.readlines()]
        for (i, line) in enumerate(lines):
            for (j, c) in enumerate(line):
                if c == '#':
                    blocks.add((i, j))
                if c == '^':
                    start = (i, j)
        return blocks, start, len(lines), len(lines[0])


def get_visited_cells(blocks, start, row_count, col_count):
    """Get a set of all visited cells"""
    position = start
    direction = UP
    visited = {start}
    while True:
        straight = add_coords(position, direction)
        if not 0 <= straight[0] < row_count or not 0 <= straight[1] < col_count:
            break
        if straight in blocks:
            direction = next_direction(direction)
        else:
            position = straight
            visited.add(position)
    return visited


def solve1(block_details):
    """Solve part 1"""
    blocks, start, row_count, col_count = block_details
    return len(get_visited_cells(blocks, start, row_count, col_count))


def solve2(block_details):
    """Solve part 2"""
    blocks, start, row_count, col_count = block_details
    result = 0
    for block_position in get_visited_cells(blocks, start, row_count, col_count):
        if block_position == start:
            continue
        position, direction = start, UP
        seen = {(position, direction)}
        while True:
            straight = add_coords(position, direction)
            if not 0 <= straight[0] < row_count or not 0 <= straight[1] < col_count:
                # out of the map, not a loop
                break
            if straight in blocks or straight == block_position:
                direction = next_direction(direction)
            else:
                position = straight
                if (position, direction) in seen:
                    # loop found
                    result += 1
                    break
                seen.add((position, direction))
    return result


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 06:', solve1(parsed), solve2(parsed))
