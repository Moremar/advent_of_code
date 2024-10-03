import re


def solve(gifts):
    total = 0
    for (length, width, height) in gifts:
        sizes = [length * width, length * height, width * height]
        total += 2 * sum(sizes) + min(sizes)
    return total


def parse(file_name):
    gifts = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            _, length, width, height, _ = re.split(r"(\d+)x(\d+)x(\d+)", line)
            gifts.append([int(length), int(width), int(height)])
    return gifts


if __name__ == '__main__':
    print(solve(parse("data.txt")))
