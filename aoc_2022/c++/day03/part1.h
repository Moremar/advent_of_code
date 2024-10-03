#pragma once
#include "../Common/Utils.h"


namespace Day03 {

    using Bag = std::pair<std::set<char>, std::set<char>>;

    std::vector<Bag> parse(const std::string& filename);

    namespace Part1 {
        int solve(const std::vector<Bag>& input);
    }
}
