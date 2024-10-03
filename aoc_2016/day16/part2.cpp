#include "part1.hpp"
#include "part2.hpp"

using namespace std;


string Part2::solve(const vector<char> &initialKey) {
    return Part1::solveForDiscSpace(initialKey, 35651584);
}
