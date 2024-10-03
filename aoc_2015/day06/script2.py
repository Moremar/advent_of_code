from script1 import parse


def solve(moves):
    lights = {}
    for move in moves:
        for i in range(move.start[0], move.end[0] + 1):
            for j in range(move.start[1], move.end[1] + 1):
                if (i, j) not in lights:
                    lights[(i,j)] = 0
                if move.action == "turn on":
                    lights[(i, j)] += 1
                elif move.action == "turn off" and lights[(i, j)] > 0:
                    lights[(i,j)] -= 1
                elif move.action == "toggle":
                    lights[(i,j)] += 2
    return sum(lights.values())


if __name__ == '__main__':
    print(solve(parse("data.txt")))
