from part1 import DIRS, parse, is_occupied


def next_seat_in_dir(i, j, direction, matrix):
    while True:
        i += direction[0]
        j += direction[1]
        if not 0 <= i < len(matrix) or not 0 <= j < len(matrix[0]) or matrix[i][j] != '.':
            return i, j


def get_adjacent_cells(i, j, matrix):
    return [next_seat_in_dir(i, j, direction, matrix) for direction in DIRS]


def count_neighbors(i, j, matrix):
    return [is_occupied(x, y, matrix) for (x, y) in get_adjacent_cells(i, j, matrix)].count(True)


def get_next_state(matrix):
    next_state = []
    for i in range(0, len(matrix)):
        row = []
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == 'L' and count_neighbors(i, j, matrix) == 0:
                row.append('#')
            elif matrix[i][j] == '#' and count_neighbors(i, j, matrix) >= 5:
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


if __name__ == "__main__":
    print(solve(parse("data.txt")))
