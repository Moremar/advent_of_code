import re


class Move:
    def __init__(self, action, x1, y1, x2, y2):
        self.action = action
        self.start = (x1, y1)
        self.end = (x2, y2)


def solve(moves):
    lights = {}
    for move in moves:
        for i in range(move.start[0], move.end[0] + 1):
            for j in range(move.start[1], move.end[1] + 1):
                if move.action == "turn on":
                    lights[(i, j)] = 1
                elif move.action == "turn off":
                    lights[(i,j)] = 0
                elif move.action == "toggle":
                    lights[(i,j)] = 1 - (lights[(i,j)] if (i, j) in lights else 0)
                else:
                    raise ValueError("Unknown action : " + move.action)
    return sum(lights.values())


def parse(file_name):
    with open(file_name, "r") as f:
        moves = []
        for line in f.readlines():
            _, action, x1, y1, x2, y2, _ = re.split(
                r"^(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)", line)
            moves.append(Move(action, int(x1), int(y1), int(x2), int(y2)))
        return moves


if __name__ == '__main__':
    print(solve(parse("data.txt")))
