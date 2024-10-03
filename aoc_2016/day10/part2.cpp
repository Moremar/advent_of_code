#include "part2.hpp"

using namespace std;

int Factory::getChip(const string &loc) const {
    return *myChips.at(loc).begin();
}

int Part2::solve(const FactoryRules &rules) {
    Factory factory(rules);
    factory.run(-1, -1);  // run until the end
    return factory.getChip("output 0")
         * factory.getChip("output 1")
         * factory.getChip("output 2");
}
