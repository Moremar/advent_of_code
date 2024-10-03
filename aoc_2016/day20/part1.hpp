#pragma once
#include "Utils.hpp"


namespace Part1 {  
    vector<pair<size_t, size_t>> parse(const string &fileName);
    int solve(const vector<pair<size_t, size_t>> &spans);
}
