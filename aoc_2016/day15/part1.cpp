#include "part1.hpp"

using namespace std;


vector<Disc> Part1::parse(const string &fileName) {
    vector<Disc> discs;
    regex rgx("Disc #([0-9]+) has ([0-9]+) positions; at time=0, it is at position ([0-9]+).");
    for (const auto &line : getFileLines(fileName)) {
        smatch match;
        if (regex_search(line.begin(), line.end(), match, rgx)) {
            discs.emplace_back(stoi(match[1]), stoi(match[2]), stoi(match[3]));
        }
    }
    return discs;
}


size_t Part1::solve(const vector<Disc> &discs) {
    size_t time = 0;
    bool pass;
    while (true) {
        pass = true;
        for (const auto &disc: discs) {
            if ((time + disc.discId + disc.initPos) % disc.totalPos != 0) {
                pass = false;
                break;
            }
        }
        if (pass) return time;
        time++;
    };
}
