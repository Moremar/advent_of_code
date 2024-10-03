import re


class Deer:
    def __init__(self, name, speed, run_time, rest_time):
        self.name = name
        self.speed = speed
        self.run_time = run_time
        self.rest_time = rest_time
        self.period = run_time + rest_time
        self.one_run = run_time * speed


def distance_ran(deer, time):
    distance = (time // deer.period) * deer.one_run
    time = time % deer.period
    if time > deer.run_time:
        distance += deer.one_run
    else:
        distance += deer.speed * time
    return distance


def solve(deers):
    return max([distance_ran(deers[deer_name], 2503) for deer_name in deers])


def parse(file_name):
    with open(file_name, "r") as f:
        deers = {}
        for line in f.readlines():
            _, deer_name, speed, run_time, rest_time, _ = re.split(
                r"([A-Za-z]+) can fly ([0-9]+) km/s for ([0-9]+) .* ([0-9]+)", line)
            deers[deer_name] = Deer(deer_name, int(speed), int(run_time), int(rest_time))
        return deers


if __name__ == '__main__':
    print(solve(parse("data.txt")))
