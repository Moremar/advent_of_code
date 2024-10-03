#pragma once
#include "Utils.hpp"


struct Disc {
    Disc(size_t discId, size_t totalPos, size_t initPos)
        : discId(discId), totalPos(totalPos), initPos(initPos) {}
    size_t discId, totalPos, initPos;
};


namespace Part1 {  
    vector<Disc> parse(const string &fileName);
    size_t solve(const vector<Disc> &discs);
}
