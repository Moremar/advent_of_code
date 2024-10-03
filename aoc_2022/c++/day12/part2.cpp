#include "part2.h"

using namespace std;


namespace Day12 {
    namespace Part2 {

        int solve(const tuple<World, Coord, Coord>& input) {
            const auto& [world, _, target] = input;
            vector<int> distances {};
            for (const auto& [position, elevation] : world) {
                if (elevation == 0) {
                    const int distance = Part1::solve({ world, position, target });
                    if (distance > 0) {
                        distances.push_back(distance);
                    }
                }
            }
            return *min_element(distances.begin(), distances.end());
        }

    }
}
