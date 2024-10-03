#pragma once
#include "../Common/Utils.h"


namespace Day17 {

    std::vector<char> parse(const std::string& filename);


    namespace Part1 {

        void dropShape(const std::vector<char>& winds, std::set<Coord>& world, int& height, int& rockId, int& windId);

        int solve(const std::vector<char>& winds);

    }
}
