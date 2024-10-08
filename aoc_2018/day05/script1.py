def opposite(l1, l2):
    return l1 != l2 and l1.upper() == l2.upper()


def reduce(polymer):
    reduced = ""
    for elem in polymer:
        if len(reduced) == 0:
            reduced = elem
        elif opposite(elem, reduced[-1]):
            reduced = reduced[:-1]
        else:
            reduced += elem
    return reduced


def process(polymer):
    return len(reduce(polymer))


def compute(file_name):
    with open(file_name, "r") as file:
        data = file.readline()
        return process(data)


if __name__ == '__main__':
    print("Part 1:", compute("data.txt"))
