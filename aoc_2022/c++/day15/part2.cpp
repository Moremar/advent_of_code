#include "part2.h"

using namespace std;


namespace Day15 {
    namespace Part2 {

        long long solve(const vector<Sensor>& sensors, const int maxBound) {
            for (int y = 0; y <= maxBound; ++y) {
                const auto intervals = Part1::findCoverageForY(sensors, y, maxBound);
                if (intervals.size() != 1) {
                    assert (intervals.size() == 2);
                    assert (intervals[0].second + 2 == intervals[1].first);  // only a 1 cell gap in the coverage
                    return static_cast<long long>(intervals[0].second + 1) * 4'000'000LL + static_cast<long long>(y);
                }
            }
            return -1;
        }

    }
}
