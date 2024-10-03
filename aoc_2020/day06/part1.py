from collections import Counter


def solve(answers):
    return sum([len(counter) for (_, counter) in answers])


def parse(file_name):
    answers = []
    with open(file_name, 'r') as f:
        for group in f.read().split('\n\n'):
            people_nb = group.count('\n') + 1
            counter = Counter(group.replace('\n', ''))
            answers.append((people_nb, counter))
        return answers


if __name__ == '__main__':
    print(solve(parse('data.txt')))
