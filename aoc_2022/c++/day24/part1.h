#pragma once
#include "../Common/Utils.h"


namespace Day24 {

    using Winds = std::map<Coord, std::set<Coord>>;

    std::tuple<Winds, Coord, Coord> parse(const std::string& filename);

    namespace Part1 {

        int crossValley(std::map<int, Winds>& winds, int initialStep, const Coord& start, const Coord& target, int maxX, int maxY);

        int solve(const std::tuple<Winds, Coord, Coord>& input);

    }
}
