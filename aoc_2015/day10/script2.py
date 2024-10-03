from script1 import parse, look_and_say


def solve(start_word):
    words = [start_word]
    for i in range(0, 50):
        words.append(look_and_say(words[-1]))
    return len(words[-1])


if __name__ == '__main__':
    print(solve(parse("data.txt")))
