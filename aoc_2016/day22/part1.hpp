#pragma once
#include "Utils.hpp"


struct Node {
    Node(const Coordinates coords, int size, int used, int avail)
        : coords(coords), size(size), used(used), avail(avail) {}
    Coordinates coords;
    int size, used, avail;
};


namespace Part1 {  
    vector<Node> parse(const string &fileName);
    int solve(const vector<Node> &nodes);
}
