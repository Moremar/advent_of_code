import re


class Password:
    def __init__(self, i1, i2, letter, word):
        self.i1 = int(i1)
        self.i2 = int(i2)
        self.letter = letter
        self.word = word

    def is_valid(self):
        return self.i1 <= self.word.count(self.letter) <= self.i2


def solve(passwords):
    return len([p for p in passwords if p.is_valid()])


def parse_line(line):
    m = re.match(r'^([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)$', line.strip())
    return Password(m.group(1), m.group(2), m.group(3), m.group(4))


def parse(file_name):
    with open(file_name, 'r') as f:
        return [parse_line(line.strip()) for line in f.readlines()]


if __name__ == '__main__':
    print(solve(parse('sample.txt')))
