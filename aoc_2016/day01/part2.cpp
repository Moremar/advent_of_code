#include "part1.hpp"
#include "part2.hpp"

using namespace std;


int Part2::solve(const vector<pair<char, int>> &moves) {
    Coordinates position(0, 0);
    Coordinates facing = DIRECTIONS[0];  // start facing NORTH
    set<Coordinates> seen;

    for(const auto &move : moves) {
        auto facing_itr = find(DIRECTIONS.begin(), DIRECTIONS.end(), facing);
        int facing_index = (int) distance(DIRECTIONS.begin(), facing_itr);
        facing = DIRECTIONS[(facing_index + (move.first == 'R' ? 1 : -1) + 4) % 4];
        for (int i = 0; i < move.second; ++i) {
            // process all points in the move 1 by 1 to add them in the "seen" vector
            seen.insert(position);
            position = position + facing;
            if (seen.find(position) != seen.end()) {
                return abs(position.first) + abs(position.second);
            }
        }
    }
    throw AdventException("Santa did not visit any position twice.");
}
