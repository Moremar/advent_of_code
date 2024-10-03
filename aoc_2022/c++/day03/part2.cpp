#include "part2.h"

using namespace std;


namespace Day03 {
    namespace Part2 {
        int solve(const vector<Bag>& bags) {
            int res = 0;
            for (int i = 0; i < bags.size() / 3; ++i) {
                set<char> fullBag1 { bags[3*i].first };
                for (const auto item : bags[3*i].second) {
                    fullBag1.insert(item);
                }
                for (const auto item : fullBag1) {
                    const bool inBag2 = bags[3*i+1].first.find(item)  != bags[3*i+1].first.end()
                                     || bags[3*i+1].second.find(item) != bags[3*i+1].second.end();
                    const bool inBag3 = bags[3*i+2].first.find(item)  != bags[3*i+2].first.end()
                                     || bags[3*i+2].second.find(item) != bags[3*i+2].second.end();
                    if (inBag2 && inBag3) {
                        res += (item > 'Z') ? item - 'a' + 1 : item - 'A' + 27;
                    }
                }
            }
            return res;
        }
    }
}
