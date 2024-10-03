#pragma once
#include "Utils.hpp"


class KeyGenerator {
public:
    KeyGenerator(const string &salt);
    int findIthKey(int i, int stretchLevel);

private:
    string mySalt;
    set<int> myFoundKeys;
    int myCurrIdx = 0;
    map<string, set<int>> myPendingKeys; // search pattern : { key indices }

    void updatePending();
};


namespace Part1 {
    string parse(const string &fileName);
    int solve(const string &salt);
}
