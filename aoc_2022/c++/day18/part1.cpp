#include "part1.h"

using namespace std;


namespace Day18 {

    set<Coord3D> parse(const string& filename) {
        set<Coord3D> cubes {};
        for (const auto& line : getFileLines(filename)) {
            const auto tokens = split(line, ",");
            cubes.insert({ stoi(tokens[0]), stoi(tokens[1]), stoi(tokens[2]) });
        }
        return cubes;
    }

    namespace Part1 {

        int solve(const set<Coord3D>& cubes) {
            int result = 0;
            for (const auto& cube : cubes) {
                for (const auto& neighbor : cube.neighbors()) {
                    if (cubes.find(neighbor) == cubes.end()) {
                        ++result;
                    }
                }
            }
            return result;
        }

    }
}
