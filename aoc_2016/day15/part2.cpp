#include "part1.hpp"
#include "part2.hpp"

using namespace std;


size_t Part2::solve(const vector<Disc> &discs) {
    vector<Disc> updatedDiscs(discs);
    updatedDiscs.emplace_back(updatedDiscs.size() + 1, 11, 0);
    return Part1::solve(updatedDiscs);
}
