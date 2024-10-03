#include "part1.hpp"

using namespace std;


vector<int> parseTriangle(const string& line) {
    vector<int> triangle;
    vector<string> numbers_str = split(line, " ");
    for (const string &number_str : numbers_str) {
        string trimmed = trim(number_str);
        if (trimmed.size() > 0) {
            triangle.push_back(stoi(trimmed));
        }
    }
    return triangle;
}


vector<vector<int>> Part1::parse(const string &fileName) {
    vector<vector<int>> triangles;
    for(const string &line : getFileLines(fileName)) {
        triangles.push_back(parseTriangle(line));
    }
    return triangles;
}


int Part1::solve(vector<vector<int>> triangles) {
    int possible = 0;
    for(auto triangle : triangles) {
        sort(triangle.begin(), triangle.end());
        if (triangle[2] < triangle[0] + triangle[1]) {
            possible++;
        }
    }
    return possible;
}
