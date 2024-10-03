def is_nice(word):
    has_double = False
    vowel_count = word[0] in "aeiou"
    for i in range(1, len(word)):
        if word[i] == word[i-1]:
            has_double = True
        if word[i] in "aeiou":
            vowel_count += 1
        if (word[i-1] + word[i]) in ["ab", "cd", "pq", "xy"]:
            return False
    return has_double and vowel_count >= 3


def solve(words):
    return len([word for word in words if is_nice(word)])


def parse(file_name):
    with open(file_name, "r") as f:
        return [line.strip() for line in f.readlines()]


if __name__ == '__main__':
    print(solve(parse("data.txt")))
