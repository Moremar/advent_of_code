from script1 import parse, get_next_state


def force_corners_on(state):
    state[0][0] = 1
    state[0][-1] = 1
    state[-1][0] = 1
    state[-1][-1] = 1


def solve(lights):
    curr_state = lights
    force_corners_on(curr_state)
    for turn in range(0, 100):
        curr_state = get_next_state(curr_state)
        force_corners_on(curr_state)
    return sum([sum(line) for line in curr_state])


if __name__ == '__main__':
    print(solve(parse("data.txt")))
