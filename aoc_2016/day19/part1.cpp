#include "part1.hpp"

using namespace std;


int Part1::parse(const string &fileName) {
    return stoi(getFileLines(fileName)[0]);
}

int Part1::solve(int elves) {
    // circular linked list of all players
    map<int, int> circle;
    for (int i = 1; i < elves; ++i) {
        circle.insert({ i, i+1 });
    }
    circle.insert({ elves, 1 });
    int curr = 1;

    // remove the next player and go to the next
    while (circle.at(curr) != curr) {
        circle[curr] = circle.at(circle.at(curr));
        curr = circle.at(curr);
    }
    return curr;
}
