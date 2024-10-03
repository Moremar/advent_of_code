#pragma once
#include "../Common/Utils.h"


namespace Day15 {

    struct Sensor {
        Sensor(const Coord& pos, const Coord& beacon) : pos(pos), beacon(beacon) {}
        Coord pos;
        Coord beacon;
    };

    std::vector<Sensor> parse(const std::string& filename);


    namespace Part1 {

        // return a sorted list of disjoint intervals of the X values covered by the sensors for a given Y
        // if maxBound is provided, limit that scope to [0, maxBound]
        std::vector<std::pair<int, int>> findCoverageForY(const std::vector<Sensor>& sensors, const int targetY, const int maxBound = -1);

        int solve(const std::vector<Sensor>& sensors, const int targetY);

    }
}
