from math import sqrt, floor


def get_presents_for_house(house):
    presents = 0
    born_sup = int(floor(sqrt(house))) + 1
    for i in range(1, born_sup):
        if house % i == 0:
            complement = house // i
            presents += i
            if complement != i:
                presents += complement
    return presents * 10


def find_smallest_house(target, count_presents):
    i = 0
    while True:
        i += 1
        if count_presents(i) >= target:
            return i


def solve(target):
    return find_smallest_house(target, get_presents_for_house)


def parse(file_name):
    with open(file_name, "r") as f:
        return int(f.readline().strip())


if __name__ == '__main__':
    print(solve(parse("data.txt")))
