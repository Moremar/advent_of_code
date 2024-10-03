#include "part1.hpp"

using namespace std;


bool State::operator==(const State &state) const {
    return floor == state.floor && pairs == state.pairs;
}


bool State::operator<(const State &state) const {
    if (floor < state.floor) return true;
    if (floor > state.floor) return false;
    return pairs < state.pairs;
}


bool State::isValid() const {
    if (floor < 1 || floor > 4) return false;
    for (const auto &pair : pairs) {
        // if generator is at the same floor, the chip is safe
        if (pair.first == pair.second) continue;
        // if another generator is at the same floor, the chip is dead
        for (const auto &pair2 : pairs) {
            if (pair2.second == pair.first) return false;
        }
    }
    return true;
}


bool State::isFinal() const {
    for (const auto &pair : pairs) {
        if (pair.first != 4 || pair.second != 4) return false;
    }
    return true;
}


State Part1::parse(const string &fileName) {
    State state;
    map<string, int> chips, generators;
    const auto lines = getFileLines(fileName);
    for (size_t i = 0; i < 4; ++i) {
        string line = lines[i];
        if (line.find("nothing") != string::npos)
            continue;
        line = line.substr(line.find("contains a ") + 11);
        line = removeSubstr(line, " and");
        line = removeSubstr(line, ".");        
        line = removeSubstr(line, ",");        
        const auto tokens = split(line, " a ");
        for (const auto &token : tokens) {
            if (token.find("generator") != string::npos) {
                generators.insert({removeSubstr(token, " generator"), i+1});
            } else {
                chips.insert({removeSubstr(token, "-compatible microchip"), i+1});
            }
        }
    }
    for (const auto &item : chips) {
        state.pairs.insert({ chips.at(item.first), generators.at(item.first) });
    }
    return state;
}


// list of all possible moves from a given state
set<State> getNextCandidates(const State &curr) {
    set<State> nextCandidates;  

    // move a single pair (one or both items of the pair)
    for (const auto &pair1 : curr.pairs) {
        set<Coordinates> potentialNextPairs;
        if (pair1.first == curr.floor) {
            potentialNextPairs.insert({ pair1.first + 1, pair1.second});
            potentialNextPairs.insert({ pair1.first - 1, pair1.second});
        }
        if (pair1.second == curr.floor) {
            potentialNextPairs.insert({ pair1.first, pair1.second + 1});
            potentialNextPairs.insert({ pair1.first, pair1.second - 1});
        }
        if (pair1.first == curr.floor && pair1.second == curr.floor) {
            potentialNextPairs.insert({ pair1.first + 1, pair1.second + 1});
            potentialNextPairs.insert({ pair1.first - 1, pair1.second - 1});
        }

        for (const auto &nextPair : potentialNextPairs) {
            State nextState = curr;
            nextState.moves++;
            const int floorDiff = (nextPair.first + nextPair.second) > (pair1.first + pair1.second) ? 1 : -1;
            nextState.floor = curr.floor + floorDiff;
            nextState.pairs.erase(nextState.pairs.find(pair1));
            nextState.pairs.insert(nextPair);
            nextCandidates.insert(nextState);
        }
    }

    // move items from 2 different pairs
    for (const auto &pair1 : curr.pairs) {
        multiset<Coordinates> otherSet(curr.pairs);
        otherSet.erase(otherSet.find(pair1));

        if (pair1.first == curr.floor) {
            for (const auto &pair2 : otherSet) {
                if (pair2.first == curr.floor) {
                    State nextStateUp = curr;
                    nextStateUp.moves++;
                    nextStateUp.floor++;
                    nextStateUp.pairs.erase(nextStateUp.pairs.find(pair1));
                    nextStateUp.pairs.erase(nextStateUp.pairs.find(pair2));
                    nextStateUp.pairs.insert({pair1.first + 1, pair1.second});
                    nextStateUp.pairs.insert({pair2.first + 1, pair2.second});
                    nextCandidates.insert(nextStateUp);
                    State nextStateDown = curr;
                    nextStateDown.moves++;
                    nextStateDown.floor--;
                    nextStateDown.pairs.erase(nextStateDown.pairs.find(pair1));
                    nextStateDown.pairs.erase(nextStateDown.pairs.find(pair2));
                    nextStateDown.pairs.insert({pair1.first - 1, pair1.second});
                    nextStateDown.pairs.insert({pair2.first - 1, pair2.second});
                    nextCandidates.insert(nextStateDown);
                } 
                if (pair2.second == curr.floor) {
                    State nextStateUp = curr;
                    nextStateUp.moves++;
                    nextStateUp.floor++;
                    nextStateUp.pairs.erase(nextStateUp.pairs.find(pair1));
                    nextStateUp.pairs.erase(nextStateUp.pairs.find(pair2));
                    nextStateUp.pairs.insert({pair1.first + 1, pair1.second});
                    nextStateUp.pairs.insert({pair2.first, pair2.second + 1});
                    nextCandidates.insert(nextStateUp);
                    State nextStateDown = curr;
                    nextStateDown.moves++;
                    nextStateDown.floor--;
                    nextStateDown.pairs.erase(nextStateDown.pairs.find(pair1));
                    nextStateDown.pairs.erase(nextStateDown.pairs.find(pair2));
                    nextStateDown.pairs.insert({pair1.first - 1, pair1.second});
                    nextStateDown.pairs.insert({pair2.first, pair2.second - 1});
                    nextCandidates.insert(nextStateDown);
                } 
            }
        }
        if (pair1.second == curr.floor) {
            for (const auto &pair2 : otherSet) {
                if (pair2.second == curr.floor) {
                    State nextStateUp = curr;
                    nextStateUp.moves++;
                    nextStateUp.floor++;
                    nextStateUp.pairs.erase(nextStateUp.pairs.find(pair1));
                    nextStateUp.pairs.erase(nextStateUp.pairs.find(pair2));
                    nextStateUp.pairs.insert({pair1.first, pair1.second + 1});
                    nextStateUp.pairs.insert({pair2.first, pair2.second + 1});
                    nextCandidates.insert(nextStateUp);
                    State nextStateDown = curr;
                    nextStateDown.moves++;
                    nextStateDown.floor--;
                    nextStateDown.pairs.erase(nextStateDown.pairs.find(pair1));
                    nextStateDown.pairs.erase(nextStateDown.pairs.find(pair2));
                    nextStateDown.pairs.insert({pair1.first, pair1.second - 1});
                    nextStateDown.pairs.insert({pair2.first, pair2.second - 1});
                    nextCandidates.insert(nextStateDown);
                } 
            }
        }
    }
    return nextCandidates;
}


int Part1::solve(const State &initialState) {
    set<State> seen = {};
    list<State> toCheck = { initialState };

    while (!toCheck.empty()) {
        auto curr = toCheck.front();
        toCheck.pop_front();
        for (const auto &candidate : getNextCandidates(curr)) {
            if (candidate.isValid()) {
                if (candidate.isFinal()) {
                    return candidate.moves;
                } else {
                    if (seen.find(candidate) == seen.end()
                        && find(toCheck.begin(), toCheck.end(), candidate) == toCheck.end()) {
                        toCheck.push_back(candidate);
                    }
                }
            }
        }
        seen.insert(curr);
    }
    return -1;
}
