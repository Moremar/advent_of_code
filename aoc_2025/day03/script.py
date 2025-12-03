"""Solution for AOC 2025 day 3"""

def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        return [list(map(int, list(line.strip()))) for line in file.readlines()]


def get_joltage(battery_bank, joltage_size):
    """Calculate the max joltage of a given size for a battery bank"""
    joltage = [battery_bank[i] for i in range(joltage_size)]
    max_k = 0  # only the first battery of the joltage (index 0) can be updated at the very beginning
    for i in range(len(battery_bank)):
        updated = False
        # loop from 0 to the index of the highest updatable battery in the joltage
        for k in range(max_k + 1):
            if i - k + joltage_size > len(battery_bank):
                # cannot update this joltage index, there are not enough batteries left in the bank to fill the rest
                continue
            if battery_bank[i] > joltage[k]:
                # update the joltage at index k
                joltage = joltage[:k] + battery_bank[i:i + joltage_size - k]
                # since we updated the joltage at index k, we can only update it up to index k+1 at the next iteration
                max_k = min(k + 1, joltage_size - 1)
                updated = True
                break
        if not updated:
            # no joltage index was updated with this battery, so the next iteration can update one index further
            max_k = min(max_k + 1, joltage_size - 1)
    return int(''.join(map(str, joltage)))


def solve1(battery_banks):
    """Solve part 1"""
    return sum(get_joltage(battery_bank, 2) for battery_bank in battery_banks)


def solve2(battery_banks):
    """Solve part 2"""
    return sum(get_joltage(battery_bank, 12) for battery_bank in battery_banks)


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 3:', solve1(parsed), solve2(parsed))
