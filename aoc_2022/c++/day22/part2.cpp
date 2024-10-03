#include "part2.h"

using namespace std;

static const int RIGHT = 0, DOWN = 1, LEFT = 2, UP = 3;
static const vector<Coord> DIRS = { { 0, 1 }, { 1,  0 }, { 0, -1 }, { -1,  0 } };

// We build a trnasition map for each position that should wrap around.
// The world can be represented as a cube with the following faces.
// The TRANSITIONS map specifies how a face connects to another one.
//
//          +---+---+
//          | 2 | 1 |
//          +---+---+
//          | 3 |
//      +---+---+
//      | 5 | 4 |
//      +---+---+
//      | 6 |
//      +---+


// (next_pos, direction) -> (next pos after wrapping, direction after wrapping)
static map<pair<Coord, int>, pair<Coord, int>> TRANSITIONS {};

namespace Day22 {
    namespace Part2 {

        pair<Coord, int> Wrapper::wrap(const World& world, const Coord& pos, const int facing) const {
            return TRANSITIONS.at({ pos, facing });
        }

        void buildTransitions() {
            const int side = 50;
            for (int i = 1; i < side+1; ++i) {
                TRANSITIONS[{ Coord{ i, side + 1 }, LEFT }]                 = { Coord{ 3 * side + 1 - i, 1 }, RIGHT };        // 1 -> 5
                TRANSITIONS[{ Coord{ 3 * side + 1 - i, 1 }, LEFT }]         = { Coord{ i, side + 1 }, RIGHT };                // 5 -> 1
                TRANSITIONS[{ Coord{ 1, side + i }, UP }]                   = { Coord{ 3 * side + i, 1 }, RIGHT };            // 1 -> 6
                TRANSITIONS[{ Coord{ 3 * side + i, 1 }, LEFT }]             = { Coord{ 1, side + i }, DOWN };                 // 6 -> 1
                TRANSITIONS[{ Coord{ 1, 2 * side + i }, UP }]               = { Coord{ 4 * side, i }, UP };                   // 2 -> 6
                TRANSITIONS[{ Coord{ 4 * side, i }, DOWN }]                 = { Coord{ 1, 2 * side + i }, DOWN };             // 6 -> 2
                TRANSITIONS[{ Coord{ i, 3 * side }, RIGHT }]                = { Coord{ 3 * side + 1 - i, 2 * side }, LEFT };  // 2 -> 4
                TRANSITIONS[{ Coord{ 3 * side + 1 - i, 2 * side }, RIGHT }] = { Coord{ i, 3 * side }, LEFT };                 // 4 -> 2
                TRANSITIONS[{ Coord{ side, 2 * side + i }, DOWN }]          = { Coord{ side + i, 2 * side }, LEFT };          // 2 -> 3
                TRANSITIONS[{ Coord{ side + i, 2 * side }, RIGHT }]         = { Coord{ side, 2 * side + i }, UP };            // 3 -> 2
                TRANSITIONS[{ Coord{ side + i, side + 1 }, LEFT }]          = { Coord{ 2 * side + 1, i }, DOWN };             // 3 -> 5
                TRANSITIONS[{ Coord{ 2 * side + 1, i }, UP }]               = { Coord{ side + i, side + 1 }, RIGHT };         // 5 -> 3
                TRANSITIONS[{ Coord{ 3 * side, side + i }, DOWN }]          = { Coord{ 3 * side + i, side }, LEFT };          // 4 -> 6
                TRANSITIONS[{ Coord{ 3 * side + i, side }, RIGHT }]         = { Coord{ 3 * side, side + i }, UP };            // 6 -> 4
            }
        }

        int solve(const tuple<Coord, World, vector<Instruction>>& input) {
            const auto [start, world, instructions] = input;
            const Part2::Wrapper wrapper {};
            buildTransitions();
            return Part1::getFinalPassword(start, world, instructions, wrapper);        }
    }
}
