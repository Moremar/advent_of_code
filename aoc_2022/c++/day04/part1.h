#pragma once
#include "../Common/Utils.h"

using Section = std::pair<int, int>;

namespace Day04 {
    std::vector<std::pair<Section, Section>> parse(const std::string& filename);

    namespace Part1 {
        int solve(const std::vector<std::pair<Section, Section>>& input);
    }
}
