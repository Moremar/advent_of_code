#include "part2.h"

using namespace std;


namespace Day24 {
    namespace Part2 {

        int solve(const tuple<Winds, Coord, Coord>& input) {
            const auto [initialWinds, start, target] = input;
            const int maxX = target.x - 1;
            const int maxY = target.y;
            map<int, Winds> winds;
            winds[0] = initialWinds;
            const int timeToTarget     = Part1::crossValley(winds,               0,  start, target, maxX, maxY);
            const int timeBackToStart  = Part1::crossValley(winds,    timeToTarget, target,  start, maxX, maxY);
            const int timeBackToTarget = Part1::crossValley(winds, timeBackToStart,  start, target, maxX, maxY);
            return timeBackToTarget;
        }

    }
}
