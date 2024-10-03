from script1 import parse


def solve(moves):
    houses = [[0, 0]]
    pos_santa = [0, 0]
    pos_robot = [0, 0]
    i = 0
    while i < len(moves):
        # move santa
        pos_santa = [pos_santa[0] + moves[i][0], pos_santa[1] + moves[i][1]]
        if pos_santa not in houses:
            houses.append(pos_santa)
        # move robot
        pos_robot = [pos_robot[0] + moves[i+1][0], pos_robot[1] + moves[i+1][1]]
        if pos_robot not in houses:
            houses.append(pos_robot)
        i += 2
    return len(houses)


if __name__ == '__main__':
    print(solve(parse("data.txt")))
