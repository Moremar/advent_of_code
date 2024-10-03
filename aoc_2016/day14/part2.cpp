#include "part1.hpp"
#include "part2.hpp"

using namespace std;


int Part2::solve(const string &salt) {
    KeyGenerator generator(salt);
    return generator.findIthKey(64, 2016);
}
