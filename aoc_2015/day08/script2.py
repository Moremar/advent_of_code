from script1 import parse


def difference(word):
    code_length = len(word)
    encoded_length = 2  # opening and closing quotes
    pos = 0
    while pos < len(word):
        encoded_length += 1
        if word[pos] in ["\\", "\""]:
            encoded_length += 1
        pos += 1
    return encoded_length - code_length


def solve(words):
    return sum([difference(word) for word in words])


if __name__ == '__main__':
    print(solve(parse("data.txt")))
