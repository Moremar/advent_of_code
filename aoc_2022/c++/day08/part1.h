#pragma once
#include "../Common/Utils.h"


namespace Day08 {

    std::vector<std::vector<int>> parse(const std::string& filename);

    namespace Part1 {
        int solve(const std::vector<std::vector<int>>& trees);
    }
}
