#pragma once
#include "../Common/Utils.h"


namespace Day06 {
    string parse(const std::string& filename);
    int startOfUniqueSequence(const std::string& s, int sequenceSize);

    namespace Part1 {
        int solve(const std::string& input);
    }
}
