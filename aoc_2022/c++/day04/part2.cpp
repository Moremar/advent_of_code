#include "part2.h"

using namespace std;


namespace Day04 {
    namespace Part2 {
        int solve(const vector<pair<Section, Section>>& parsed) {
            int overlaps { 0 };
            for_each(parsed.begin(), parsed.end(), [&overlaps](const auto& elves){
                const auto& [elf1, elf2] = elves;
                if ((elf1.first >= elf2.first && elf1.first <= elf2.second)
                 || (elf1.second >= elf2.first && elf1.second <= elf2.second)
                 || (elf2.first >= elf1.first && elf2.first <= elf1.second)
                 || (elf2.second >= elf1.first && elf2.second <= elf1.second)) {
                    overlaps += 1;
                }
            });
            return overlaps;
        }
    }
}
