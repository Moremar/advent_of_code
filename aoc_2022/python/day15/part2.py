#!/usr/bin/env python3
import time
import part1


def solve_part2(sensors, bound):
    for y in range(bound+1):
        intervals = []
        for sensor in sensors:
            half_span = sensor.distance - abs(sensor.y - y)
            if half_span <= 0:
                continue
            if sensor.x - half_span > bound or sensor.x + half_span < 0:
                continue
            intervals.append([max(0, sensor.x - half_span), min(sensor.x + half_span, bound+1)])
        intervals = part1.merge_intervals(intervals)
        if len(intervals) != 1:
            return 4000000 * (intervals[0][1] + 1) + y


if __name__ == "__main__":
    start = time.time()
    parsed = part1.parse("data.txt")
    result = solve_part2(parsed, 4000000)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
