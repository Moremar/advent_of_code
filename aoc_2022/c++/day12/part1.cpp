#include "part1.h"

using namespace std;


namespace Day12 {

    tuple<World, Coord, Coord> parse(const string& filename) {
        World world {};
        Coord start, target;
        const auto lines = getFileLines(filename);
        for (int i = 0; i < lines.size(); ++i) {
            for (int j = 0; j < lines[0].size(); ++j) {
                char elevation = lines[i][j];
                if (elevation == 'S') {
                    start = Coord{ i, j };
                    elevation = 'a';
                }
                if (elevation == 'E') {
                    target = Coord{ i, j };
                    elevation = 'z';
                }
                world[Coord{ i, j }] = elevation - 'a';
            }
        }
        return { world, start, target };
    }


    namespace Part1 {

        int solve(const tuple<World, Coord, Coord>& input) {
            const auto& [world, start, target] = input;
            set<Coord> seen { start };
            deque<tuple<Coord, int>> toCheck { { start, 0 } };
            while (toCheck.size() > 0) {
                const auto& [position, distance] = toCheck.front();
                for (const auto& neighbor : position.neighbors()) {
                    if (world.find(neighbor) == world.end()) {
                        // out of bound
                        continue;
                    }
                    if (seen.find(neighbor) != seen.end()) {
                        // this position was already checked before
                        continue;
                    }
                    if (world.at(neighbor) > world.at(position) + 1) {
                        // too high, cannot climb
                        continue;
                    }
                    if (neighbor == target) {
                        return distance + 1;
                    }
                    seen.insert(neighbor);
                    toCheck.push_back({ neighbor, distance + 1 });
                }
                toCheck.pop_front();
            }
            return -1;
        }

    }
}
