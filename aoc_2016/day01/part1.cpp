#include "part1.hpp"

using namespace std;


vector<pair<char, int>> Part1::parse(const string &fileName) {
    string line = getFileLines(fileName)[0];
    vector<pair<char, int>> moves;
    for (const string &token : split(line, ", ")) {
        moves.push_back(make_pair(token[0], stoi(token.substr(1))));
    }
    return moves;
}

int Part1::solve(const vector<pair<char, int>> &moves) {
    Coordinates position(0, 0);
    Coordinates facing = DIRECTIONS[0];  // start facing NORTH

    for(const auto &move : moves) {
        auto facing_itr = find(DIRECTIONS.begin(), DIRECTIONS.end(), facing);
        int facing_index = (int) distance(DIRECTIONS.begin(), facing_itr);
        facing = DIRECTIONS[(facing_index + (move.first == 'R' ? 1 : -1) + 4) % 4];
        position = position + facing * move.second;
    }
    return abs(position.first) + abs(position.second);
}
