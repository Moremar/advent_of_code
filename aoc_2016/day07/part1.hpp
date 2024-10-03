#pragma once
#include "Utils.hpp"


class IPv7 {
    public:
    IPv7(const string &str);
    bool supportTLS() const;
    bool supportSSL() const;  // for part 2 only

    private:
    vector<string> mySupernetSequences;
    vector<string> myHypernetSequences;
};

namespace Part1 {
    vector<IPv7> parse(const string &filePath);
    int solve(const vector<IPv7> &ipv7s);
}