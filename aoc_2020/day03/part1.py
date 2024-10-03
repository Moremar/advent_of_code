def count_trees(trees, dx, dy):
    x, y, count = 0, 0, 0
    while y + dy < len(trees):
        x += dx
        y += dy
        count += trees[y][x % len(trees[0])]
    return count


def solve(trees):
    return count_trees(trees, 3, 1)


def parse(file_name):
    trees = []
    with open(file_name, 'r') as f:
        for line in map(str.strip, f.readlines()):
            trees.append([0 if c == '.' else 1 for c in line])
        return trees


if __name__ == '__main__':
    print(solve(parse('data.txt')))
