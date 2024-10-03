#include "part1.hpp"

using namespace std;


World::World(int magicKey): myMagicKey(magicKey) {
    // starting point
    myWorld.insert({ make_pair(1, 1), true });
};


bool World::isFree(const Coordinates &pair) {
    if (pair.first < 0 || pair.second < 0)
        return false;
    if (myWorld.find(pair) == myWorld.end()) {
        int n = pair.first * pair.first
              + 3 * pair.first
              + 2 * pair.first * pair.second
              + pair.second
              + pair.second * pair.second
              + myMagicKey;
        // point is free if the number of bits in n is even
        int bits1 = 0;
        while (n > 0) {
            bits1 += n % 2;
            n = n >> 1;
        }
        myWorld.insert({pair, (bits1 % 2 == 0)});
    }
    return myWorld.at(pair);
}


tuple<int, int, int> Part1::parse(const string &fileName) {
    auto tokens = split(getFileLines(fileName)[0], " ");
    return make_tuple(stoi(tokens[0]), stoi(tokens[1]), stoi(tokens[2]));
}


set<Coordinates> Part1::getNeighbors(const Coordinates &point) {
    return {
        make_pair(point.first - 1, point.second),
        make_pair(point.first, point.second - 1),
        make_pair(point.first + 1, point.second),
        make_pair(point.first, point.second + 1)
    };
}

int Part1::solve(const tuple<int, int, int> &input) {
    World world(get<0>(input));
    auto target = make_pair(get<1>(input), get<2>(input));
    set<Coordinates> seen;
    list<pair<int, Coordinates>> toCheck = { {0, {1, 1}} }; // distance so far + (x, y)

    while (toCheck.size() > 0) {
        const auto curr = toCheck.front();
        const auto currDist = curr.first;
        const auto currPoint = curr.second;
        toCheck.pop_front();
        for (const auto &point : getNeighbors(currPoint)) {
            if (world.isFree(point) && seen.find(point) == seen.end()) {
                if (point == target) {
                    return currDist + 1;
                }
                toCheck.emplace_back(currDist + 1, point);
            }
        }
        seen.insert(currPoint);
    }
    throw AdventException("No route found to the target.");
}
