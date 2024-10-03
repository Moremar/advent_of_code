#pragma once
#include "Utils.hpp"


class World {
public:
    World(const map<Coordinates, char> &worldMap);
    Coordinates getStartPoint() const;
    size_t getKeysCount() const;
    bool hasKey(const Coordinates &coord) const;
    char getKey(const Coordinates &coord) const;
    map<Coordinates, map<Coordinates, int>> getGraph() const;
private:
    void buildGraph();
    void simplifyGraph();
    Coordinates start;
    map<Coordinates, char> worldMap;
    map<Coordinates, char> keys;
    map<Coordinates, map<Coordinates, int>> graph;
};


struct State {
    State(const Coordinates &pos, const set<char> &keys, int dist)
        : pos(pos), keys(keys), dist(dist) {}
    bool operator<(const State other) const;
    Coordinates pos;
    set<char> keys;
    int dist;
};


namespace Part1 {  
    map<Coordinates, char> parse(const string &fileName);
    int solve(const map<Coordinates, char> &worldMap);

    int findSmallestRoute(const World &world, bool goBackHome);
}
