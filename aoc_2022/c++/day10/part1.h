#pragma once
#include "../Common/Utils.h"


namespace Day10 {

    enum class Operator_t {
        noop = 0,
        addx = 1
    };

    std::vector<std::pair<Operator_t, int>> parse(const std::string& filename);

    namespace Part1 {
        int solve(const std::vector<std::pair<Operator_t, int>>& input);
    }
}
