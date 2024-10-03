#include "part2.h"

using namespace std;


namespace Day09 {
    namespace Part2 {
        
        int solve(const vector<pair<Coord, int>>& moves) {
            const int knotsCount = 10;
            vector<Coord> rope { knotsCount, Coord{0, 0} };
            set<Coord> tailLocations { rope[knotsCount-1] };
            for (const auto& [direction, count] : moves) {
                for (int i = 0; i < count; ++i) {
                    rope[0] += direction;
                    for (int k = 1; k < knotsCount; ++k) {
                        rope[k] = Part1::getNextTailCoord(rope[k-1], rope[k]);
                    }
                    tailLocations.insert(rope[knotsCount-1]);
                }
            }
            return tailLocations.size();
        }

    }
}
