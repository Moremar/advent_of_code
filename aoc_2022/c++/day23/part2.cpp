#include "part2.h"

using namespace std;


namespace Day23 {
    namespace Part2 {

        int solve(const vector<Coord>& initialElves) {            
            vector<Coord> elves       { initialElves };
            vector<Coord> suggestions (initialElves.size()); 
            vector<int>   suggested   (initialElves.size());  // use 0 and 1 since vector<bool> not supported

            int roundId = 0;
            bool moved = true;
            while (moved) {
                moved = Part1::playRound(elves, roundId++, suggestions, suggested);
            }
            return roundId;
        }

    }
}
