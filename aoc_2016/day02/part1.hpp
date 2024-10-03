#pragma once
#include "Utils.hpp"


namespace Part1 {
    vector<vector<char>> parse(const string &fileName);
    int solve(vector<vector<char>> directions);
    void next_position(const char& c, Coordinates &coords);
}
