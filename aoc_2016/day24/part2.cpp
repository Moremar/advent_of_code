#include "part1.hpp"
#include "part2.hpp"

using namespace std;


int Part2::solve(const map<Coordinates, char> &worldMap) {
    World world(worldMap);
    return Part1::findSmallestRoute(world, true);
}
