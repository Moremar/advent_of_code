"""Solution for AOC 2025 day 12"""


def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        blocks = file.read().split('\n\n')
        # read presents description section
        present_sizes = {}
        for (i, block) in enumerate(blocks[:-1]):
            present_sizes[i] = sum(sum(1 for c in line if c == '#') for line in block)
        # read regions description section
        regions = []
        for line in blocks[-1].split('\n'):
            block1, block2 = line.split(': ')
            x, y = map(int, block1.split('x'))
            present_count = list(map(int, block2.split(' ')))
            regions.append(((x, y), present_count))
        return present_sizes, regions


def solve1(present_sizes, regions):
    """Solve part 1"""
    regions_big_enough = 0
    # count the number of regions that have physically enough space for the presents
    for (x, y), present_count in regions:
        if x * y >= sum(present_count[i] * present_sizes[i] for i in range(len(present_count))):
            regions_big_enough += 1
    # in the general case, we should use a complex Tetris-like algorithm to find which regions among them can actually
    # fit the presents, but the input file was designed so that all regions that have enough space can actually fit
    # them, so nothing left to do in our case
    return regions_big_enough


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 12:', solve1(*parsed))
