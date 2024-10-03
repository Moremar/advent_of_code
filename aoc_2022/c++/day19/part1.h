#pragma once
#include "../Common/Utils.h"


namespace Day19 {

    using Blueprint = std::array<std::array<int, 4>, 4>;

    std::vector<Blueprint> parse(const std::string& filename);


    namespace Part1 {

        int solve(const std::vector<Blueprint>& blueprints);

    }
}
