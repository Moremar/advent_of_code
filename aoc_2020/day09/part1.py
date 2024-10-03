def valid(numbers, i):
    """Check if the number at position i is the sum of 2 numbers in the previous 25"""
    seen = set()
    for k in range(i-25, i):
        if (numbers[i] - numbers[k]) in seen:
            return True
        seen.add(numbers[k])
    return False


def solve(numbers):
    for (i, val) in enumerate(numbers):
        if i < 25:
            continue
        if not valid(numbers, i):
            return numbers[i]
    raise Exception('Not found')


def parse(file_name):
    with open(file_name, 'r') as f:
        return list(map(int, f.readlines()))


if __name__ == "__main__":
    print(solve(parse("data.txt")))
