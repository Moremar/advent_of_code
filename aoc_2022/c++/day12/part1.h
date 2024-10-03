#pragma once
#include "../Common/Utils.h"


namespace Day12 {

    // type alias
    using World = std::map<Coord, int>;

    std::tuple<World, Coord, Coord> parse(const std::string& filename);

    namespace Part1 {

        int solve(const std::tuple<World, Coord, Coord>& input);

    }
}
