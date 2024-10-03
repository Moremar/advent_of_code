def get_diff_sequence(jolts):
    jolts.sort()
    prev = [0] + jolts
    jolts.append(jolts[-1] + 3)
    return [jolts[i] - prev[i] for i in range(len(jolts))]


def solve(jolts):
    diff = get_diff_sequence(jolts)
    return diff.count(3) * diff.count(1)


def parse(file_name):
    with open(file_name, 'r') as f:
        return list(map(int, f.readlines()))


if __name__ == "__main__":
    print(solve(parse("sample.txt")))