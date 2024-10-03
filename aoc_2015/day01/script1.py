def solve(line):
    return line.count("(") - line.count(")")


def parse(file_name):
    with open(file_name, "r") as f:
        return f.readline()


if __name__ == '__main__':
    print(solve(parse("data.txt")))
