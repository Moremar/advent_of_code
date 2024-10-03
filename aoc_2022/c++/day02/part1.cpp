#include "part1.h"

using namespace std;


namespace Day02 {

    static const map<char, Move_t> MOVES {
        { 'A', Move_t::ROCK }, { 'B', Move_t::PAPER }, { 'C', Move_t::SCISSORS }, 
        { 'X', Move_t::ROCK }, { 'Y', Move_t::PAPER }, { 'Z', Move_t::SCISSORS }
    };


    namespace Part1 {

        vector<Strategy> parse(const string& filename) {
            vector<Strategy> parsed;
            for (const string& line : getFileLines(filename)) {
                parsed.emplace_back(MOVES.at(line[0]), MOVES.at(line[2]));
            }
            return parsed;
        }

        int solve(const vector<Strategy>& parsed) {
            int score { 0 };
            for (const Strategy& strategy : parsed) {
                // shape score
                const auto& [hisPlay, myPlay] = strategy;
                score += val(strategy.second) + 1;
                // outcome score
                score += val(myPlay) == (val(hisPlay) + 1) % 3 ? 6    // Victory
                       : val(myPlay) == (val(hisPlay) + 2) % 3 ? 0    // Defeat
                       : 3;                                           // Draw
            }
            return score;
        }
    }
}
