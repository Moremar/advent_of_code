#include "part1.h"

using namespace std;

static const int RIGHT = 0, DOWN = 1, LEFT = 2, UP = 3;
static const vector<Coord> DIRS = { { 0, 1 }, { 1,  0 }, { 0, -1 }, { -1,  0 } };


namespace Day22 {

    tuple<Coord, World, vector<Instruction>> parse(const string& filename) {
        const auto lines = getFileLines(filename);
        Coord start { 0, 0 };
        // parse the map
        map<Coord, char> world {};
        for (int i = 0; i < lines.size() - 2; ++i) {
            for (int j = 0; j < lines[i].size(); ++j) {
                if (lines[i][j] != ' ') {
                    if (start == Coord{ 0, 0 }) {
                        start = Coord{ i + 1, j + 1 };   // coordinates start at 1
                    }
                    world.insert({ {i + 1, j + 1}, lines[i][j] });
                }
            }
        }
        // parse the instructions
        vector<Instruction> instructions {};
        const auto turns     = regexSplit(lines[lines.size()-1], regex{ "\\d+" });
        const auto distances = regexSplit(lines[lines.size()-1], regex{ "[LR]" });
        for (int i = 0; i < distances.size(); ++i) {
            instructions.emplace_back(stoi(distances[i]), turns[i][0]);
        }
        return { start, world, instructions };
    }


    namespace Part1 {

        pair<Coord, int> Wrapper::wrap(const World& world, const Coord& pos, const int facing) const {
            Coord nextPos = pos + DIRS[facing];
            if (facing == UP) {
                while (world.find(nextPos + DIRS[DOWN]) != world.end())  nextPos += DIRS[DOWN];
            } else if (facing == RIGHT) {
                while (world.find(nextPos + DIRS[LEFT]) != world.end())  nextPos += DIRS[LEFT];
            } else if (facing == DOWN) {
                while (world.find(nextPos + DIRS[UP]) != world.end())    nextPos += DIRS[UP];
            } else {
                while (world.find(nextPos + DIRS[RIGHT]) != world.end()) nextPos += DIRS[RIGHT];
            }
            return { nextPos, facing };
        }


        int getFinalPassword(
                const Coord& start,
                const World& world,
                const vector<Instruction>& instructions,
                const IWrapper& wrapper) {
            
            Coord pos = start;
            int facing = RIGHT;
            for (const auto& instruction : instructions) {
                // turn if needed
                if (instruction.turn == 'R') facing = (facing + 1) % 4;
                if (instruction.turn == 'L') facing = (facing + 3) % 4;
                // move forward in the facing direction
                for (int k = 0; k < instruction.distance; ++k) {
                    Coord nextPos = pos + DIRS[facing];
                    int nextFacing = facing;
                    if (world.find(nextPos) == world.end()) {
                        // wrap around
                        const auto [wrappedPos, wrappedFacing] = wrapper.wrap(world, pos, facing);
                        nextPos = wrappedPos;
                        nextFacing = wrappedFacing;
                    } 
                    if (world.at(nextPos) == '#') {
                        // facing a wall, stop the move for this instruction
                        break;
                    }
                    pos = nextPos;
                    facing = nextFacing;
                }
            }
            return 1000 * pos.x + 4 * pos.y + facing;
        }

        int solve(const tuple<Coord, World, vector<Instruction>>& input) {
            const auto [start, world, instructions] = input;
            const Wrapper wrapper {};
            return getFinalPassword(start, world, instructions, wrapper);
        };

    }
}
