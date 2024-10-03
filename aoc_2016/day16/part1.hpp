#pragma once
#include "Utils.hpp"


namespace Part1 {  
    vector<char> parse(const string &fileName);
    string solve(const vector<char> &initialKey); 
    string solveForDiscSpace(const vector<char> &initialKey, size_t discSpace);
}
