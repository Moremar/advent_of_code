#include "part1.hpp"
#include "part2.hpp"

using namespace std;


vector<vector<int>> Part2::parse(const string &fileName) {
    vector<vector<int>> triangles;
    vector<string> lines = getFileLines(fileName);
    while (lines.size() > 0) {
        // read original triangles
        vector<int> triangle1 = parseTriangle(lines[0]);
        vector<int> triangle2 = parseTriangle(lines[1]);
        vector<int> triangle3 = parseTriangle(lines[2]);
        
        // remove the lines we just read
        lines.erase(lines.begin(), lines.begin() + 3);
        
        // create the actual triangles
        vector<int> actual1 = {triangle1[0], triangle2[0], triangle3[0]};
        vector<int> actual2 = {triangle1[1], triangle2[1], triangle3[1]};
        vector<int> actual3 = {triangle1[2], triangle2[2], triangle3[2]};

        triangles.push_back(actual1);
        triangles.push_back(actual2);
        triangles.push_back(actual3);
    }
    return triangles;
}
