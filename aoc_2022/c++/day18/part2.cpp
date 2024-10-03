#include "part2.h"

using namespace std;


namespace Day18 {
    namespace Part2 {

        int solve(const set<Coord3D>& cubes) {
            int result = 0;
            // keep track of all cubes we have already analyzed
            set<Coord3D> inside;
            set<Coord3D> outside;
            for (const auto& cube : cubes) {
                for (const auto& neighbor : cube.neighbors()) {
                    if (cubes.find(neighbor) == cubes.end()) {
                        // the neighbor is air, find out if it is inside or outside
                        if (inside.find(neighbor) != inside.end()) {
                            continue;
                        }
                        if (outside.find(neighbor) != outside.end()) {
                            ++result;
                            continue;
                        }
                        // we dont know if the cube is inside or outside yet, find out with a BFS
                        set<Coord3D> currentGroup { };
                        deque<Coord3D> toCheck { neighbor };
                        bool isOutside = false;
                        while (toCheck.size() > 0 && !isOutside) {
                            const auto& currPos = toCheck.front();
                            if (currentGroup.find(currPos) != currentGroup.end()) {
                                toCheck.pop_front();
                                continue;
                            } else {
                                currentGroup.insert(currPos);
                            }
                            for (const auto& nextCoord : currPos.neighbors()) {
                                if (cubes.find(nextCoord) != cubes.end()) {
                                    continue;
                                }
                                if (inside.find(nextCoord) != inside.end()) {
                                    toCheck.clear(); // we are inside, no need to check the rest
                                    break;
                                }
                                if (outside.find(nextCoord) != outside.end() || nextCoord.x == 0 || nextCoord.y == 0 || nextCoord.z == 0) {
                                    isOutside = true;
                                    ++result;
                                    toCheck.clear(); // we are outside, no need to check the rest
                                    break;
                                }
                                toCheck.push_back(nextCoord);
                            }
                            if (toCheck.size() > 0) {
                                // if the deque was not emptied, pop the processed element
                                toCheck.pop_front();
                            }
                        }
                        for (const auto& coord : currentGroup) {
                            if (isOutside) {
                                outside.insert(coord);
                            } else {
                                inside.insert(coord);
                            }
                        }
                    }
                }
            }
            return result;
        }

    }
}
