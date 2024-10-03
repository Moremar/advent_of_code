#include "part2.h"

using namespace std;


namespace Day01 {
    namespace Part2 {
        int solve(const vector<int>& parsed) {
            assert (parsed.size() >= 3);
            vector<int> vals { parsed };
            sort(vals.begin(), vals.end());
            return reduce(vals.end() - 3, vals.end());  // sum of the elements
        }
    }
}
