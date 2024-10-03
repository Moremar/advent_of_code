#pragma once
#include "../Common/Utils.h"


namespace Day09 {

    std::vector<std::pair<Coord, int>> parse(const std::string& filename);

    namespace Part1 {

        Coord getNextTailCoord(const Coord& head, const Coord& tail);

        int solve(const std::vector<std::pair<Coord, int>>& moves);

    }
}
