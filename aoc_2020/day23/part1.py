# A simple approach with a new list created at every move works fine for part 1
# but for part 2 the problem is too big to complete in a decent time.
# If we use a map giving for each cup the value of the next cup, we do not need to
# create/copy any list, and the search of the destination is O(1) instead of O(n)

def next_move(curr, next_cups):
    next1 = next_cups[curr]
    next2 = next_cups[next1]
    next3 = next_cups[next2]
    next_cups[curr] = next_cups[next3]
    destination = curr - 1
    while destination in [0, next1, next2, next3]:
        destination = (destination - 1) % (len(next_cups)+1)
    next_cups[next3] = next_cups[destination]
    next_cups[destination] = next1
    return next_cups[curr]


def solve(cups):
    next_cups = {}
    for i in range(len(cups)-1):
        next_cups[cups[i]] = cups[i+1]
    next_cups[cups[len(cups)-1]] = cups[0]

    curr = cups[0]
    for i in range(100):
        curr = next_move(curr, next_cups)

    res, curr = '', next_cups[1]
    while curr != 1:
        res += str(curr)
        curr = next_cups[curr]
    return res


def parse(file_name):
    with open(file_name, 'r') as f:
        return [int(c) for c in f.read().strip()]


if __name__ == "__main__":
    print(solve(parse("data.txt")))
