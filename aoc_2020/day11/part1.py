DIRS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def get_adjacent_cells(i, j):
    return [(i + dx, j + dy) for (dx, dy) in DIRS]


def is_occupied(i, j, matrix):
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and matrix[i][j] == '#'


def count_neighbors(i, j, matrix):
    return [is_occupied(x, y, matrix) for (x, y) in get_adjacent_cells(i, j)].count(True)


def get_next_state(matrix):
    next_state = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'L' and count_neighbors(i, j, matrix) == 0:
                row.append('#')
            elif matrix[i][j] == '#' and count_neighbors(i, j, matrix) >= 4:
                row.append('L')
            else:
                row.append(matrix[i][j])
        next_state.append(row)
    return next_state


def solve(initial_state):
    curr_state = initial_state
    while True:
        next_state = get_next_state(curr_state)
        if curr_state == next_state:
            return sum([row.count('#') for row in curr_state])
        curr_state = next_state


def parse(file_name):
    matrix = []
    with open(file_name, 'r') as f:
        for line in f.readlines():
            matrix.append([c for c in line.strip()])
    return matrix


if __name__ == "__main__":
    print(solve(parse("data.txt")))
