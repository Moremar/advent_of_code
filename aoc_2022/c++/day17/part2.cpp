#include "part2.h"

using namespace std;


namespace Day17 {
    namespace Part2 {

        long long solve(const vector<char>& winds) {
            // drop the first 10'000 rocks
            array<int, 10'000> heights;
            int height = 0;
            int rockId = 0;
            int windId = 0;
            set<Coord> world {};
            for (int i = 0; i < 10000; ++i) {
                Part1::dropShape(winds, world, height, rockId, windId);
                heights[i] = height;
            }
            // create a vector of the difference between 2 successive heights
            vector<int> diffs {};
            for (int i = 1; i < 10000; ++i) {
                diffs.push_back(heights[i] - heights[i-1]);
            }
            // find the size of the cycle
            // we arbitrarily start to search from the 4000th rock and look for 100 common values
            int cycleSize = -1;
            int cycleHeight = -1;
            for (int i = 4001; i < 9900; ++i) {
                bool foundMatch = true;
                for (int j= 0; j < 100; ++j) {
                    if (diffs[i+j] != diffs[4000+j]) {
                        foundMatch = false;
                        break;
                    }
                }
                if (foundMatch) {
                    cycleSize = i - 4000;
                    cycleHeight = heights[i] - heights[4000];
                    break;
                }
            }
            const long long totalRocks = 1'000'000'000'000LL;
            const long long quotient   = totalRocks / static_cast<long long>(cycleSize);
            const long long remainder  = totalRocks % static_cast<long long>(cycleSize);
            return heights[cycleSize + remainder - 1LL] + (quotient - 1LL) * cycleHeight;
        }

    }
}
