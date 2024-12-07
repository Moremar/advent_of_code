"""Solution for AOC 2024 day 4"""


def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        grid = {}
        lines = file.readlines()
        for (i, line) in enumerate(lines):
            for (j, c) in enumerate(line):
                grid[(i, j)] = c
        return len(lines), len(lines[0].strip()), grid


def solve1(grid_info):
    """Solve part 1"""
    line_count, line_size, grid = grid_info
    result = 0
    for i in range(line_count):
        for j in range(line_size):
            if grid[(i, j)] != 'X':
                continue
            for direction in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                if (i + 3 * direction[0], j + 3 * direction[1]) in grid and \
                        grid[i + direction[0], j + direction[1]] == 'M' and \
                        grid[i + 2 * direction[0], j + 2 * direction[1]] == 'A' and \
                        grid[i + 3 * direction[0], j + 3 * direction[1]] == 'S':
                    result += 1
    return result


def solve2(grid_info):
    """Solve part 2"""
    max_i, max_j, grid = grid_info
    result = 0
    for i in range(1, max_i - 1):
        for j in range(1, max_j - 1):
            if grid[(i, j)] != 'A':
                continue
            x1 = (grid[(i - 1, j - 1)] == 'M' and grid[(i + 1, j + 1)] == 'S') or (
                    grid[(i - 1, j - 1)] == 'S' and grid[(i + 1, j + 1)] == 'M')
            x2 = (grid[(i - 1, j + 1)] == 'M' and grid[(i + 1, j - 1)] == 'S') or (
                    grid[(i - 1, j + 1)] == 'S' and grid[(i + 1, j - 1)] == 'M')
            if x1 and x2:
                result += 1
    return result


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 04:', solve1(parsed), solve2(parsed))
