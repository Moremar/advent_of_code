#include "part1.hpp"

using namespace std;


string Part1::decompress(const string &compressed) {
    size_t pos = 0;
    ostringstream oss;
    regex rgx("\\(([0-9]+)x([0-9]+)\\)");
    while(pos < compressed.size()) {
        if (compressed.at(pos) != '(') {
            oss << compressed.at(pos);
            pos++;
            continue;
        }
        // found a marker
        const auto markerSize = compressed.substr(pos).find(")") + 1;
        const string marker = compressed.substr(pos, markerSize);
        smatch match;
        regex_search(marker.begin(), marker.end(), match, rgx);
        const size_t repeatChars = stoul(match[1]);
        const size_t repeatTimes = stoul(match[2]);
        const string repeatSeq = compressed.substr(pos + markerSize, repeatChars);
        // add the repeated sequence to the result
        for (size_t i = 0; i < repeatTimes; i++) {
            oss << repeatSeq;
        }
        pos += markerSize + repeatChars;
    }
    return oss.str();
}


string Part1::parse(const string &filePath) {
    return getFileLines(filePath)[0];
}


 int Part1::solve(const string &compressed) {
    return decompress(compressed).size();
}
