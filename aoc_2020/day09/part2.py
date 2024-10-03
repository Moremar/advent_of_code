import part1 as p1


def solve(file_name):
    numbers = p1.parse(file_name)
    target = p1.solve(numbers)
    for i in range(len(numbers)):
        total, sequence, k = (0, [], i)
        while k < len(numbers) and total < target:
            sequence.append(numbers[k])
            total += numbers[k]
            k += 1
        if total == target:
            return min(sequence) + max(sequence)
    raise Exception('Not found')


if __name__ == "__main__":
    print(solve("data.txt"))
