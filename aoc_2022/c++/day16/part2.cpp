#include "part2.h"

using namespace std;


namespace Day16 {
    namespace Part2 {

        struct State {
            set<string> openValves {};
            std::array<string, 2> position;
            std::array<int, 2>    time;
            int score { 0 };
        };

        int solve(const map<string, Valve>& valves) {
            int bestScore = 0;
            vector<int> playerIds {0, 1};

            // keep track for each pair of positions (ordered by alphabetical order) the times and score to get there
            // (location1, location2) -> (time to activate valve 1, time to activate valve 2, score)
            map<pair<string, string>, set<tuple<int, int, int>>> cache;
            for (const auto& v1 : valves | views::keys) {
                for (const auto& v2 : valves | views::keys) {
                    if (v1 <= v2) {
                        cache.insert({ {v1, v2}, {} });
                    }
                }
            }

            deque<State> toCheck {};
            toCheck.push_back(State{ { "AA" }, { "AA", "AA" } , { 0, 0 }, 0 });

            while (toCheck.size() > 0) {
                const auto& state = toCheck.front();

                // abandon this path if a better state is found in cache
                bool skip = false;
                const int player1 = state.position[0] <= state.position[1] ? 0 : 1;
                const int player2 = 1 - player1;
                for (const auto& [time1, time2, score] : cache[pair{ state.position[player1], state.position[player2] }]) {
                    if (time1 <= state.time[player1] && time2 <= state.time[player2] && score >= state.score) {
                        skip = true;
                        break;
                    }
                }
                if (skip) {
                    toCheck.pop_front();
                    continue;
                }

                // abandon this path if it has no chance to go beyond the best score
                int maxPossible = state.score;
                int remainingTime = 26 - min(state.time[0], state.time[1]);
                for (const auto& v : valves | views::keys) {
                    if (state.openValves.find(v) == state.openValves.end()) {
                        maxPossible += remainingTime * valves.at(v).rate;
                    }
                }
                if (maxPossible <= bestScore) {
                    toCheck.pop_front();
                    continue;
                }

                // add this path to the cache
                cache[{state.position[player1], state.position[player2]}].insert({ state.time[player1], state.time[player2], state.score });
                
                for (const auto& nextValve : valves | views::keys) {
                    if (nextValve == "AA" || state.openValves.find(nextValve) != state.openValves.end()) {
                        // cannot open this valve
                        continue;
                    }
                    for (const int playerId : playerIds) {
                        const int nextTime = state.time[playerId] + valves.at(state.position[playerId]).tunnels.at(nextValve) + 1;
                        if (nextTime < 26) {
                            State nextState { state };
                            nextState.openValves.insert(nextValve);
                            nextState.position[playerId] = nextValve;
                            nextState.time[playerId] = nextTime;
                            nextState.score += (26 - nextTime) * valves.at(nextValve).rate;
                            bestScore = max(bestScore, nextState.score);
                            toCheck.push_back(nextState);
                        }
                    }
                }
                toCheck.pop_front();
            }
            return bestScore;
        }

    }
}
