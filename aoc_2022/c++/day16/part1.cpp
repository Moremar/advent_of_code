#include "part1.h"

using namespace std;


namespace Day16 {

    /*
     * Valves with rate = 0 are useless, they are just tunnels.
     * We can remove them and connect directly the valves linked to them
     * this reduces the total number of valves of the graph
     * We keep only valve AA with a zero rate, as it is the starting point.
     */
    void reduceValves(map<string, Valve>& valves) {
        set<string> deletedValves;
        for (const auto& valveName : valves | views::keys) {
            if (valves[valveName].rate == 0 && valveName != "AA") {
                for (const auto& v1 : valves[valveName].tunnels | views::keys) {
                    for (const auto& v2 : valves[valveName].tunnels | views::keys) {
                        if (v1 == v2) continue;
                        const int distance = valves[valveName].tunnels[v1] + valves[valveName].tunnels[v2];
                        valves[v1].tunnels.insert({ v2, distance });
                        valves[v2].tunnels.insert({ v1, distance });
                        valves[v1].tunnels.erase(valveName);
                        valves[v2].tunnels.erase(valveName);
                    }
                }
                deletedValves.insert(valveName);
            }
        }
        for (const auto& valveName : deletedValves) valves.erase(valveName);
    }

    /*
     * We need to go to one valve to another, and find the best order to maximize the total rate.
     * To simplify the traversal, we enrich the tunnels to calculate the optimal path from each valve to each valve.
     */
    void expandValves(map<string, Valve>& valves) {
        for (const auto& origin : valves | views::keys) {
            map<string, int> bestDist {};
            for (const auto& dest : valves | views::keys) {
                bestDist[dest] = -1;
            }
            bestDist[origin] = 0;
            deque<string> toCheck { origin };
            while (toCheck.size() > 0) {
                const auto& curr = toCheck.front();
                for (const auto& [v, d] : valves[curr].tunnels) {
                    if (bestDist[v] == -1 || bestDist[curr] + d < bestDist[v]) {
                        bestDist[v] = bestDist[curr] + d;
                        toCheck.push_back(v);
                    }
                }
                toCheck.pop_front();
            }
            bestDist.erase(origin);
            valves[origin].tunnels = bestDist;
        }
    }

    map<string, Valve> parse(const string& filename) {
        map<string, Valve> valves;
        const regex pattern { "Valve ([A-Z]{2}) has flow rate=(\\d+); tunnels? leads? to valves? ([A-Z, ]+)" };
        for (const auto& line : getFileLines(filename)) {
            smatch match;
            regex_search(line.begin(), line.end(), match, pattern);
            Valve valve { match[1], stoi(match[2]) };
            for (const auto& destValve : split(match[3], ", ")) {
                valve.tunnels.insert({ destValve, 1 });
            }
            valves.insert({ valve.name,  valve });
        }
        reduceValves(valves);
        expandValves(valves);
        return valves;
    }

    namespace Part1 {

        struct State {
            set<string> openValves {};
            string position;
            int time;
            int score;
        };

        int solve(const map<string, Valve>& valves) {
            int bestScore = 0;
            deque<State> toCheck {};
            toCheck.push_back(State{ { "AA" }, "AA", 0, 0 });
            while (toCheck.size() > 0) {
                const auto& state = toCheck.front();
                for (const auto& nextValve : valves | views::keys) {
                    if (nextValve == "AA" || state.openValves.find(nextValve) != state.openValves.end()) {
                        // cannot open the valve there
                        continue;
                    }
                    const int nextTime = state.time + valves.at(state.position).tunnels.at(nextValve) + 1;
                    if (nextTime >= 30) {
                        // not enough time to go open that valve
                        continue;
                    }
                    State nextState { state };
                    nextState.openValves.insert(nextValve);
                    nextState.position = nextValve;
                    nextState.time = nextTime;
                    nextState.score += (30 - nextTime) * valves.at(nextValve).rate;
                    bestScore = max(bestScore, nextState.score);
                    toCheck.push_back(nextState);
                }
                toCheck.pop_front();
            }
            return bestScore;
        }

    }
}
