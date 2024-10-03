#include "part2.h"

using namespace std;


namespace Day14 {
    namespace Part2 {

        int solve(const World& world) {
            World worldCopy { world };
            int deepestPath = 0;
            for (const auto& [coord, _] : worldCopy) {
                deepestPath = max(deepestPath, coord.y);
            }
            // flow sand until the origin point is reached
            bool atRest = true;
            int droppedSand = 0;
            while (atRest) {
                atRest = Part1::dropSand(worldCopy, deepestPath, true);
                ++droppedSand;
            }
            // Part1::print(worldCopy);
            return droppedSand - 1;
        }

    }
}
