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
            words = []
            if (i, j + 3) in grid:  # horizontal
                words.append(grid[(i, j + 1)] + grid[(i, j + 2)] + grid[(i, j + 3)])
            if (i, j - 3) in grid:  # horizontal backwards
                words.append(grid[(i, j - 1)] + grid[(i, j - 2)] + grid[(i, j - 3)])
            if (i + 3, j) in grid:  # vertical
                words.append(grid[(i + 1, j)] + grid[(i + 2, j)] + grid[(i + 3, j)])
            if (i - 3, j) in grid:  # vertical backwards
                words.append(grid[(i - 1, j)] + grid[(i - 2, j)] + grid[(i - 3, j)])
            if (i + 3, j + 3) in grid:  # diagonal down-right
                words.append(grid[(i + 1, j + 1)] + grid[(i + 2, j + 2)] + grid[(i + 3, j + 3)])
            if (i + 3, j - 3) in grid:  # diagonal down-left
                words.append(grid[(i + 1, j - 1)] + grid[(i + 2, j - 2)] + grid[(i + 3, j - 3)])
            if (i - 3, j - 3) in grid:  # diagonal up-left
                words.append(grid[(i - 1, j - 1)] + grid[(i - 2, j - 2)] + grid[(i - 3, j - 3)])
            if (i - 3, j + 3) in grid:  # diagonal up-right
                words.append(grid[(i - 1, j + 1)] + grid[(i - 2, j + 2)] + grid[(i - 3, j + 3)])
            result += sum(1 for word in words if word == 'MAS')
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
