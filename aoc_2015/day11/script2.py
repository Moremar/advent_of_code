from script1 import parse, get_next_valid


def solve(current_pwd):
    return get_next_valid(get_next_valid(current_pwd))


if __name__ == '__main__':
    print(solve(parse("data.txt")))
