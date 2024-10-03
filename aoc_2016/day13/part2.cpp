#include "part1.hpp"
#include "part2.hpp"

using namespace std;


int Part2::solve(const tuple<int, int, int> &input) {
    World world(get<0>(input));
    const int maxDist = 50;
    set<Coordinates> seen;
    list<pair<int, Coordinates>> toCheck = { {0, {1, 1}} }; // distance so far + (x, y)

    while (toCheck.size() > 0) {
        const auto curr = toCheck.front();
        const auto currDist = curr.first;
        const auto currPoint = curr.second;
        toCheck.pop_front();
        // break if we have already seen all accessible points within the limit distance
        if (currDist > maxDist) {
            break;
        }
        for (const auto &point : Part1::getNeighbors(currPoint)) {
            if (world.isFree(point) && seen.find(point) == seen.end()) {
                toCheck.emplace_back(currDist + 1, point);
            }
        }
        seen.insert(currPoint);
    }
    return seen.size();
}
