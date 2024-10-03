#pragma once
#include "../Common/Utils.h"


namespace Day18 {

    std::set<Coord3D> parse(const std::string& filename);


    namespace Part1 {

        int solve(const std::set<Coord3D>& cubes);

    }
}
