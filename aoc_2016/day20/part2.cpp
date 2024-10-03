#include "part1.hpp"
#include "part2.hpp"

using namespace std;


int Part2::solve(const vector<pair<size_t, size_t>> &spans) {
    size_t validIPs = 0;
    size_t currIP = 0;
    for (const auto &span : spans) {
        if (currIP < span.first) {
            validIPs += span.first - currIP;
        }
        if (currIP <= span.second) {
            currIP = span.second + 1;
        }
    }
    // add all IPs between the biggest max span limit and the max IP allowed
    size_t maxPossibleIP = numeric_limits<uint32_t>::max();
    if (currIP <= maxPossibleIP) {
        validIPs += maxPossibleIP - currIP + 1;
    }
    return validIPs;
}
