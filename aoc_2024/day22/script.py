"""Solution for AOC 2024 day 22"""


def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        return list(map(int, file.readlines()))


def mix(val, secret):
    """Mix a secret"""
    return val ^ secret


def prune(secret):
    """Prune a secret"""
    return secret % 16777216


def get_next(secret):
    """Get the next pseudo-random secret number"""
    secret = prune(mix(64 * secret, secret))
    secret = prune(mix(secret // 32, secret))
    return prune(mix(2048 * secret, secret))


def solve1(secret_numbers):
    """Solve part 1"""
    result = 0
    for secret in secret_numbers:
        for i in range(2000):
            secret = get_next(secret)
        result += secret
    return result


def solve2(secret_numbers):
    """Solve part 2"""
    banana_count = {}
    for secret in secret_numbers:
        changes = (None, None, None, None)
        seen = set()
        prev_price = secret % 10
        for i in range(2000):
            secret = get_next(secret)
            price = secret % 10
            changes = (changes[1], changes[2], changes[3], price - prev_price)
            prev_price = price
            if changes[0] is not None and changes not in seen:
                seen.add(changes)
                if changes not in banana_count:
                    banana_count[changes] = 0
                banana_count[changes] += price
    return max([banana_count[sequence] for sequence in banana_count])


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 22:', solve1(parsed), solve2(parsed))
