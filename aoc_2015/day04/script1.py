import hashlib


def hexa_hash(packet):
    encoded = hashlib.md5(packet.encode())
    return encoded.hexdigest()


def solve(secret_key):
    i = 0
    while True:
        if hexa_hash(secret_key + str(i))[:5] == "00000":
            return i
        i += 1


def parse(file_name):
    with open(file_name, "r") as f:
        return f.readline()


if __name__ == '__main__':
    print(solve(parse("data.txt")))
