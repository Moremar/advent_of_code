def look_and_say(word):
    next_word = ""
    prev_digit = ""
    prev_digit_count = 0
    for c in word:
        if c == prev_digit:
            prev_digit_count += 1
        elif prev_digit_count > 0:
            next_word += str(prev_digit_count) + prev_digit
            prev_digit_count = 1
            prev_digit = c
        else:  # first iteration
            prev_digit_count = 1
            prev_digit = c
    # add last block of digits
    next_word += str(prev_digit_count) + prev_digit
    return next_word


def solve(start_word):
    words = [start_word]
    for i in range(0, 40):
        words.append(look_and_say(words[-1]))
    return len(words[-1])


def parse(file_name):
    with open(file_name, "r") as f:
        return f.readline().strip()


if __name__ == '__main__':
    print(solve(parse("data.txt")))
