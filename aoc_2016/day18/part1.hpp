#pragma once
#include "Utils.hpp"


class Room {
public:
    Room(const vector<uint8_t> &firstRow);
    int countSafeTiles(int rows);

private:
    int myRowsCount = 0;
    vector<uint8_t> v1, v2;
};


namespace Part1 {  
    pair<int, vector<uint8_t>> parse(const string &fileName);
    int solve(const pair<int, vector<uint8_t>> &input);
}
