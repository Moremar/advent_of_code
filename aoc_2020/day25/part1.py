def find_private_key(subject, card_pub):
    loops, val = 0, 1
    while val != card_pub:
        loops += 1
        val = (val * subject) % 20201227
    return loops


def calculate(subject, loop_size):
    val = 1
    for i in range(loop_size):
        val = (val * subject) % 20201227
    return val


def solve(data):
    card_pub, door_pub = data
    card_priv = find_private_key(7, card_pub)
    door_priv = find_private_key(7, door_pub)

    res1 = calculate(card_pub, door_priv)
    res2 = calculate(door_pub, card_priv)
    assert res1 == res2

    return res1


def parse(file_name):
    with open(file_name, 'r') as f:
        return [int(line) for line in f.readlines()]


if __name__ == "__main__":
    print(solve(parse("data.txt")))
