#include "part1.h"

using namespace std;

static const Coord NORTH { -1, 0 };
static const Coord EAST {  0, 1 };
static const Coord SOUTH { 1, 0 };
static const Coord WEST { 0, -1 };


namespace Day23 {

    vector<Coord> parse(const string& filename) {
        vector<Coord> elves {};
        const auto lines = getFileLines(filename);
        for (int i = 0; i < lines.size(); ++i) {
            for (int j = 0; j < lines.size(); ++j) {
                if (lines[i][j] == '#') {
                    elves.emplace_back(i, j);
                }
            }
        }
        return elves;
    }


    namespace Part1 {

        vector<Coord> getNeighbors(const Coord& coord) {
            return {
                coord + WEST + NORTH,   coord + NORTH,   coord + NORTH + EAST, 
                coord + WEST,                            coord + EAST, 
                coord + SOUTH + WEST,   coord + SOUTH,   coord + EAST + SOUTH
            };
        }

        vector<vector<Coord>> getNeighborGroups(const Coord& coord) {
            return {
                { coord + NORTH,  coord + WEST + NORTH, coord + NORTH + EAST },  // N + NW + NE 
                { coord + SOUTH,  coord + EAST + SOUTH, coord + SOUTH + WEST },  // S + SE + SW
                { coord + WEST,   coord + SOUTH + WEST, coord + NORTH + WEST },  // W + NW + SW
                { coord + EAST,   coord + EAST + SOUTH, coord + EAST + NORTH }   // E + SE + NE
            };
        }


        bool playRound(vector<Coord>& elves, int roundId, vector<Coord>& suggestions, vector<int>& suggested) {
            const set<Coord> elvesSet { elves.begin(), elves.end() };
            map<Coord, int> suggestionCount {};

            // all elves suggest their next move
            for (int i = 0; i < elves.size(); ++i) {
                const auto& elf = elves[i];
                const auto neighbors = getNeighbors(elf);
                const auto neighborGroups = getNeighborGroups(elf);
                suggested[i] = 0;
                // do not move if there are no other elves around
                if (all_of(neighbors.begin(), neighbors.end(), [&elvesSet](const Coord& neighbor){ 
                    return elvesSet.find(neighbor) == elvesSet.end();
                })) {
                    continue;
                }
                // test each of the 4 directions, and move if no one is in the 3 cells in that direction
                for (int k = 0; k < 4; ++k) {
                    const auto& group = neighborGroups[(roundId+k) % 4];
                    if (all_of(group.begin(), group.end(), [&elvesSet](const Coord& neighbor){ 
                        return elvesSet.find(neighbor) == elvesSet.end();
                    })) {
                        suggested[i] = 1;
                        suggestions[i] = *(group.begin());
                        suggestionCount[suggestions[i]] += 1;
                        break;
                    }
                }
            }
            // build the next elves vector
            bool moved = false;
            for (int i = 0; i < elves.size(); ++i) {
                if (suggested[i] == 0 || suggestionCount[suggestions[i]] > 1) {
                    continue;
                }
                elves[i] = suggestions[i];
                moved = true;
            }
            return moved;
        }


        int solve(const vector<Coord>& initialElves) {
            vector<Coord> suggestions(initialElves.size()); 
            vector<int>   suggested(initialElves.size());    // use 0 and 1 since vector<bool> not supported
            vector<Coord> elves { initialElves };

            // play 10 rounds
            for (int roundId = 0; roundId < 10; ++roundId) {
                playRound(elves, roundId, suggestions, suggested);
            }

            // return the number of empty cells in the rectangle
            int minX = elves.begin()->x, maxX = elves.begin()->x;
            int minY = elves.begin()->y, maxY = elves.begin()->y;
            for (const auto elf : elves) {
                minX = min(minX, elf.x);
                maxX = max(maxX, elf.x);
                minY = min(minY, elf.y);
                maxY = max(maxY, elf.y);
            }
            return (maxX - minX + 1) * (maxY - minY + 1) - elves.size();
        }

    }
}
