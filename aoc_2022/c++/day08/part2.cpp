#include "part2.h"

using namespace std;


namespace Day08 {
    namespace Part2 {

        int calculateScenicScore(const vector<vector<int>>& trees, int i, int j) {
            // tree is on the border
            if (i == 0 || j == 0 || i == trees.size() - 1 || j == trees[0].size() - 1) {
                return 0;
            }
            int west = 1, east = 1, north = 1, south = 1;
            // view to the west
            {
                int x = j-1;
                while (x > 0 && trees[i][x] < trees[i][j]) {
                    --x;
                    ++west;
                }
            }
            // view to the east
            {
                int x = j+1;
                while (x < trees[0].size()-1 && trees[i][x] < trees[i][j]) {
                    ++x;
                    ++east;
                }
            }
            // view to the north
            {
                int x = i-1;
                while (x > 0 && trees[x][j] < trees[i][j]) {
                    --x;
                    ++north;
                }
            }
            // view to the south
            {
                int x = i+1;
                while (x < trees.size()-1 && trees[x][j] < trees[i][j]) {
                    ++x;
                    ++south;
                }
            }
            return west * east * north * south;
        }

        int solve(const vector<vector<int>>& trees) {
            int maxScore = 0;
            for (int i = 0; i < trees.size(); ++i) {
                for (int j = 0; j < trees[0].size(); ++j) {
                    maxScore = max(maxScore, calculateScenicScore(trees, i, j));
                }
            }
            return maxScore;
        }

    }
}
