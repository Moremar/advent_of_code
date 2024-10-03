from script1 import parse, hexa_hash


def solve(secret_key):
    i = 0
    while True:
        if hexa_hash(secret_key + str(i))[:6] == "000000":
            return i
        i += 1


if __name__ == '__main__':
    print(solve(parse("data.txt")))
