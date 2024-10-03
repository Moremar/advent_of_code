from script1 import parse, find_smallest_house
from math import sqrt, floor


def get_presents_for_house(house):
    presents = 0
    born_sup = int(floor(sqrt(house))) + 1
    for i in range(1, born_sup):
        if house % i == 0:
            complement = house // i
            if complement <= 50:
                presents += i
            if complement != i and i <= 50:
                presents += complement
    return presents * 11


def solve(target):
    return find_smallest_house(target, get_presents_for_house)


if __name__ == '__main__':
    print(solve(parse("data.txt")))
