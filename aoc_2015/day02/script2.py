from script1 import parse


def solve(gifts):
    total = 0
    for (length, width, height) in gifts:
        half_perimeters = [length + width, length + height, width + height]
        total += 2 * min(half_perimeters) + (length * width * height)
    return total


if __name__ == '__main__':
    print(solve(parse("data.txt")))
