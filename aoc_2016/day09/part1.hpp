#pragma once
#include "Utils.hpp"


namespace Part1 {
    string parse(const string &filePath);
    int solve(const string &compressed);

    string decompress(const string &compressed);
}
