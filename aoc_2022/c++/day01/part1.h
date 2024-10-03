#pragma once
#include "../Common/Utils.h"


namespace Day01 {

    std::vector<int> parse(const std::string& filename);

    namespace Part1 {
        int solve(const std::vector<int>& input);
    }
}
