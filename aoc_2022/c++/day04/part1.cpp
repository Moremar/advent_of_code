#include "part1.h"

using namespace std;


namespace Day04 {

    std::vector<pair<Section, Section>> parse(const string& filename) {
        vector<pair<Section, Section>> parsed;
        const regex pattern { "(\\d+)-(\\d+),(\\d+)-(\\d+)" };
        for (const string& line : getFileLines(filename)) {
            smatch match;
            regex_search(line.begin(), line.end(), match, pattern);
            parsed.emplace_back(Section{stoi(match[1]), stoi(match[2])}, Section{stoi(match[3]), stoi(match[4])});
        }
        return parsed;
    }

    namespace Part1 {
        int solve(const vector<pair<Section, Section>>& parsed) {
            int overlaps { 0 };
            for_each(parsed.begin(), parsed.end(), [&overlaps](const auto& elves){
                const auto& [elf1, elf2] = elves;
                if ((elf1.first >= elf2.first && elf1.second <= elf2.second)
                 || (elf2.first >= elf1.first && elf2.second <= elf1.second)) {
                    overlaps += 1;
                }
            });
            return overlaps;
        }
    }
}
