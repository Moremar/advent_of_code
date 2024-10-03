def difference(word):
    code_length = len(word)
    string_length = 0
    pos = 1  # skip opening and closing quotes
    while pos < len(word) - 1:
        if word[pos] == "\\" and word[pos+1] in ["\\", "\""]:
            pos += 2
        elif word[pos] == "\\" and word[pos+1] == "x":
            pos += 4
        else:
            pos += 1
        string_length += 1
    return code_length - string_length


def solve(words):
    return sum([difference(word) for word in words])


def parse(file_name):
    with open(file_name, "r") as f:
        return [line.strip() for line in f.readlines()]


if __name__ == '__main__':
    print(solve(parse("data.txt")))
