#include "part2.h"

using namespace std;


namespace Day13 {
    namespace Part2 {

        int solve(const vector<pair<Value, Value>>& packets) {
            const Value divider1 = Part1::parseValue("[[2]]");
            const Value divider2 = Part1::parseValue("[[6]]");
            vector<Value> sortedPackets { divider1, divider2 };
            for (const auto& [pck1, pck2] : packets) {
                sortedPackets.push_back(pck1);
                sortedPackets.push_back(pck2);
            }
            sort(sortedPackets.begin(), sortedPackets.end());

            const auto posDivider1 = find(sortedPackets.begin(), sortedPackets.end(), divider1);
            const auto posDivider2 = find(sortedPackets.begin(), sortedPackets.end(), divider2);

            return (posDivider1 - sortedPackets.begin() + 1) * (posDivider2 - sortedPackets.begin() + 1);
        }

    }
}
