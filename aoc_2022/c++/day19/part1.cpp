#include "part1.h"

using namespace std;

const int ORE      = 0;
const int CLAY     = 1;
const int OBSIDIAN = 2;
const int GEODE    = 3;

namespace Day19 {

    vector<Blueprint> parse(const string& filename) {
        vector<Blueprint> blueprints {};
        const regex pattern  { "Blueprint \\d+: Each ore robot costs (\\d+) ore. "
                               "Each clay robot costs (\\d+) ore. "
                               "Each obsidian robot costs (\\d+) ore and (\\d+) clay. "
                               "Each geode robot costs (\\d+) ore and (\\d+) obsidian." };
        for (const auto line : getFileLines(filename)) {
            smatch match;
            regex_search(line.begin(), line.end(), match, pattern);
            Blueprint blueprint {
                array<int, 4>{ stoi(match[1]),              0,              0, 0 },
                array<int, 4>{ stoi(match[2]),              0,              0, 0 },
                array<int, 4>{ stoi(match[3]), stoi(match[4]),              0, 0 },
                array<int, 4>{ stoi(match[5]),              0, stoi(match[6]), 0 },
            };
            blueprints.push_back(blueprint);
        }
        return blueprints;
    }

    struct State {
        array<int, 4> resources { 0, 0, 0, 0 };
        array<int, 4> bots { 1, 0, 0, 0 };
        int time = 0;
    };

    namespace Part1 {

        int calculateMaxGeodes(const Blueprint& blueprint, const int maxTime) {

            // we can build only 1 bot at a time, so it is useless to have more bots of a resource
            // than the maximum required of that resource for a bot construction
            array<int, 3> maxUsefulBots;
            for (int i = 0; i < 3; ++i) {
                for (int j = 0; j < 4; ++j) {
                    maxUsefulBots[i] = max(maxUsefulBots[i], blueprint[j][i]);
                }
            }

            int maxGeodes = 0;
            deque<State> toCheck { State{} };
            vector<State> nextStates {};
            while (toCheck.size() > 0) {
                const auto& state = toCheck.front();

                maxGeodes = max(maxGeodes, state.resources[GEODE] + state.bots[GEODE]);

                // schedule the build of each type of bot if it is useful
                for (int resource = 0; resource < 4; ++resource) {
                    // skip that bot type if we already have enough bots
                    if (resource != GEODE && state.bots[resource] >= maxUsefulBots[resource]) {
                        continue;
                    }
                    // skip that bot if we cannot produce it yet
                    if ((resource == OBSIDIAN && state.bots[CLAY] == 0) || (resource == GEODE && state.bots[OBSIDIAN] == 0)) {
                        continue;
                    }
                    int timeToGetResources = 0;
                    for (int i = 0; i < 3; ++i) {
                        const int missingResources = blueprint[resource][i] - state.resources[i];
                        int time = 0;
                        if (missingResources > 0) {
                            time = missingResources / state.bots[i] + (missingResources % state.bots[i] == 0 ? 0 : 1);
                        }
                        timeToGetResources = max(timeToGetResources, time);
                    }
                    ++timeToGetResources;  // +1 for the time to build the bot
                    if (state.time + timeToGetResources < maxTime) {
                        State nextState { state };
                        nextState.time += timeToGetResources;
                        ++nextState.bots[resource];                        
                        for (int i = 0; i < 4; ++i) {
                            nextState.resources[i] += timeToGetResources * state.bots[i] - blueprint[resource][i];
                        }
                        toCheck.push_back(nextState);
                    }
                }
                toCheck.pop_front();
            }

            return maxGeodes;
        }


        int solve(const vector<Blueprint>& blueprints) {
            int result = 0;
            for (int i = 0; i < blueprints.size(); ++i) {
                result += calculateMaxGeodes(blueprints[i], 24) * (i + 1);
            }
            return result;
        }

    }
}
