#include "part1.hpp"

using namespace std;


State::State(const Coordinates &coords, const string &password, const string &path)
    : myCoords(coords), myPassword(password), myPath(path) {}


vector<State> State::getNextStates() const {
    vector<char> dirChars { 'U', 'D', 'L', 'R' };
    vector<Coordinates> dirs = { Coordinates(0, -1), Coordinates(0,  1),
                                 Coordinates(-1, 0), Coordinates(1,  0) };
    vector<State> res;
    const auto hash = md5(myPassword + myPath);
    for (size_t i = 0; i < 4; i++) {
        if ("bcdef"s.find(hash.at(i)) != string::npos) {
            Coordinates nextCoords(myCoords.first + dirs.at(i).first,
                               myCoords.second + dirs.at(i).second);
            if (nextCoords.first < 0 | nextCoords.first > 3 
                    | nextCoords.second < 0 | nextCoords.second > 3) {
                // out of the grid
                continue;
            }
            res.emplace_back(nextCoords, myPassword, myPath + dirChars.at(i));
        }
    }
    return res;
}


string Part1::parse(const string &fileName) {
    return getFileLines(fileName)[0];
}


string Part1::solve(const string &password) {
    Coordinates target(3, 3);
    State initialState(Coordinates(0, 0), password, "");
    list<State> toCheck { initialState };
    while (toCheck.size() > 0) {
        const auto curr = toCheck.front();
        toCheck.pop_front();
        for (const auto &state : curr.getNextStates()) {
            if (state.getCoordinates() == target) {
                return state.getPath();
            }
            toCheck.push_back(state);
        }
    }
    throw AdventException("No path found to the vault");
}
