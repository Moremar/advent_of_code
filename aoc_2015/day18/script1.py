def count_neigbors_on(lights, i, j):
    return (lights[i-1][j-1] if i > 0 and j > 0 else 0) \
           + (lights[i-1][j] if i > 0 else 0) \
           + (lights[i-1][j+1] if i > 0 and j < len(lights) - 1 else 0) \
           + (lights[i][j-1] if j > 0 else 0) \
           + (lights[i][j+1] if j < len(lights) - 1 else 0) \
           + (lights[i+1][j-1] if i < len(lights) - 1 and j > 0 else 0) \
           + (lights[i+1][j] if i < len(lights) - 1 else 0) \
           + (lights[i+1][j+1] if i < len(lights) - 1 and j < len(lights) - 1 else 0)


def get_next_state(curr_state):
    next_state = []
    for i in range(0, len(curr_state)):
        row = [0] * len(curr_state[0])
        for j in range(0, len(row)):
            on_stays_on = curr_state[i][j] == 1 and count_neigbors_on(curr_state, i, j) in [2, 3]
            off_turns_on = curr_state[i][j] == 0 and count_neigbors_on(curr_state, i, j) == 3
            if on_stays_on or off_turns_on:
                row[j] = 1
        next_state.append(row)
    return next_state


def solve(lights):
    curr_state = lights
    for turn in range(0, 100):
        curr_state = get_next_state(curr_state)
    return sum([sum(line) for line in curr_state])


def parse(file_name):
    with open(file_name, "r") as f:
        lights = []
        lines = [line.strip() for line in f.readlines()]
        for i in range(0, len(lines)):
            row = [0] * len(lines[0])
            for j in range(0, len(row)):
                if lines[i][j] == "#":
                    row[j] = 1
            lights.append(row)
        return lights


if __name__ == '__main__':
    print(solve(parse("data.txt")))
