#include "part1.hpp"

using namespace std;


vector<pair<size_t, size_t>> Part1::parse(const string &fileName) {
    vector<pair<size_t, size_t>> spans;
    for (const auto &line : getFileLines(fileName)) {
        const auto limits = split(line, "-");
        spans.emplace_back(stoul(limits[0]), stoul(limits[1]));
    }
    sort(spans.begin(), spans.end(), [](auto span1, auto span2) {
        return span1.first < span2.first
            || (span1.first == span2.first && span1.second < span2.second);
    });
    return spans;
}

int Part1::solve(const vector<pair<size_t, size_t>> &spans) {
    size_t currIP = 0;
    for (const auto &span : spans) {
        if (currIP < span.first) {
            return currIP;
        }
        if (currIP <= span.second) {
            currIP = span.second + 1;
        }
    }
    return currIP;
}
