from script1 import parse


def is_nice(word):
    pair_repeated = False
    sandwich_letter = False
    for i in range(0, len(word)-1):
        pair = word[i] + word[i+1]
        if pair in word[:i] or pair in word[i+2:]:
            pair_repeated = True
    for i in range(0, len(word)-2):
        if word[i] == word[i+2]:
            sandwich_letter = True
    return pair_repeated and sandwich_letter


def solve(words):
    return len([word for word in words if is_nice(word)])


if __name__ == '__main__':
    print(solve(parse("data.txt")))
