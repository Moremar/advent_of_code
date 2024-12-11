"""Solution for AOC 2024 day 11"""

# cache the number of stones that a stone generates after a given number of blinks
CACHE = {}


def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        return list(map(int, file.read().split(' ')))


def count_stones(stone_val, blinks):
    """count how many stones a stone generates after a given number of blinks"""
    if (stone_val, blinks) not in CACHE:
        if blinks == 0:
            generated_stones = 1
        elif stone_val == 0:
            generated_stones = count_stones(1, blinks - 1)
        else:
            stone_str = f'{stone_val}'
            if len(stone_str) % 2 == 0:
                generated_stones = count_stones(int(stone_str[:len(stone_str) // 2]), blinks - 1) \
                                   + count_stones(int(stone_str[len(stone_str) // 2:]), blinks - 1)
            else:
                generated_stones = count_stones(stone_val * 2024, blinks - 1)
        CACHE[(stone_val, blinks)] = generated_stones

    return CACHE[(stone_val, blinks)]


def solve(stones, blinks):
    """Count the total number of stones after a given number of blinks"""
    return sum(count_stones(stone, blinks) for stone in stones)


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 11:', solve(parsed, 25), solve(parsed, 75))
