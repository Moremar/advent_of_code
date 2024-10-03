#include "part1.h"

using namespace std;


namespace Day06 {

    string parse(const string& filename) {
        return trim(getFileLines(filename)[0]);
    }

    int startOfUniqueSequence(const string& s, int sequenceSize) {
        set<char> chars;
        for (int i = 0; i < s.size() - sequenceSize - 1; ++i) {
            for_each(s.begin()+i, s.begin() + i + sequenceSize, [&chars](const char c) {
                chars.insert(c);
            });
            if (chars.size() == sequenceSize) {
                return i + sequenceSize;
            }
            chars.clear();
        }
        return -1;
    }

    namespace Part1 {
        int solve(const string& datastream) {
            return startOfUniqueSequence(datastream, 4);
        }
    }
}
