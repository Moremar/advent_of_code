#include "part1.hpp"

using namespace std;


vector<Node> Part1::parse(const string &fileName) {
    vector<Node> nodes;
    regex rgx("/dev/grid/node-x([0-9]+)-y([0-9]+) +([0-9]+)T +([0-9]+)T +([0-9]+)");
    int headerSize = 2;
    for (const auto line : getFileLines(fileName)) {
        if (headerSize > 0) {
            headerSize--;
            continue;
        }
        smatch match;
        regex_search(line.begin(), line.end(), match, rgx);
        nodes.emplace_back(Coordinates(stoi(match[1]), stoi(match[2])), stoi(match[3]), stoi(match[4]), stoi(match[5]));
    }
    return nodes;
}


int Part1::solve(const vector<Node> &nodes) {
    int pairs = 0;
    for (const auto &nodeA : nodes) {
        for (const auto &nodeB : nodes) {
            if (nodeA.coords != nodeB.coords && nodeA.used > 0 && nodeA.used <= nodeB.avail) {
                pairs++;
            }
        }
    }
    return pairs;
}
