#include "part1.h"

using namespace std;


namespace Day03 {

    vector<Bag> parse(const string& filename) {
        vector<Bag> parsed;
        for (const string& line : getFileLines(filename)) {
            const string half1 = line.substr(0, line.size() / 2);
            const string half2 = line.substr(line.size() / 2);
            set<char> list1 = { half1.begin(), half1.end() };
            set<char> list2 = { half2.begin(), half2.end() };
            parsed.emplace_back(list1, list2);
        }
        return parsed;
    }

    namespace Part1 {
        int solve(const vector<Bag>& bags) {
            int res = 0;
            for (const auto& [half1, half2] : bags) {
                for (const char item : half1) {
                    if (half2.find(item) != half2.end()) {
                        res += (item > 'Z') ? item - 'a' + 1 : item - 'A' + 27;
                        break;
                    }
                }
            }
            return res;
        }
    }
}
