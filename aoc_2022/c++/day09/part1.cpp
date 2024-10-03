#include "part1.h"

using namespace std;


namespace Day09 {

    vector<pair<Coord, int>> parse(const string& filename) {
        vector<pair<Coord, int>> moves;        

        const map<char, Coord> directions = {
            {'L', Coord::WEST  },
            {'R', Coord::EAST  },
            {'U', Coord::NORTH },
            {'D', Coord::SOUTH }
        };

        for (const auto& line : getFileLines(filename)) {
            const auto tokens = split(line, " ");
            moves.emplace_back(directions.at(tokens[0][0]), stoi(tokens[1]));
        }
        return moves;
    }


    namespace Part1 {

        Coord getNextTailCoord(const Coord& head, const Coord& tail) {
            // tail moves horizontally
            if (head.x == tail.x && abs(head.y - tail.y) > 1) {
                return { tail.x, tail.y + (head.y > tail.y ? 1 : -1) };
            }
            // tail moves vertically
            if (head.y == tail.y && abs(head.x - tail.x) > 1) {
                return { tail.x + (head.x > tail.x ? 1 : -1), tail.y };
            }
            // tail moves diagonally
            if (Coord::manhattan(head, tail) > 2) {
                return { tail.x + (head.x > tail.x ? 1 : -1), tail.y + (head.y > tail.y ? 1 : -1) };
            }
            // tail doesn't move
            return tail;
        }

        int solve(const vector<pair<Coord, int>>& moves) {
            Coord head { 0, 0 };
            Coord tail { 0, 0 };
            set<Coord> tailLocations { tail };
            for (const auto& [direction, count] : moves) {
                for (int i = 0; i < count; ++i) {
                    head += direction;
                    tail = getNextTailCoord(head, tail);
                    tailLocations.insert(tail);
                }
            }
            return tailLocations.size();
        }

    }
}
