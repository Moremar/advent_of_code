#!/usr/bin/env python3
import re
import time

ORE, CLAY, OBS, GEODE = 0, 1, 2, 3
CACHE = {}
BOT_MAX = {}


class Blueprint:
    def __init__(self, num, orebot_ore, claybot_ore, obsbot_ore, obsbot_clay, geobot_ore, geobot_obs):
        self.num = num
        self.bots = (orebot_ore,  0, 0), \
                    (claybot_ore, 0, 0), \
                    (obsbot_ore,  obsbot_clay, 0), \
                    (geobot_ore,  0, geobot_obs)


def parse(input_path):
    with open(input_path, 'r') as f:
        return [ Blueprint(*tuple(map(int, re.findall(r'\d+', line)))) for line in f.readlines()]


def resolve(blueprint, bots, resources, remaining_time):

    # cap the amount of each resource owned to the maximum usable in the remaining time
    # this allows to hit the cache more often
    for type in [ORE, CLAY, OBS]:
        resources[type] = min(resources[type], BOT_MAX[type] * remaining_time)

    # return the result if already in cache
    key = (*bots, *resources, remaining_time)
    if key in CACHE:
        return CACHE[key]

    # final score if we do not construct any more robots for the remaining time
    result = resources[GEODE] + remaining_time * bots[GEODE]

    # check the best final score when creating each type of robot
    for type in [ORE, CLAY, OBS, GEODE]:

        if type != GEODE and bots[type] >= BOT_MAX[type]:
            # we do not need any more robot of this type
            continue

        if (type == OBS and bots[CLAY] == 0) or (type == GEODE and bots[OBS] == 0):
            # do not own yet the robots to generate required resources
            continue

        # time needed to accumulate enough resources and build this bot
        ore_needed = max(0, blueprint.bots[type][ORE] - resources[ORE])
        time_required = (ore_needed // bots[ORE]) + (0 if ore_needed % bots[ORE] == 0 else 1)
        if type == OBS:
            clay_needed = max(0, blueprint.bots[type][CLAY] - resources[CLAY])
            time_required_clay = (clay_needed // bots[CLAY]) + (0 if clay_needed % bots[CLAY] == 0 else 1)
            time_required = max(time_required, time_required_clay)
        elif type == GEODE:
            obs_needed = max(0, blueprint.bots[type][OBS] - resources[OBS])
            time_required_obs = (obs_needed // bots[OBS]) + (0 if obs_needed % bots[OBS] == 0 else 1)
            time_required = max(time_required, time_required_obs)
        time_required += 1

        if time_required < remaining_time:
            new_bots = bots[:type] + [bots[type]+1] + bots[type+1:]
            new_resources = [resources[x] + time_required * bots[x] for x in [ORE, CLAY, OBS, GEODE]]
            new_resources[ORE] -= blueprint.bots[type][ORE]
            new_resources[CLAY] -= blueprint.bots[type][CLAY]
            new_resources[OBS] -= blueprint.bots[type][OBS]
            result = max(result, resolve(blueprint, new_bots, new_resources, remaining_time - time_required))

    CACHE[key] = result
    return result


def best_geode_number(blueprint, time):
    # clear the cache between each blueprint
    CACHE.clear()
    # set the maximum number of each resource that is useful to own at any given time
    BOT_MAX[ORE] = max(blueprint.bots[ORE][ORE],
                       blueprint.bots[CLAY][ORE],
                       blueprint.bots[OBS][ORE],
                       blueprint.bots[GEODE][ORE])
    BOT_MAX[CLAY] = blueprint.bots[OBS][CLAY]
    BOT_MAX[OBS] = blueprint.bots[GEODE][OBS]

    return resolve(blueprint, [1, 0, 0, 0], [0, 0, 0, 0], time)


def solve_part1(blueprints, time):
    return sum([blueprint.num * best_geode_number(blueprint, time) for blueprint in blueprints])


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve_part1(parsed, 24)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')