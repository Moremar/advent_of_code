#include "part1.hpp"
#include "part2.hpp"

using namespace std;


int Part2::solve(const string &password) {
    Coordinates target(3, 3);
    size_t longest = 0;
    State initialState(Coordinates(0, 0), password, "");
    list<State> toCheck { initialState };
    while (toCheck.size() > 0) {
        const auto curr = toCheck.front();
        toCheck.pop_front();
        for (const auto &state : curr.getNextStates()) {
            if (state.getCoordinates() == target) {
                longest = max(longest, state.getPath().size());
            } else {
                toCheck.push_back(state);
            }
        }
    }
    return longest;
}

