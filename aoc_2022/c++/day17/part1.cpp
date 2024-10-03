#include "part1.h"

using namespace std;


static const vector<set<Coord>> ROCKS {
    { Coord{1, 1}, Coord{2, 1}, Coord{3, 1}, Coord{4, 1} },               //  horizontal line
    { Coord{2, 1}, Coord{1, 2}, Coord{2, 2}, Coord{3, 2}, Coord{2, 3} },  //  cross
    { Coord{1, 1}, Coord{2, 1}, Coord{3, 1}, Coord{3, 2}, Coord{3, 3} },  //  reverse L
    { Coord{1, 1}, Coord{1, 2}, Coord{1, 3}, Coord{1, 4} },               //  vertical line
    { Coord{1, 1}, Coord{1, 2}, Coord{2, 1}, Coord{2, 2} }                //  square
};

static const Coord LEFT  { -1,  0 };
static const Coord RIGHT {  1,  0 };
static const Coord DOWN  {  0, -1 };


namespace Day17 {

    vector<char> parse(const string& filename) {
        vector<char> winds {};
        const string windsStr = getFileLines(filename)[0];
        for (const char& c : windsStr) {
            winds.push_back(c);
        }
        return winds;
    }

    namespace Part1 {

        void dropShape(const vector<char>& winds, set<Coord>& world, int& height, int& rockId, int& windId) {
            // start with the rock to drop at its starting position
            Coord shift { 2, height + 3 };
            set<Coord> rock;
            for (const auto& coord : ROCKS[(rockId++) % ROCKS.size()]) {
                rock.insert(coord + shift);
            }
            // apply the wind and the fall
            bool canMove = true;
            while (canMove) {
                set<Coord> nextRock;
                // apply the horizontal wind
                canMove = true;
                const char wind = winds[(windId++) % winds.size()];
                for (const auto& coord : rock) {
                    const Coord nextCoord { coord + (wind == '<' ? LEFT : RIGHT) };
                    if (nextCoord.x > 0 && nextCoord.x < 8 && nextCoord.y > 0 && world.find(nextCoord) == world.end()) {
                        nextRock.insert(nextCoord);
                    } else {
                        canMove = false;
                        break;
                    }
                }
                if (canMove) {
                    rock = nextRock;
                }
                // apply the vertical fall
                canMove = true;
                nextRock.clear();
                for (const auto& coord : rock) {
                    const Coord nextCoord { coord + DOWN };
                    if (nextCoord.x > 0 && nextCoord.x < 8 && nextCoord.y > 0 && world.find(nextCoord) == world.end()) {
                        nextRock.insert(nextCoord);
                    } else {
                        canMove = false;
                        break;
                    }
                }
                if (canMove) {
                    rock = nextRock;
                }
            }
            // save the new rock once it no longer moves
            for (const auto& coord : rock) {
                if (height < coord.y) {
                    height = coord.y;
                }
                world.insert(coord);
            }
        }


        int solve(const vector<char>& winds) {
            set<Coord> world {};
            int height = 0;
            int rockId = 0;
            int windId = 0;
            for (int i = 0; i < 2022; ++i) {
                dropShape(winds, world, height, rockId, windId);
            }
            return height;
        }

    }
}
