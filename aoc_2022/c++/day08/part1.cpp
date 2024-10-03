#include "part1.h"

using namespace std;


namespace Day08 {

    vector<vector<int>> parse(const string& filename) {
        vector<vector<int>> trees;
        const auto lines = getFileLines(filename);
        for (int i = 0; i < lines.size(); ++i) {
            trees.emplace_back(lines[0].size(), 0);
            for (int j = 0; j < lines[i].size(); ++j) {
                trees[i][j] = stoi(string{lines[i][j]});
            }
        }
        return trees;
    }


    namespace Part1 {

        int isVisible(const vector<vector<int>>& trees, int i, int j) {
            // tree is on the border
            if (i == 0 || j == 0 || i == trees.size() - 1 || j == trees[0].size() - 1) {
                return true;
            }
            // tree is visible from the west
            if (all_of(trees[i].begin(), trees[i].begin() + j, [&](int height) { return height < trees[i][j]; })) {
                return true;
            }
            // tree is visible from the east
            if (all_of(trees[i].begin()+j+1, trees[i].end(), [&](int height) { return height < trees[i][j]; })) {
                return true;
            }
            // tree is visible from the north
            vector<int> vNorth(i);
            iota(vNorth.begin(), vNorth.end(), 0);   // set the vector to [1, 2, 3, ..., i-1]
            if (all_of(vNorth.begin(), vNorth.end(), [&](int x) { return trees[x][j] < trees[i][j]; })) {
                return true;
            }
            // tree is visible from the south
            vector<int> vSouth(trees.size()-i-1);
            iota(vSouth.begin(), vSouth.end(), 0);   // set the vector to [1, 2, 3, ..., N-i]
            if (all_of(vSouth.begin(), vSouth.end(), [&](int x) { return trees[trees.size()-1-x][j] < trees[i][j]; })) {
                return true;
            }
            // tree is not visible
            return false;
        }

        int solve(const vector<vector<int>>& trees) {
            int result = 0;
            for (int i = 0; i < trees.size(); ++i) {
                for (int j = 0; j < trees[0].size(); ++j) {
                    if (isVisible(trees, i, j)) {
                        ++result;
                    }
                }
            }
            return result;
        }

    }
}
