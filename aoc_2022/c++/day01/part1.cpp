#include "part1.h"

using namespace std;


namespace Day01 {

    vector<int> parse(const string& filename) {
        vector<int> parsed;
        int curr = 0;
        for (const string& line : getFileLines(filename)) {
            if (trim(line).size()) {
                curr += stoi(line);
            } else {
                parsed.push_back(curr);
                curr = 0;
            }
        }
        return parsed;
    }

    namespace Part1 {
        int solve(const vector<int>& parsed) {
            return *max_element(parsed.begin(), parsed.end());
        }
    }
}
