from part1 import parse, add, turn_right, NORTH, EAST, SOUTH, WEST


def solve(instructions):
    pos = (0, 0)
    waypoint = (10, 1)
    for (letter, val) in instructions:
        if letter == 'F':
            pos = add(pos, waypoint, val)
        elif letter == 'N':
            waypoint = add(waypoint, NORTH, val)
        elif letter == 'S':
            waypoint = add(waypoint, SOUTH, val)
        elif letter == 'W':
            waypoint = add(waypoint, WEST, val)
        elif letter == 'E':
            waypoint = add(waypoint, EAST, val)
        elif letter == 'R':
            waypoint = turn_right(waypoint, val // 90)
        elif letter == 'L':
            waypoint = turn_right(waypoint, 4 - val // 90)
    return abs(pos[0]) + abs(pos[1])


if __name__ == "__main__":
    print(solve(parse("data.txt")))
