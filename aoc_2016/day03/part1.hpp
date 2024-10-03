#pragma once
#include "Utils.hpp"


// Parse one line of the input into a triangle
vector<int> parseTriangle(const string& line);


namespace Part1 {
    vector<vector<int>> parse(const string &fileName);
    int solve(vector<vector<int>> triangles);
}
