#pragma once
#include "Utils.hpp"


class World {
public:
    World(int magicKey);
    bool isFree(const Coordinates &pair);

private:
    int myMagicKey;
    map<Coordinates, bool> myWorld;
};


namespace Part1 {  
    tuple<int, int, int> parse(const string &fileName);
    int solve(const tuple<int, int, int> &input);

    set<Coordinates> getNeighbors(const Coordinates &point);
}
