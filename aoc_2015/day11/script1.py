ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def increment(pwd):
    incremented = ""
    pos_not_z = len(pwd) - 1
    while pwd[pos_not_z] == "z":
        incremented = "a" + incremented
        pos_not_z -= 1
    incremented = pwd[:pos_not_z] + ALPHABET[ALPHABET.index(pwd[pos_not_z]) + 1] + incremented
    return incremented


def valid(pwd):
    if any([forbidden in pwd for forbidden in ["i", "l", "o"]]):
        return False
    # check for a sequence of 3 consecutive letters
    contains_seq = False
    for i in range(0, 6):
        if pwd[i:i+3] in ALPHABET:
            contains_seq = True
            break
    if not contains_seq:
        return False
    # check for 2 pairs
    pairs = 0
    pos = 0
    while pos <= 6:
        if pwd[pos] == pwd[pos + 1]:
            pairs += 1
            pos += 2
        else:
            pos += 1
    return pairs >= 2


def get_next_valid(pwd):
    pwd = increment(pwd)
    while not valid(pwd):
        pwd = increment(pwd)
    return pwd


def solve(current_pwd):
    return get_next_valid(current_pwd)


def parse(file_name):
    with open(file_name, "r") as f:
        return f.readline().strip()


if __name__ == '__main__':
    print(solve(parse("sample.txt")))
