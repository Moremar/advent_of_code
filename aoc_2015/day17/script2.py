from script1 import parse, get_combinations


def solve(recipients):
    combinations = []
    get_combinations([], recipients, 150, combinations)
    nb_of_recipients = [sum(combination) for combination in combinations]
    return nb_of_recipients.count(min(nb_of_recipients))


if __name__ == '__main__':
    print(solve(parse("data.txt")))
