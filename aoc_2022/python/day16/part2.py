#!/usr/bin/env python3
import collections
import time
import part1


# This solution is very memory-intensive, to run it on Pycharm we need to increase the available memory
# with the interpreter parameter -Xmx4096m, it then completes in around 2 minutes


class State:
    def __init__(self, location_me, location_el, valves, visited_me, visited_el, time_me, time_el, score):
        self.location_me = location_me
        self.location_el = location_el
        self.valves = valves
        self.visited_me = visited_me
        self.visited_el = visited_el
        self.time_me = time_me
        self.time_el = time_el
        self.score = score


def solve_part2(valves):
    max_time = 26
    current_minute = 0
    seen = {(name1, name2): {} for name1 in valves for name2 in valves}
    best_score = 0
    to_check = collections.deque()
    to_check.append(State('AA', 'AA', set(), {'AA'}, {'AA'}, 0, 0, 0))
    while len(to_check):
        curr_state = to_check.popleft()
        best_score = max(best_score, curr_state.score)

        # keep track of the highest minute being checked
        if curr_state.time_me > current_minute:
            current_minute = curr_state.time_me

        # no more processing if all valves are opens (except AA that has rate = 0)
        if len(curr_state.valves) == len(valves)-1:
            continue

        if curr_state.time_me >= max_time and curr_state.time_el >= max_time:
            continue

        # discard the state if no more chance to beat the current best score
        remaining_rate = sum([valves[v].rate for v in valves if v not in curr_state.valves])
        if curr_state.score + remaining_rate * (max_time - max(curr_state.time_me, curr_state.time_el)) <= best_score:
            continue

        # heuristic to avoid processing many states that are extremely unlikely to give the highest score :
        # after the 8th minute, we discard any state that has a score lower than half the best score found so far
        # this heuristic divides by 3 the time to find the best score (154s instead of 422s)
        if current_minute > 8 and curr_state.score < best_score//2:
            continue

        # discard the state if a better state was processed
        location = (curr_state.location_me, curr_state.location_el)
        tuple_key = tuple(curr_state.valves)
        if tuple_key not in seen[location]:
            seen[location][tuple_key] = []
        if any([t <= min(curr_state.time_me, curr_state.time_el) and s >= curr_state.score
                for (t, s) in seen[location][tuple_key]]):
            continue
        else:
            seen[location][tuple_key].append((max(curr_state.time_me, curr_state.time_el), curr_state.score))

        # always move either me or the elephant, whichever has the smallest time elapsed
        if curr_state.time_me <= curr_state.time_el:   # move me

            # open the valve
            if valves[curr_state.location_me].rate > 0 and curr_state.location_me not in curr_state.valves:
                to_check.append(State(curr_state.location_me,
                                      curr_state.location_el,
                                      curr_state.valves | {curr_state.location_me},
                                      {curr_state.location_me},
                                      curr_state.visited_el,
                                      curr_state.time_me + 1,
                                      curr_state.time_el,
                                      curr_state.score + valves[curr_state.location_me].rate * (26 - curr_state.time_me - 1)))

            # discard the state if we have already been here since the last valve we opened
            for next_valve in valves[curr_state.location_me].lead_to:
                if next_valve in curr_state.visited_me:
                    continue

                to_check.append(State(next_valve,
                                      curr_state.location_el,
                                      curr_state.valves,
                                      curr_state.visited_me | {next_valve},
                                      curr_state.visited_el,
                                      curr_state.time_me + valves[curr_state.location_me].lead_to[next_valve],
                                      curr_state.time_el,
                                      curr_state.score))

        else:    # move the elephant

            # open the valve
            if valves[curr_state.location_el].rate > 0 and curr_state.location_el not in curr_state.valves:
                to_check.append(State(curr_state.location_me,
                                      curr_state.location_el,
                                      curr_state.valves | {curr_state.location_el},
                                      curr_state.visited_me,
                                      {curr_state.location_el},
                                      curr_state.time_me,
                                      curr_state.time_el + 1,
                                      curr_state.score + valves[curr_state.location_el].rate * (
                                                  26 - curr_state.time_el - 1)))

            # discard the state if the elephant has already been here since the last valve he opened
            for next_valve in valves[curr_state.location_el].lead_to:
                if next_valve in curr_state.visited_el:
                    continue

                to_check.append(State(curr_state.location_me,
                                      next_valve,
                                      curr_state.valves,
                                      curr_state.visited_me,
                                      curr_state.visited_el | {next_valve},
                                      curr_state.time_me,
                                      curr_state.time_el + valves[curr_state.location_el].lead_to[next_valve],
                                      curr_state.score))
    return best_score


if __name__ == "__main__":
    start = time.time()
    parsed = part1.parse("data.txt")
    result = solve_part2(parsed)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
