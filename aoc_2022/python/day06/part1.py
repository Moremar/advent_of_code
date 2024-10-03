import time


def solve_part1(sequence, length):
    for i in range(length, len(sequence)):
        if len(set(sequence[i-length:i])) == length:
            return i


def parse(input_path):
    with open(input_path, 'r') as f:
        return f.read()


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve_part1(parsed, 4)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
