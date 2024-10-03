#!/usr/bin/env python3
import collections
import re
import time


class Valve:
    def __init__(self, rate, lead_to):
        self.rate = rate
        self.lead_to = {valve: 1 for valve in lead_to}


class State:
    def __init__(self, location, valves, visited, time, score):
        self.location = location
        self.valves = valves
        self.visited = visited
        self.time = time
        self.score = score


def simplify_valves(valves):
    # many valves in the input file have a rate of zero, so they cannot be opened.
    # they can be treated as a simple tunnel between actual valves, so we remove them and simply
    # increase the distance between the connected valves
    for valve_name in set(name for name in valves):
        if valve_name == 'AA':  # starting valve, can't simplify it
            continue
        if valves[valve_name].rate == 0:
            for v1 in valves[valve_name].lead_to:
                for v2 in valves[valve_name].lead_to:
                    if v1 != v2:
                        valves[v1].lead_to[v2] = valves[valve_name].lead_to[v1] + valves[valve_name].lead_to[v2]
                        del valves[v1].lead_to[valve_name]
            del valves[valve_name]


def parse(input_path):
    with open(input_path, 'r') as f:
        valves = {}
        for line in f.readlines():
            name, rate, lead_to = re.match(
                r'Valve ([A-Z]+) has flow rate=(\d+); tunnel[s]* lead[s]* to valve[s]* ([A-Z, ]+)', line).groups()
            valves[name] = Valve(int(rate), lead_to.split(', '))
        simplify_valves(valves)
        return valves


def solve_part1(valves):
    max_time = 30
    seen = {name: {} for name in valves}
    best_score = 0
    to_check = collections.deque()
    to_check.append(State('AA', set(), {'AA'}, 0, 0))

    while len(to_check):
        curr_state = to_check.popleft()
        best_score = max(best_score, curr_state.score)

        # no more processing if all valves are opens (except AA that has rate = 0)
        if  len(curr_state.valves) == len(valves)-1:
            continue

        if curr_state.time >= max_time:
            continue

        # discard the state if no more chance to beat the current best score
        remaining_rate = sum([valves[v].rate for v in valves if v not in curr_state.valves])
        if curr_state.score + remaining_rate * (max_time - curr_state.time) <= best_score:
            continue

        # discard the state if a better state was already processed
        tuple_key = tuple(curr_state.valves)
        if tuple_key not in seen[curr_state.location]:
            seen[curr_state.location][tuple_key] = []
        if any([t <= curr_state.time and s >= curr_state.score for (t, s) in seen[curr_state.location][tuple_key]]):
            continue
        else:
            seen[curr_state.location][tuple_key].append((curr_state.time, curr_state.score))

        # open the valve
        if valves[curr_state.location].rate > 0 and curr_state.location not in curr_state.valves:
            to_check.append(State(curr_state.location,
                                  curr_state.valves | {curr_state.location},
                                  {curr_state.location},
                                  curr_state.time + 1,
                                  curr_state.score + valves[curr_state.location].rate * (max_time - curr_state.time - 1)))

        # discard the state if we have already been here since the last valve we opened
        for next_valve in valves[curr_state.location].lead_to:
            if next_valve in curr_state.visited:
                continue

            to_check.append(State(next_valve,
                                  curr_state.valves,
                                  curr_state.visited | {next_valve},
                                  curr_state.time + valves[curr_state.location].lead_to[next_valve],
                                  curr_state.score))
    return best_score


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve_part1(parsed)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
