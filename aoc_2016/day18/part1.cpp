#include "part1.hpp"

using namespace std;


Room::Room(const vector<uint8_t> &firstRow) {
    myRowsCount = 1;
    // we use only 2 vectors v1 and v2 to compute the next state at each state
    // 0 is a safe tile, 1 is a trap
    // we use a 0 filler at the beginning and end of the array for walls
    v1.push_back(0);
    copy(firstRow.begin(), firstRow.end(), back_inserter(v1));
    v1.push_back(0);
    v2.resize(v1.size());  // just for the size
}


int Room::countSafeTiles(int rows) {
    // does not count the first and last elements of the row (walls)
    auto safeTiles = count(v1.begin() + 1, v1.end() -1, uint8_t(0));
    while (myRowsCount < rows) {
        // the rules can be simplified to a XOR :
        // a cell is a trap if the previous left XOR the previous right is a trap 
        for (size_t i = 1; i < v1.size() - 1; ++i) {
            v2[i] = v1[i-1] ^ v1[i+1];
        }
        safeTiles += count(v2.begin() + 1, v2.end() - 1, uint8_t(0));
        v1.swap(v2);
        myRowsCount++;
    }
    return safeTiles;
}


pair<int, vector<uint8_t>> Part1::parse(const string &fileName) {
    int rowsCount = stoi(getFileLines(fileName)[0]);
    const string rowStr = getFileLines(fileName)[1];
    vector<uint8_t> row;
    transform(rowStr.begin(), rowStr.end(), back_inserter(row), [](const char &c) {
        return c == '.' ? uint8_t(0) : uint8_t(1);
    });
    return { rowsCount, row };
}


int Part1::solve(const pair<int, vector<uint8_t>> &input) {
    Room room(input.second);
    return room.countSafeTiles(input.first);
}
