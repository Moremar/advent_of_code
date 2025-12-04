"""Solution for AOC 2025 day 4"""

def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        return { (i, j) for (i, line) in enumerate(file.readlines())
                        for (j, c) in enumerate(line)
                        if c == '@' }


def get_adjacent(p):
    """Get the 8 adjacent coordinates"""
    x, y = p
    return {(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)}


def get_removable(world):
    """Get the subset of coordinates that have less than 4 neighbors"""
    return {p for p in world if len(get_adjacent(p).intersection(world)) < 4}


def solve1(world):
    """Solve part 1"""
    return len(get_removable(world))


def solve2(world):
    """Solve part 2"""
    total = 0
    while True:
        removable = get_removable(world)
        if len(removable):
            total += len(removable)
            world = world.difference(removable)
        else:
            return total


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 4:', solve1(parsed), solve2(parsed))
