class NumberInfo:
    def __init__(self, index):
        self.count = 1
        self.index = index
        self.prev_index = -1

    def update(self, index):
        self.count += 1
        self.prev_index = self.index
        self.index = index

    def get_age(self):
        return self.index - self.prev_index

    def __repr__(self):
        return 'NumberInfo({0}, {1}, {2})'.format(self.count, self.index, self.prev_index)


def get_nth_number(starting_numbers, n):
    seen = {}
    last_number = starting_numbers[-1]
    for (i, k) in enumerate(starting_numbers):
        seen[k] = NumberInfo(i)
    for i in range(len(starting_numbers), n):
        last_number = 0 if seen[last_number].count == 1 else seen[last_number].get_age()
        if last_number in seen:
            seen[last_number].update(i)
        else:
            seen[last_number] = NumberInfo(i)
    return last_number


def solve(starting_numbers):
    return get_nth_number(starting_numbers, 2020)


def parse(file_name):
    with open(file_name, 'r') as f:
        return list(map(int, f.readlines()[0].strip().split(',')))


if __name__ == "__main__":
    print(solve(parse("data.txt")))
