def compute(file_name):
    with open(file_name, "r") as file:
        return sum([int(line) for line in file.readlines()])


if __name__ == '__main__':
    print("Part 1:", compute("data.txt"))
