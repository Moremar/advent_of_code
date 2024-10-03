#pragma once
#include "./part1.h"
#include "../Common/Utils.h"
 

namespace Day22 {
    namespace Part2 {

        // Wrapper for part 2
        class Wrapper : public IWrapper {
        public:
            std::pair<Coord, int> wrap(const World& world, const Coord& pos, const int facing) const override;
        };

        int solve(const std::tuple<Coord, World, std::vector<Instruction>>& input);

    }
}
