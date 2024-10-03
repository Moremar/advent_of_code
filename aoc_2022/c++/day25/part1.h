#pragma once
#include "../Common/Utils.h"


namespace Day25 {

    std::vector<std::string> parse(const std::string& filename);

    namespace Part1 {

        long long   snafuToDecimal(const std::string& snafu);
        std::string decimalToSnafu(const long long n);

        string solve(const std::vector<std::string>& snafus);

    }
}
