#include "part1.hpp"

using namespace std;


vector<char> Part1::parse(const string &fileName) {
    const string line = getFileLines(fileName)[0];
    return { line.begin(), line.end() };
}


vector<char> checksum(const vector<char> &input, size_t targetSize) {
    vector<char> res;
    res.reserve(targetSize / 2);
    for (size_t i = 0; i < targetSize/2; ++i) {
        res.push_back(input.at(2 * i) == input.at(2 * i + 1) ? '1' : '0');
    }
    return (res.size() % 2 == 0) ? checksum(res, res.size()) : res;
}


string Part1::solveForDiscSpace(const vector<char> &initialKey, size_t discSpace) {
    auto curr = initialKey;
    // get a long enough data sequence by dragon curve
    while (curr.size() < discSpace) {
        vector<char> next;
        next.reserve(curr.size() * 2 + 1);
        copy(curr.begin(), curr.end(), back_inserter(next));
        next.push_back('0');
        transform(curr.rbegin(), curr.rend(), back_inserter(next), [](const char &c) {
            return c == '0' ? '1' : '0';
        });
        curr = next;
    }
    const auto check = checksum(curr, discSpace);
    return string(check.begin(), check.end());

}


string Part1::solve(const vector<char> &initialKey) {
    return solveForDiscSpace(initialKey, 272);
}
