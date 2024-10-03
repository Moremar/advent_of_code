#include "part1.hpp"
#include "part2.hpp"

using namespace std;


int Part2::solve(const pair<int, vector<uint8_t>> &input) {
    Room room(input.second);
    return room.countSafeTiles(400000);
}