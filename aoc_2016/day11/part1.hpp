#pragma once
#include "Utils.hpp"


struct State {
    int moves = 0;
    int floor = 1;
    multiset<Coordinates> pairs;  // floor of chip + generator
    bool isValid() const;
    bool operator==(const State &state) const;
    bool operator<(const State &state) const;
    bool isFinal() const;
};

namespace Part1 {  
    State parse(const string &fileName);
    int solve(const State &state);
}
