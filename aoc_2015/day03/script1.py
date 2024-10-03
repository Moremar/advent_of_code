def solve(moves):
    houses = [[0, 0]]
    pos = [0, 0]
    for move in moves:
        pos = [pos[0] + move[0], pos[1] + move[1]]
        if pos not in houses:
            houses.append(pos)
    return len(houses)


def parse(file_name):
    moves = []
    with open(file_name, "r") as f:
        for c in f.readline():
            if c == "^":
                moves.append([0, 1])
            elif c == ">":
                moves.append([1, 0])
            elif c == "v":
                moves.append([0, -1])
            elif c == "<":
                moves.append([-1, 0])
    return moves


if __name__ == '__main__':
    print(solve(parse("data.txt")))
