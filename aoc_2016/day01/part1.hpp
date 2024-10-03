#pragma once
#include "Utils.hpp"


// constant scoped to the compilation unit
const vector<Coordinates> DIRECTIONS {
    {  0,  1 },       // NORTH
    {  1,  0 },       // EAST
    {  0, -1 },       // SOUTH
    { -1,  0 }        // WEST
};


namespace Part1 {  
    vector<pair<char, int>> parse(const string &fileName);
    int solve(const vector<pair<char, int>> &moves);
}
