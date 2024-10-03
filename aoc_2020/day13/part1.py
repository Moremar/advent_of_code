def solve(data):
    earliest, buses = data
    best_bus, min_time_to_wait = buses[0][1], buses[0][1]
    for (_, bus_id) in buses:
        time_to_wait = ((earliest // bus_id) + 1) * bus_id - earliest
        if time_to_wait < min_time_to_wait:
            best_bus = bus_id
            min_time_to_wait = time_to_wait
    return best_bus * min_time_to_wait


def parse(file_name):
    with open(file_name, 'r') as f:
        line1, line2 = f.readlines()
        return int(line1), [(i, int(n)) for (i, n) in enumerate(line2.split(',')) if n != 'x']


if __name__ == "__main__":
    print(solve(parse("data.txt")))
