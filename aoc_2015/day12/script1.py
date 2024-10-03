def solve(json_str):
    total = 0
    curr_nb = ""
    for c in json_str:
        if c in "-0123456789":
            curr_nb = curr_nb + c
        elif len(curr_nb) > 0:
            total += int(curr_nb)
            curr_nb = ""
    return total


def parse(file_name):
    with open(file_name, "r") as f:
        return f.readline().strip()


if __name__ == '__main__':
    print(solve(parse("data.txt")))
