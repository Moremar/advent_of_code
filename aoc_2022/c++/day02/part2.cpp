#include "part2.h"

using namespace std;


namespace Day02 {

    static const map<char, Move_t> MOVES {
        { 'A', Move_t::ROCK }, { 'B', Move_t::PAPER }, { 'C', Move_t::SCISSORS }
    };


    namespace Part2 {
        vector<Strategy> parse(const string& filename) {
            vector<Strategy> parsed;
            for (const string& line : getFileLines(filename)) {
                const Move_t hisPlay = MOVES.at(line[0]);
                const char   target  = line[2];
                const Move_t myPlay  = target == 'X' ? static_cast<Move_t>((val(hisPlay) + 2) % 3)
                                     : target == 'Y' ? hisPlay
                                     : static_cast<Move_t>((val(hisPlay) + 1) % 3);
                parsed.emplace_back(hisPlay, myPlay);
            }
            return parsed;
        }
    }
}
