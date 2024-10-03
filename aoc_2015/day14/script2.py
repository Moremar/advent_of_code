from script1 import parse


def solve(deers):
    state = {}
    for deer_name in deers:
        state[deer_name] = {"score": 0, "distance": 0}

    # play the race turn by turn
    top_deers = []
    top_distance = 0
    for turn in range(1, 2503 + 1):
        for deer_name in deers:
            deer = deers[deer_name]
            equiv_turn = turn % deer.period
            if 0 < equiv_turn <= deer.run_time:  # deer is running
                state[deer_name]["distance"] += deer.speed
            if state[deer_name]["distance"] == top_distance and deer_name not in top_deers:
                # 2 deers have the same best distance
                top_deers.append(deer_name)
            elif state[deer_name]["distance"] > top_distance:
                # 1 deer makes a new best distance
                top_distance = state[deer_name]["distance"]
                top_deers = [deer_name]
        for top_deer in top_deers:
            state[top_deer]["score"] += 1

    return max([state[deer_name]["score"] for deer_name in deers])


if __name__ == '__main__':
    print(solve(parse("data.txt")))
