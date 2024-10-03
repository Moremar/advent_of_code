#!/usr/bin/env python3
import re
import time


class Sensor:
    def __init__(self, sx, sy, bx, by):
        self.x = sx
        self.y = sy
        self.beacon = (bx, by)
        self.distance = abs(sx - bx) + abs(sy - by)


def parse(input_path):
    with open(input_path, 'r') as f:
        return [Sensor(*tuple(map(int, re.findall(r'[-\d]+', line)))) for line in f.readlines()]


def merge_intervals(intervals):
    assert len(intervals) > 0
    intervals.sort()
    res = [intervals[0]]
    for interval in intervals[1:]:
        if res[-1][0] <= interval[0] <= res[-1][-1] + 1:
            res[-1][-1] = max(res[-1][-1], interval[-1])
        else:
            res.append(interval)
    return res


def solve_part1(sensors, target_y):
    intervals = []
    for sensor in sensors:
        half_span = sensor.distance - abs(sensor.y - target_y)
        if half_span <= 0:
            continue  # no covered area in row target_y for this sensor
        intervals.append([sensor.x - half_span, sensor.x + half_span])
    intervals = merge_intervals(intervals)

    beacons = set([s.beacon for s in sensors
                   if s.beacon[1] == target_y
                   and any([a <= s.beacon[0] <= b for [a, b] in intervals])])

    return sum([s[1] - s[0] + 1 for s in intervals]) - len(beacons)


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve_part1(parsed, 2000000)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
