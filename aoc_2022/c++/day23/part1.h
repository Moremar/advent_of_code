#pragma once
#include "../Common/Utils.h"


namespace Day23 {

    std::vector<Coord> parse(const std::string& filename);

    namespace Part1 {

        bool playRound(std::vector<Coord>& elves, int roundId, std::vector<Coord>& suggestions, std::vector<int>& suggested);

        int solve(const std::vector<Coord>& initialElves);

    }
}
